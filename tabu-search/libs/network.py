'''This class models a network test model using an incidence matrix. The network 
lines are modeled as the matrix lines whereas the buses are modeled as the matrix
columns.'''

class TestModel:

	def __init__(self, model_name = ''):
		self.buses = list()
		self.line_states = list()
		self.matrix = list()
		self.name = model_name


	def bus_exists(self, bus):
		for b in self.buses:
			if bus == b:
				return True
		return False


	def add_bus(self, bus_name):
		if not self.bus_exists(bus_name):
			for line in self.matrix:
				line.append(0);
			self.buses.append(bus_name)
		else:
			raise(NameError('The bus %s already exists.' % bus_name))


	def add_buses(self, buses_names):
		for bus in buses_names:
			self.add_bus(bus)


	def add_line(self, bus_a, bus_b, closed = True):
		new_line = list()
		for _ in self.buses:
			new_line.append(0)
		self.matrix.append(new_line)
		self.line_states.append(closed)
		self.matrix[-1][self.get_bus_id(bus_a)] = 1
		self.matrix[-1][self.get_bus_id(bus_b)] = 1


	def get_bus_id(bus_name):
		index = 0
		for bus in self.buses:
			if bus == bus_name:
				return index
			index += 1
		raise(Exception("The bus %s doesn't exists." % bus_name))


	def get_bus_name(self, bus_id):
		if 0 <= bus_id < len(self.buses):
			return self.buses[bus_id]
		else:
			raise(Exception("The bus[%d] doesn't exists." % bus_id))


	def is_closed(self, line):
		if 0 <= line < len(self.line_states):
			return self.line_states[line]
		else:
			raise(Exception("The line[%d] doesn't exists." % line_id))


	def open(self, line):
		if 0 <= line < len(self.line_states):
			self.line_states[line] = False
		else:
			raise(Exception("The line[%d] doesn't exists." % line_id))

	
	def close(self, line):
		if 0 <= line < len(self.line_states):
			self.line_states[line] = True
		else:
			raise(Exception("The line[%d] doesn't exists." % line_id))


	def get_line_states(self):
		return [int(state) for state in self.line_states]

	
	def get_closed_lines(self):
		index = 0
		closed_lines = list()
		for line in self.line_states:
			if line:
				closed_lines.append(index)
			index += 1
		return closed_lines
	

	def get_open_lines(self):
		index = 0
		closed_lines = list()
		for line in self.line_states:
			if not line:
				closed_lines.append(index)
			index += 1
		return closed_lines


	def get_buses(self):
		return self.buses

# Continuar daqui
	def vertex_degree(self, line):
		degree = 0
		for number in self.matrix[self.get_vertex_position(line)]:
			degree += number
		return degree


	def get_adjacent_indexes(self, line):
		adjacent = list()
		index = 0
		for bus in self.matrix[self.get_vertex_position(line)]:
			if bus == 1:
				adjacent.append(index)
			index += 1
		return adjacent


	def get_adjacent(self, line):
		adjacent = list()
		index = 0
		for bus in self.matrix[self.get_vertex_position(line)]:
			if bus == 1:
				adjacent.append(self.buses[index])
			index += 1
		return adjacent


	def is_adjacent_to(self, line, vertices_list):
		for bus in vertices_list:
			if not self.edge_exists(bus, line):
				return False
		return True


	def clear(self):
		self.buses = list()
		self.matrix = list()


	# Read a adjacency matrix of a graph from a file
	def read_from_file(self, file_name):
		self.clear()
		file = open(file_name, 'r')
		for bus_name in file.readline().splitlines()[0].split('\t'):
			self.add_bus(bus_name)
			#print(bus_name)
		i = 0
		for line in file:
			j = 0
			for number in line.split('\t'):
				#print('(%d, %d): %s' % (i, j, number))
				self.set_edge(i, j, int(number))
				j += 1
			i += 1
		file.close()


	def __str__(self):
		#string = '   '
		string = '\t'
		for bus_name in self.buses:
			#string += bus_name + '   '
			string += bus_name + '\t'
		string += '\n'
		index = 0
		for line in self.matrix:
			#string += self.buses[index] + '  '
			string += self.buses[index] + '\t'
			for number in line:
				#string += str(number) + '   '
				string += str(number) + '\t'
			string += '\n'
			index += 1
		return string