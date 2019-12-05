''' This file implements the Tabu Search to the modeled problem.
'''

from tl import TabuList
from models import model33bus
from tools import *

# DEFINING GLOBAL VARIABLES AND PARAMETERS ---------

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
# Best solution
best = remove_fault_points(top.get_edge_states(), fault)

# Number of solutions
n_solutions = 5

# List of generated solutions
solutions = list()

# Iteration number
iteration = 0

# Maximum limit of non-improved solution
max_i = 50

# Maximum iterations to local search
max_local = 6

# --------------------------------------------------


while not stop:
    # Neighborhood generation

    # Neighbor selection

    # Intermediate-term memory

    # Checking termination criteria