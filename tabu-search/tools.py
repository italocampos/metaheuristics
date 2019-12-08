''' This file contains some functionalities to support the development
of the TS'''

from topology import Topology
from random import randint, random


def create_topology(pp_net):
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


def make_switch_operations(line_vector, pp_net):
	for i, value in enumerate(line_vector, start=0):
		pp_net.switch['closed'][i] = bool(value)


def swap(index_a, index_b, line_vector):
	lv = line_vector.copy()
	lv[index_a], lv[index_b] = lv[index_b], lv[index_a]
	return lv


def objective_function(topology, root):
	return len(topology.conex_vertices(root)) - 1


def best_of(solutions, topology, source):
	best = solutions.pop(0)
	topology.set_edge_states(solutions.pop(0))
	value = objective_function(topology, source)
	for s in solutions:
		topology.set_edge_states(s)
		v = objective_function(topology, source)
		if v > value:
			best = s
			value = v
	return best
	

def get_used_indexes(line_vector):
	used = list()
	for i, item in enumerate(line_vector, start=0):
		if item == 1:
			used.append(i)
	return used


def get_unused_indexes(line_vector):
	unused = list()
	for i, item in enumerate(line_vector, start=0):
		if item == 0:
			unused.append(i)
	return unused


def swap_1_0(line_vector):
	used = get_used_indexes(line_vector)
	a = used[randint(0, len(used)-1)]
	unused = get_unused_indexes(line_vector)
	b = unused[randint(0, len(unused)-1)]
	return swap(a, b, line_vector)


def set_value(line_vector, indexes, value):
	if value not in [0, 1]:
		raise(Exception('Invalid value to set in a solution'))
	for index in indexes:
		line_vector[index] = value
	return line_vector


def set_faults(topology, fault_points):
	for fault in fault_points:
		topology.deactivate_edge(fault)
	return topology


def bridge_lines(topology, root):
	bridges = list()
	adjacent = topology.get_adjacent(root)
	while len(adjacent) == 1:
		bridges.append((root, adjacent[0]))
		predecessor = root
		root = adjacent[0]
		adjacent = list()
		for adj in topology.get_adjacent(root):
			if adj != predecessor:
				adjacent.append(adj)
	return bridges


def get_lines_probability(topology, source):
	probabilities = list()
	heights = topology.breadth_first_search(source)
	tree_h = topology.height(source)
	for i in range(len(topology.get_edge_states())):
		va, vb, state = topology.get_edge(i)
		ha = heights[topology.get_vertex_index(va)][1]
		hb = heights[topology.get_vertex_index(vb)][1]
		p = 0.7 if max(ha, hb)/tree_h > 0.7 else max(ha, hb)/tree_h
		probabilities.append(p)
	return probabilities


def draw(probability = 0.5):
	return random() <= probability