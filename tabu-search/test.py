from tools import *
from models import model_33bus
from pandapower import runpp

net = model_33bus()
top = create_topology(net)

# Defining the fault points
fault = [top.get_edge_index('bus9', 'bus10')]

# Applying the fault points
set_faults(top, fault)