''' This file contains some functionalities to support the development
of the TS'''

import os

os.sys.path.insert(0, 'libs')


from topology import Topology


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