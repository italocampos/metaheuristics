''' This file models a graph that uses some properties
in the vertices.
'''

import os

os.sys.path.insert(0, 'libs')


from graph import Graph

class Topology(Graph):
	def __init__(self):
		super().__init__(list(), list())
		self._edges = list()


	def add_edge(self, vertex_a, vertex_b, used = True):
		super().add_edge(vertex_a, vertex_b)
		self._edges.append((vertex_a, vertex_b, used))


	def get_edge(self, index):
		if 0 <= index < len(self._edges):
			return self._edges[index]
		raise(Exception('There is no an edge related to the given index.'))


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


	def get_lines_vector(self):
		return [int(b[2]) for b in self._edges]