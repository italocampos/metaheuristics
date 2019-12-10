''' This file implements the Tabu Search to the modeled problem. '''

from tl import TabuList
from models import model_33bus
from tools import *
from random import random
from pandapower import runpp
from time import time


def run(loops = 10):

	results = list()
		
	for step in range(loops):

		print('\n\nSTEP %d ---------------------------------------------' % step)

		# Extra variables
		elapsed_time = 0
		

		# DEFINING GLOBAL VARIABLES AND PARAMETERS --------------

		# The variable that controls the loop
		stop = False

		# Getting the test model
		net = model_33bus()

		# Getting the initial topology
		top = create_topology(net)

		# The tabu-list
		tabu = TabuList(max_length = int(0.2 * len(net.line))) #int(20% of the number of lines)

		# Defining the fault points
		#fault = [top.get_edge_index('bus2', 'bus3')]
		#fault = [top.get_edge_index('bus5', 'bus6')]
		#fault = [top.get_edge_index('bus3', 'bus4'), top.get_edge_index('bus26', 'bus27'), top.get_edge_index('bus9', 'bus10')]
		fault = [top.get_edge_index('bus18', 'bus19'), top.get_edge_index('bus10', 'bus11')]

		# Applying the fault points
		set_faults(top, fault)

		# Voltage limit variation
		v_variation = 0.1

		# Best solution (starting with the initial solution)
		best = top.get_edge_states()

		# Number of solutions generated per iteration
		n_solutions = int(0.2 * len(net.line))

		# Iteration number (starting with 0)
		iteration = 1

		# The IT memory
		memory = [0 for _ in range(len(net.line))]

		# Stores the last iteration that improve the best solution
		improved = iteration

		# Limiar of frequence that determines if a component will stay in the solution
		# after the reset of the search by the ITM
		frequence = 0.6

		# A flag that indicates if the search was restarted once
		reset = False

		# The number of max iterations before reset the search with IT memory
		max_reset = 25

		# Maximum limit of iterations without improve the best solution found (termination criteria)
		max_i = 50

		# Maximum iterations to local search
		max_local = 20

		# Power source name
		source = net.bus['name'][int(net.ext_grid['bus'])]

		# Getting the indexes of the bridge lines between the source (bus0) and the first fork
		bridges = bridge_lines(top, source)
		# -------------------------------------------------------

		# MAIN LOOP ---------------------------------------------
		print('Starting loop...')
		print('Initial solution:', top.get_edge_states())
		# Stores the initial time
		begin = time()

		while not stop:

			# List of generated neighbors (solutions)
			neighbors = list()

			# The iteration-selected solution
			selected = top.get_edge_states()

			# Neighborhood generation ---------------------------
			print('Iteration #%d' % iteration)
			print('Generating neighbors...')
			# Getting probability vector
			pv = get_lines_probability(top, source)
			# Making `n_solutions` neihgbors
			for k in range(n_solutions):
				print('  Generating %d/%d' % (k+1, n_solutions))
				# Generating the neighbor components
				sol = list()
				for i in range(len(net.line)):
					c = selected[i]
					if c == 1:
						if draw(pv[i]):
							c = 0
					else:
						if draw(0.5):
							c = 1
					# Making solution
					sol.append(c)
				# Local search
				#print('  Performing local search...')
				local = [sol] + [swap_1_0(sol.copy()) for _ in range(max_local)]
				# Activating the bridge lines and removing fault points
				for i in range(len(local)):
					local[i] = set_value(local[i], bridges, 1)
					local[i] = set_value(local[i], fault, 0)
				#print('  Removing cycles...')
				# Removing cycles
				for i in range(len(local)):
					top.set_edge_states(local[i])
					for cycle in top.cycles(source, search = 'bfs'):
						top.deactivate_edge(top.get_edge_index(cycle[0], cycle[1]))
					local[i] = top.get_edge_states()
				#print('  Running the power flow...')
				# Voltage constraints
				for i in range(len(local)):
					top.set_edge_states(local[i])
					make_switch_operations(top.get_edge_states(), net)
					# Running powerflow
					try:
						runpp(net, algorithm='nr', numba=True)
					except:
						print('  ### ERROR: Error during the power flow. Ignoring the solution.')
						local[i] = [0 for _ in range(len(selected))]
						local[i] = set_value(local[i], bridges, 1)
					for j, voltage in enumerate(net.res_bus['vm_pu'], start=0):
						if abs(1 - voltage) >= v_variation: # out of the voltage constraints
							bus = top.get_vertex_name(j)
							for adjacent in top.get_adjacent(bus):
								top.deactivate_edge(top.get_edge_index(bus, adjacent))
					local[i] = top.get_edge_states()
				# Getting the best of local search
				neighbors.append(best_of(local, top, source))
			# ---------------------------------------------------

			# Neighbor selection --------------------------------
			print('Selecting the neighbor...')
			best_of_iteration = best_of(neighbors, top, source)
			while len(neighbors) != 0:
				selected = best_of(neighbors, top, source)
				neighbors.remove(selected)
				if tabu.is_tabu(selected):
					print('  TABU: This solution is in tabu list. Applying aspiration criteria...')
					# Aspiration criteria
					if not draw(0.3):
						print('  Result: REFUSED')
						continue
					print('  Result: ACCEPTED')
					if len(neighbors) == 0:
						print('  All solutions is in tabu list. Selecting the best found.')
						selected = best_of_iteration.copy()
						tabu.add(best_of_iteration)
						top.set_edge_states(best_of_iteration)
						break
				tabu.add(selected)
				top.set_edge_states(selected)
				print('  Solution selected.')
				break
			#print('  Comparing the selected solution with the best solution found...')
			if best != []:
				sel = best_of([selected, best], top, source)
				if sel != best:
					print(  'IMPROVEMENT: Improving solution at iteration %d' % iteration)
					best = sel.copy()
					improved = iteration
			else:
				best = selected.copy()
			# ---------------------------------------------------

			# Intermediate-term memory --------------------------
			print('Saving the solution in the intermediate-term memory...')
			for i in range(len(selected)):
				memory[i] += selected[i]
			if not reset and iteration - improved > max_reset:
				print('RESETING SEARCH -------------------')
				print(  'Reseting the search with intermediate-term memory.')
				reset = True
				mcc = list()
				for value in memory:
					if value/iteration > frequence:
						mcc.append(1)
					else:
						mcc.append(0)
				# Activating the bridge lines and removing fault points
				mcc = set_value(mcc, bridges, 1)
				mcc = set_value(mcc, fault, 0)
				# Removing cycles
				top.set_edge_states(mcc)
				for cycle in top.cycles(source, search = 'bfs'):
					top.deactivate_edge(top.get_edge_index(cycle[0], cycle[1]))
				mcc = top.get_edge_states()
				print(  'Most common components:', mcc)
				selected = mcc.copy()
				top.set_edge_states(selected)
			# ---------------------------------------------------

			# Checking termination criteria ---------------------
			print('Selected:', selected)
			#print('Best:', best)
			iteration += 1
			if iteration - improved > max_i:
				stop = True
				elapsed_time = time() - begin
				print('Elapsed time: ', elapsed_time)
				print('Best solution found: ', best)
			# ---------------------------------------------------

		# -------------------------------------------------------
		results.append({
			'time': elapsed_time,
			'best': best,
			'total_i': iteration,
			'i_best': improved,
			'fault': [(top.get_edge(e)[0], top.get_edge(e)[1]) for e in fault],
			'i_local': max_local,
			'itm': max_reset,
			'max_i': max_i,
			})

	return results