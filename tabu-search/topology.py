''' This file models a graph that uses some properties
in the vertices. This class hinerits from the Graph 
class, available on https://github.com/italocampos/graphs/blob/python/adjacency_matrix/graph.py
'''

import sys

sys.path.insert(0, '../../graphs/adjacency_matrix/')

from graph import Graph

class Topology(Graph):
	def __init__(self):
		super().__init__(list(), list())
		self._edges = list()


	def add_edge(self, vertex_a, vertex_b, used = True):
		if used:
			super().add_edge(vertex_a, vertex_b)
		self._edges.append((vertex_a, vertex_b, used))


	def get_edge(self, index):
		if self._is_valid_index(index):
			return self._edges[index]


	def get_edge_index(self, vertex_a, vertex_b):
		index = 0
		for line in self._edges:
			va, vb, _ = line
			edge = [(va, vb), (vb, va)]
			if (vertex_a, vertex_b) in edge:
				return index
			index += 1


	def is_used(self, edge_index):
		return self.get_edge(edge_index)[2]


	def get_edge_states(self):
		return [int(b[2]) for b in self._edges]


	def set_edge_states(self, vector):
		if len(vector) != len(self._edges):
			raise(Exception('The given vector has a different size against the number of edges.'))
		for i, value in enumerate(vector, start=0):
			self._edges[i] = bool(value)


	def set_state_of_edge(self, edge, state):
		if self._is_valid_index(edge):
			self._edges[edge] = state


	def get_state_of_edge(self, edge):
		return self.get_edge(edge)[2]


	def unused_edges(self):
		unused = list()
		for i, edge in enumerate(self._edges, start=0):
			if not edge[2]:
				unused.append(i)
		return unused
	

	def activate_edge(self, index):
		if self._is_valid_index(index):
			super().add_edge(self.get_edge(index))
	

	def deactivate_edge(self, index):
		if self._is_valid_index(index):
			self.remove_edge(self.get_edge(index))


	def num_of_used_edges(self):
		return self._edges.count(1)

	
	def _is_valid_index(index):
		if 0 <= index < len(self._edges):
			return True
		raise(ValueError('There is no an edge related to the given index.'))