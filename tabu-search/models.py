''' This file contains the network test models used in the TS modeling. '''

import pandapower as pp

def model_33bus():
	# Create empty net
	net = pp.create_empty_network()

	# Create buses
	bus0 = pp.create_bus(net, name = 'bus0', vn_kv = 12, type = 'b')
	bus1 = pp.create_bus(net, name = 'bus1', vn_kv = 12, type = 'b')
	bus2 = pp.create_bus(net, name = 'bus2', vn_kv = 12, type = 'b')
	bus3 = pp.create_bus(net, name = 'bus3', vn_kv = 12, type = 'b')
	bus4 = pp.create_bus(net, name = 'bus4', vn_kv = 12, type = 'b')
	bus5 = pp.create_bus(net, name = 'bus5', vn_kv = 12, type = 'b')
	bus6 = pp.create_bus(net, name = 'bus6', vn_kv = 12, type = 'b')
	bus7 = pp.create_bus(net, name = 'bus7', vn_kv = 12, type = 'b')
	bus8 = pp.create_bus(net, name = 'bus8', vn_kv = 12, type = 'b')
	bus9 = pp.create_bus(net, name = 'bus9', vn_kv = 12, type = 'b')
	bus10 = pp.create_bus(net, name = 'bus10', vn_kv = 12, type = 'b')
	bus11 = pp.create_bus(net, name = 'bus11', vn_kv = 12, type = 'b')
	bus12 = pp.create_bus(net, name = 'bus12', vn_kv = 12, type = 'b')
	bus13 = pp.create_bus(net, name = 'bus13', vn_kv = 12, type = 'b')
	bus14 = pp.create_bus(net, name = 'bus14', vn_kv = 12, type = 'b')
	bus15 = pp.create_bus(net, name = 'bus15', vn_kv = 12, type = 'b')
	bus16 = pp.create_bus(net, name = 'bus16', vn_kv = 12, type = 'b')
	bus17 = pp.create_bus(net, name = 'bus17', vn_kv = 12, type = 'b')
	bus18 = pp.create_bus(net, name = 'bus18', vn_kv = 12, type = 'b')
	bus19 = pp.create_bus(net, name = 'bus19', vn_kv = 12, type = 'b')
	bus20 = pp.create_bus(net, name = 'bus20', vn_kv = 12, type = 'b')
	bus21 = pp.create_bus(net, name = 'bus21', vn_kv = 12, type = 'b')
	bus22 = pp.create_bus(net, name = 'bus22', vn_kv = 12, type = 'b')
	bus23 = pp.create_bus(net, name = 'bus23', vn_kv = 12, type = 'b')
	bus24 = pp.create_bus(net, name = 'bus24', vn_kv = 12, type = 'b')
	bus25 = pp.create_bus(net, name = 'bus25', vn_kv = 12, type = 'b')
	bus26 = pp.create_bus(net, name = 'bus26', vn_kv = 12, type = 'b')
	bus27 = pp.create_bus(net, name = 'bus27', vn_kv = 12, type = 'b')
	bus28 = pp.create_bus(net, name = 'bus28', vn_kv = 12, type = 'b')
	bus29 = pp.create_bus(net, name = 'bus29', vn_kv = 12, type = 'b')
	bus30 = pp.create_bus(net, name = 'bus30', vn_kv = 12, type = 'b')
	bus31 = pp.create_bus(net, name = 'bus31', vn_kv = 12, type = 'b')
	bus32 = pp.create_bus(net, name = 'bus32', vn_kv = 12, type = 'b')

	# Create the loads
	pp.create_ext_grid(net, bus=bus0, vm_pu=1, name="source")
	#load0 = pp.create_load(net, bus0, p_mw = 0.000000, q_mvar = 0.000000, name = 'load0')
	load1 = pp.create_load(net, bus1, p_mw = 0.100000, q_mvar = 0.060000, name = 'load1')
	load2 = pp.create_load(net, bus2, p_mw = 0.090000, q_mvar = 0.040000, name = 'load2')
	load3 = pp.create_load(net, bus3, p_mw = 0.120000, q_mvar = 0.080000, name = 'load3')
	load4 = pp.create_load(net, bus4, p_mw = 0.060000, q_mvar = 0.030000, name = 'load4')
	load5 = pp.create_load(net, bus5, p_mw = 0.060000, q_mvar = 0.020000, name = 'load5')
	load6 = pp.create_load(net, bus6, p_mw = 0.200000, q_mvar = 0.100000, name = 'load6')
	load7 = pp.create_load(net, bus7, p_mw = 0.200000, q_mvar = 0.100000, name = 'load7')
	load8 = pp.create_load(net, bus8, p_mw = 0.060000, q_mvar = 0.020000, name = 'load8')
	load9 = pp.create_load(net, bus9, p_mw = 0.060000, q_mvar = 0.020000, name = 'load9')
	load10 = pp.create_load(net, bus10, p_mw = 0.045000, q_mvar = 0.030000, name = 'load10')
	load11 = pp.create_load(net, bus11, p_mw = 0.060000, q_mvar = 0.035000, name = 'load11')
	load12 = pp.create_load(net, bus12, p_mw = 0.060000, q_mvar = 0.035000, name = 'load12')
	load13 = pp.create_load(net, bus13, p_mw = 0.120000, q_mvar = 0.080000, name = 'load13')
	load14 = pp.create_load(net, bus14, p_mw = 0.060000, q_mvar = 0.010000, name = 'load14')
	load15 = pp.create_load(net, bus15, p_mw = 0.060000, q_mvar = 0.020000, name = 'load15')
	load16 = pp.create_load(net, bus16, p_mw = 0.060000, q_mvar = 0.020000, name = 'load16')
	load17 = pp.create_load(net, bus17, p_mw = 0.090000, q_mvar = 0.040000, name = 'load17')
	load18 = pp.create_load(net, bus18, p_mw = 0.090000, q_mvar = 0.040000, name = 'load18')
	load19 = pp.create_load(net, bus19, p_mw = 0.090000, q_mvar = 0.040000, name = 'load19')
	load20 = pp.create_load(net, bus20, p_mw = 0.090000, q_mvar = 0.040000, name = 'load20')
	load21 = pp.create_load(net, bus21, p_mw = 0.090000, q_mvar = 0.040000, name = 'load21')
	load22 = pp.create_load(net, bus22, p_mw = 0.090000, q_mvar = 0.050000, name = 'load22')
	load23 = pp.create_load(net, bus23, p_mw = 0.420000, q_mvar = 0.200000, name = 'load23')
	load24 = pp.create_load(net, bus24, p_mw = 0.420000, q_mvar = 0.200000, name = 'load24')
	load25 = pp.create_load(net, bus25, p_mw = 0.060000, q_mvar = 0.025000, name = 'load25')
	load26 = pp.create_load(net, bus26, p_mw = 0.060000, q_mvar = 0.025000, name = 'load26')
	load27 = pp.create_load(net, bus27, p_mw = 0.060000, q_mvar = 0.020000, name = 'load27')
	load28 = pp.create_load(net, bus28, p_mw = 0.120000, q_mvar = 0.070000, name = 'load28')
	load29 = pp.create_load(net, bus29, p_mw = 0.200000, q_mvar = 0.600000, name = 'load29')
	load30 = pp.create_load(net, bus30, p_mw = 0.150000, q_mvar = 0.070000, name = 'load30')
	load31 = pp.create_load(net, bus31, p_mw = 0.210000, q_mvar = 0.100000, name = 'load31')
	load32 = pp.create_load(net, bus32, p_mw = 0.060000, q_mvar = 0.040000, name = 'load32')


	# Create types of lines with respective values of resistance
	dl1 = {'c_nf_per_km': 210, 'r_ohm_per_km': 0.092200, 'x_ohm_per_km': 0.047000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl1, 'line1', element='line')
	dl2 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.493000, 'x_ohm_per_km': 0.251100, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl2, 'line2', element='line')
	dl3 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.366000, 'x_ohm_per_km': 0.186400, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl3, 'line3', element='line')
	dl4 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.381100, 'x_ohm_per_km': 0.194100, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl4, 'line4', element='line')
	dl5 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.819000, 'x_ohm_per_km': 0.707000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl5, 'line5', element='line')
	dl6 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.187200, 'x_ohm_per_km': 0.618800, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl6, 'line6', element='line')
	dl7 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.711400, 'x_ohm_per_km': 1.235100, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl7, 'line7', element='line')
	dl8 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.030000, 'x_ohm_per_km': 0.740000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl8, 'line8', element='line')
	dl9 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.044000, 'x_ohm_per_km': 0.740000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl9, 'line9', element='line')
	dl10 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.196600, 'x_ohm_per_km': 0.065000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl10, 'line10', element='line')
	dl11 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.374400, 'x_ohm_per_km': 0.123800, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl11, 'line11', element='line')
	dl12 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.468000, 'x_ohm_per_km': 1.155000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl12, 'line12', element='line')
	dl13 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.541600, 'x_ohm_per_km': 0.721900, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl13, 'line13', element='line')
	dl14 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.591000, 'x_ohm_per_km': 0.526000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl14, 'line14', element='line')
	dl15 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.746300, 'x_ohm_per_km': 0.545000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl15, 'line15', element='line')
	dl16 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.289000, 'x_ohm_per_km': 1.721000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl16, 'line16', element='line')
	dl17 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.732000, 'x_ohm_per_km': 0.574000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl17, 'line17', element='line')
	dl18 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.164000, 'x_ohm_per_km': 0.156500, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl18, 'line18', element='line')
	dl19 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.504200, 'x_ohm_per_km': 1.355400, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl19, 'line19', element='line')
	dl20 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.409500, 'x_ohm_per_km': 0.478400, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl20, 'line20', element='line')
	dl21 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.708900, 'x_ohm_per_km': 0.937300, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl21, 'line21', element='line')
	dl22 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.451200, 'x_ohm_per_km': 0.308300, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl22, 'line22', element='line')
	dl23 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.898000, 'x_ohm_per_km': 0.709100, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl23, 'line23', element='line')
	dl24 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.896000, 'x_ohm_per_km': 0.701100, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl24, 'line24', element='line')
	dl25 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.203000, 'x_ohm_per_km': 0.103400, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl25, 'line25', element='line')
	dl26 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.284200, 'x_ohm_per_km': 0.144700, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl26, 'line26', element='line')
	dl27 = {'c_nf_per_km': 11, 'r_ohm_per_km': 1.059000, 'x_ohm_per_km': 0.933700, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl27, 'line27', element='line')
	dl28 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.804200, 'x_ohm_per_km': 0.700600, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl28, 'line28', element='line')
	dl29 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.507500, 'x_ohm_per_km': 0.258500, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl29, 'line29', element='line')
	dl30 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.974400, 'x_ohm_per_km': 0.963000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl30, 'line30', element='line')
	dl31 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.310500, 'x_ohm_per_km': 0.361900, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl31, 'line31', element='line')
	dl32 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.341000, 'x_ohm_per_km': 0.530200, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl32, 'line32', element='line')
	dl33 = {'c_nf_per_km': 11, 'r_ohm_per_km': 2.000000, 'x_ohm_per_km': 2.000000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl33, 'line33', element='line')
	dl34 = {'c_nf_per_km': 11, 'r_ohm_per_km': 2.000000, 'x_ohm_per_km': 2.000000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl34, 'line34', element='line')
	dl35 = {'c_nf_per_km': 11, 'r_ohm_per_km': 2.000000, 'x_ohm_per_km': 2.000000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl35, 'line35', element='line')
	dl36 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.500000, 'x_ohm_per_km': 0.500000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl36, 'line36', element='line')
	dl37 = {'c_nf_per_km': 11, 'r_ohm_per_km': 0.500000, 'x_ohm_per_km': 0.500000, 'max_i_ka': 0.426, 'type': 'cs', 'q_mm2': 50, 'alpha': 4.03e-3}
	pp.create_std_type(net, dl37, 'line37', element='line')

	# Create branch elements
	line1 = pp.create_line(net, from_bus=bus0, to_bus=bus1, length_km=1.0, std_type='line1', name='line1')
	line2 = pp.create_line(net, from_bus=bus1, to_bus=bus2, length_km=1.0, std_type='line2', name='line2')
	line3 = pp.create_line(net, from_bus=bus2, to_bus=bus3, length_km=1.0, std_type='line3', name='line3')
	line4 = pp.create_line(net, from_bus=bus3, to_bus=bus4, length_km=1.0, std_type='line4', name='line4')
	line5 = pp.create_line(net, from_bus=bus4, to_bus=bus5, length_km=1.0, std_type='line5', name='line5')
	line6 = pp.create_line(net, from_bus=bus5, to_bus=bus6, length_km=1.0, std_type='line6', name='line6')
	line7 = pp.create_line(net, from_bus=bus6, to_bus=bus7, length_km=1.0, std_type='line7', name='line7')
	line8 = pp.create_line(net, from_bus=bus7, to_bus=bus8, length_km=1.0, std_type='line8', name='line8')
	line9 = pp.create_line(net, from_bus=bus8, to_bus=bus9, length_km=1.0, std_type='line9', name='line9')
	line10 = pp.create_line(net, from_bus=bus9, to_bus=bus10, length_km=1.0, std_type='line10', name='line10')
	line11 = pp.create_line(net, from_bus=bus10, to_bus=bus11, length_km=1.0, std_type='line11', name='line11')
	line12 = pp.create_line(net, from_bus=bus11, to_bus=bus12, length_km=1.0, std_type='line12', name='line12')
	line13 = pp.create_line(net, from_bus=bus12, to_bus=bus13, length_km=1.0, std_type='line13', name='line13')
	line14 = pp.create_line(net, from_bus=bus13, to_bus=bus14, length_km=1.0, std_type='line14', name='line14')
	line15 = pp.create_line(net, from_bus=bus14, to_bus=bus15, length_km=1.0, std_type='line15', name='line15')
	line16 = pp.create_line(net, from_bus=bus15, to_bus=bus16, length_km=1.0, std_type='line16', name='line16')
	line17 = pp.create_line(net, from_bus=bus16, to_bus=bus17, length_km=1.0, std_type='line17', name='line17')
	line18 = pp.create_line(net, from_bus=bus1, to_bus=bus18, length_km=1.0, std_type='line18', name='line18')
	line19 = pp.create_line(net, from_bus=bus18, to_bus=bus19, length_km=1.0, std_type='line19', name='line19')
	line20 = pp.create_line(net, from_bus=bus19, to_bus=bus20, length_km=1.0, std_type='line20', name='line20')
	line21 = pp.create_line(net, from_bus=bus20, to_bus=bus21, length_km=1.0, std_type='line21', name='line21')
	line22 = pp.create_line(net, from_bus=bus2, to_bus=bus22, length_km=1.0, std_type='line22', name='line22')
	line23 = pp.create_line(net, from_bus=bus22, to_bus=bus23, length_km=1.0, std_type='line23', name='line23')
	line24 = pp.create_line(net, from_bus=bus23, to_bus=bus24, length_km=1.0, std_type='line24', name='line24')
	line25 = pp.create_line(net, from_bus=bus5, to_bus=bus25, length_km=1.0, std_type='line25', name='line25')
	line26 = pp.create_line(net, from_bus=bus25, to_bus=bus26, length_km=1.0, std_type='line26', name='line26')
	line27 = pp.create_line(net, from_bus=bus26, to_bus=bus27, length_km=1.0, std_type='line27', name='line27')
	line28 = pp.create_line(net, from_bus=bus27, to_bus=bus28, length_km=1.0, std_type='line28', name='line28')
	line29 = pp.create_line(net, from_bus=bus28, to_bus=bus29, length_km=1.0, std_type='line29', name='line29')
	line30 = pp.create_line(net, from_bus=bus29, to_bus=bus30, length_km=1.0, std_type='line30', name='line30')
	line31 = pp.create_line(net, from_bus=bus30, to_bus=bus31, length_km=1.0, std_type='line31', name='line31')
	line32 = pp.create_line(net, from_bus=bus31, to_bus=bus32, length_km=1.0, std_type='line32', name='line32')
	line33 = pp.create_line(net, from_bus=bus7, to_bus=bus20, length_km=1.0, std_type='line33', name='line33')
	line34 = pp.create_line(net, from_bus=bus8, to_bus=bus14, length_km=1.0, std_type='line34', name='line34')
	line35 = pp.create_line(net, from_bus=bus11, to_bus=bus21, length_km=1.0, std_type='line35', name='line35')
	line36 = pp.create_line(net, from_bus=bus17, to_bus=bus32, length_km=1.0, std_type='line36', name='line36')
	line37 = pp.create_line(net, from_bus=bus24, to_bus=bus28, length_km=1.0, std_type='line37', name='line37')

	# Create switches in 'to' buses
	pp.create_switch(net, bus=bus1, element=line1, et="l", closed=True, name='sw1')
	pp.create_switch(net, bus=bus2, element=line2, et="l", closed=True, name='sw2')
	pp.create_switch(net, bus=bus3, element=line3, et="l", closed=True, name='sw3')
	pp.create_switch(net, bus=bus4, element=line4, et="l", closed=True, name='sw4')
	pp.create_switch(net, bus=bus5, element=line5, et="l", closed=True, name='sw5')
	pp.create_switch(net, bus=bus6, element=line6, et="l", closed=True, name='sw6')
	pp.create_switch(net, bus=bus7, element=line7, et="l", closed=True, name='sw7')
	pp.create_switch(net, bus=bus8, element=line8, et="l", closed=True, name='sw8')
	pp.create_switch(net, bus=bus9, element=line9, et="l", closed=True, name='sw9')
	pp.create_switch(net, bus=bus10, element=line10, et="l", closed=True, name='sw10')
	pp.create_switch(net, bus=bus11, element=line11, et="l", closed=True, name='sw11')
	pp.create_switch(net, bus=bus12, element=line12, et="l", closed=True, name='sw12')
	pp.create_switch(net, bus=bus13, element=line13, et="l", closed=True, name='sw13')
	pp.create_switch(net, bus=bus14, element=line14, et="l", closed=True, name='sw14')
	pp.create_switch(net, bus=bus15, element=line15, et="l", closed=True, name='sw15')
	pp.create_switch(net, bus=bus16, element=line16, et="l", closed=True, name='sw16')
	pp.create_switch(net, bus=bus17, element=line17, et="l", closed=True, name='sw17')
	pp.create_switch(net, bus=bus18, element=line18, et="l", closed=True, name='sw18')
	pp.create_switch(net, bus=bus19, element=line19, et="l", closed=True, name='sw19')
	pp.create_switch(net, bus=bus20, element=line20, et="l", closed=True, name='sw20')
	pp.create_switch(net, bus=bus21, element=line21, et="l", closed=True, name='sw21')
	pp.create_switch(net, bus=bus22, element=line22, et="l", closed=True, name='sw22')
	pp.create_switch(net, bus=bus23, element=line23, et="l", closed=True, name='sw23')
	pp.create_switch(net, bus=bus24, element=line24, et="l", closed=True, name='sw24')
	pp.create_switch(net, bus=bus25, element=line25, et="l", closed=True, name='sw25')
	pp.create_switch(net, bus=bus26, element=line26, et="l", closed=True, name='sw26')
	pp.create_switch(net, bus=bus27, element=line27, et="l", closed=True, name='sw27')
	pp.create_switch(net, bus=bus28, element=line28, et="l", closed=True, name='sw28')
	pp.create_switch(net, bus=bus29, element=line29, et="l", closed=True, name='sw29')
	pp.create_switch(net, bus=bus30, element=line30, et="l", closed=True, name='sw30')
	pp.create_switch(net, bus=bus31, element=line31, et="l", closed=True, name='sw31')
	pp.create_switch(net, bus=bus32, element=line32, et="l", closed=True, name='sw32')
	pp.create_switch(net, bus=bus20, element=line33, et="l", closed=False, name='sw33')
	pp.create_switch(net, bus=bus14, element=line34, et="l", closed=False, name='sw34')
	pp.create_switch(net, bus=bus21, element=line35, et="l", closed=False, name='sw35')
	pp.create_switch(net, bus=bus32, element=line36, et="l", closed=False, name='sw36')
	pp.create_switch(net, bus=bus28, element=line37, et="l", closed=False, name='sw37')

	return net