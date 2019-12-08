''' This file implements the Tabu Search to the modeled problem.
'''

from tl import TabuList
from models import model33bus
from tools import *
from random import random
from pandapower import runpp

# DEFINING GLOBAL VARIABLES AND PARAMETERS --------------

# The variable that controls the loop
stop = False

# Getting the test model
net = model33bus()

# Getting the initial topology
top = create_topology(net)

# The tabu-list
tabu = TabuList(length = int(0.2 * len(net.line))) #int(20% of the number of lines)

# Defining the fault points
fault = [top.get_edge_index('bus9', 'bus10')]

# Applying the fault points
top = set_faults(top, fault)

# Voltage limit variation
v_variation = 0.1

# Best solution (starting with the initial solution)
best = top.get_edge_states()

# Number of solutions generated per iteration
n_solutions = 5

# Iteration number
iteration = 0

# Maximum limit of iterations without improve the best solution found
max_i = 50

# Maximum iterations to local search
max_local = 10

# Power source name
source = net.bus['name'][int(net.ext_grid['bus'])]

# Getting bridge lines between the source (bus0) and the first fork
bridges = bridge_lines(top, source)

# -------------------------------------------------------

# MAIN LOOP ---------------------------------------------
while not stop:

	# List of generated neighbors (solutions)
	neighbors = list()

	# The iteration-selected solution
	selected = top.get_edge_states()

	# Neighborhood generation ---------------------------
	# Getting probability vector
	pv = get_lines_probability(top, source)
	# Making `n_solutions` neihgbors
	for _ in range(n_solutions):
		# Generating the neighbor components
		sol = list()
		for i in range(len(net.line)):
			c = selected[i]
			if c == 1:
				if not draw(pv[i]):
					c = 0
			else:
				if draw(0.5):
					c = 1
			# Making solution
			sol.append(c)
		# Local search
		local = [sol] + [swap_1_0(sol.copy()) for _ in range(max_local)]
		# Activating the bridge lines
		for i in range(len(local)):
			local[i] = set_value(local[i], bridges, 1)
		# Removing cycles
		for i in range(len(local)):
			top.set_edge_states(local[i])
			for cycle in top.cycles(source, search = 'bfs'):
				top.deactivate_edge(top.get_edge_index(cycle[0], cycle[1]))
			local[i] = top.get_edge_states()
		# Voltage constraints
		for i in range(len(local)):
			top.set_edge_states(local[i])
			n = make_switch_operations(top.get_edge_states(), net)
			# Running powerflow
			runpp(n)
			for i, voltage in enumerate(n.res_bus['vm_pu'], start=0):
				if abs(1 - voltage) >= v_variation: # out of the voltage constraints
					bus = top.get_vertex_name(i)
					for adjacent in top.get_adjacent(bus):
						top.deactivate_edge(top.get_edge_index(bus, adjacent))
			local[i] = top.get_edge_states()
		# Getting the best of local search
		neighbors.append(best_of(local, top, source))
	# ---------------------------------------------------

	# Neighbor selection --------------------------------
	# It doesn't work
	while True:
		temp = best_of(neighbors, top, source)
		neighbors.remove(temp)
		if tabu.is_tabu(temp):
			# Aspiration criteria
			if random() < 0.3:
				selected = temp
				break
			else:
				continue
		else:
			selected = temp
			break



	# Intermediate-term memory

	# Checking termination criteria

# -------------------------------------------------------