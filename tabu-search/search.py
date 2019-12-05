''' This file implements the Tabu Search to the modeled problem.
'''

from tl import TabuList
from models import model33bus
from tools import *

# General variables definition

# The variable that controls the loop
stop = False

# Getting the test model and its respective topology
net = model33bus()
top = mount_topology(net)

# The tabu-list
tabu = TabuList(length = int(0.2 * len(net.line))) #int(20% of the number of lines)

# Defining the fault points
fault = [top.get_edge_index('bus9', 'bus10')]


# Generating the initial solution

while not stop:
    # Neighborhood generation

    # Neighbor selection

    # Intermediate-term memory

    # Checking termination criteria