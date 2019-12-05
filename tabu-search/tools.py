''' This file contains some functionalities to support the development
of the TS'''

from topology import Topology
from random import randint


def mount_topology(pp_net):
	top = Topology()
	# Creating vertices (buses)
	for bus in pp_net.bus['name']:
		top.add_vertex(bus)
	# Creating edges (lines)
	lines = list()
	for from_bus in pp_net.line['from_bus']:
		lines.append([pp_net.bus['name'][from_bus], ''])
	for i, to_bus in enumerate(pp_net.line['to_bus'], start = 0):
		lines[i][1] = pp_net.bus['name'][to_bus]
	for i, state in enumerate(pp_net.switch['closed'], start = 0):
		top.add_edge(lines[i][0], lines[i][1], state)
	return top


def make_switch_operations(topology, pp_net):
	for i, state in enumerate(topology.get_edge_states(), start=0):
		pp_net.switch['closed'][i] = bool(state)


def swap(index_a, index_b, topology):
	temp = topology.get_state_of_edge(index_a)
	topology.set_state_of_edge(index_a, topology.get_state_of_edge(index_b))
	topology.set_state_of_edge(index_b, temp)


def objective_function(topology, root):
	return len(topology.conex_vertices(root)) - 1


def best_topology(topologies):
	best = tops.pop(0)
	value = objective_function(best)
	for topology in topologies:
		v = objective_function(topology)
		if v > value:
			best = topology
			value = v
	return best
	

def swap_by_unused(topology, index_to_swap):
	choosed = randint(0, len(topology.unused_lines))
	swap(index_to_swap, choosed)


def remove_fault_points(topology, fault_points):
	for point in fault_points:
		topology[point] = 0 #int(False)
	return topology