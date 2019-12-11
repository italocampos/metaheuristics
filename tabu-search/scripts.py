'''demands = [(1, 2), (2, 3), (3, 4)]

for i, demand in enumerate(demands, start = 0):
	print('%d, p = %f, q = %f' % (i, demand[0]/1e6, demand[1]/1e6))


resistances = [(0, 1, 0.0922, 0.0470), (1, 2, 0.4930, 0.2511), (2, 3, 0.3660, 0.1864), (3, 4, 0.3811, 0.1941), (4, 5, 0.8190, 0.7070), (5, 6, 0.1872, 0.6188), (6, 7, 1.7114, 1.2351), (7, 8, 1.0300, 0.7400), (8, 9, 1.0440, 0.7400), (9, 10, 0.1966, 0.0650), (10, 11, 0.3744, 0.1238), (11, 12, 1.4680, 1.1550), (12, 13, 0.5416, 0.7219), (13, 14, 0.5910, 0.5260), (14, 15, 0.7463, 0.5450), (15, 16, 1.2890, 1.7210), (16, 17, 0.7320, 0.5740), (1, 18, 0.1640, 0.1565), (18, 19, 1.5042, 1.3554), (19, 20, 0.4095, 0.4784), (20, 21, 0.7089, 0.9373), (2, 22, 0.4512, 0.3083), (22, 23, 0.8980, 0.7091), (23, 24, 0.8960, 0.7011), (5, 25, 0.2030, 0.1034), (25, 26, 0.2842, 0.1447), (26, 27, 1.0590, 0.9337), (27, 28, 0.8042, 0.7006), (28, 29, 0.5075, 0.2585), (29, 30, 0.9744, 0.9630), (30, 31, 0.3105, 0.3619), (31, 32, 0.3410, 0.5302), (7, 20, 2.0000, 2.0000), (8, 14, 2.0000, 2.0000), (11, 21, 2.0000, 2.0000), (17, 32, 0.5000, 0.5000), (24, 28, 0.5000, 0.5000)]

for i, r in enumerate(resistances, start = 1):
	nf = 210
	if r[0] >= 1:
		nf = 11
	print('%d, from = %d, to = %d, nf = %d, r = %f, x = %f, max_i = %f' % (i, r[0], r[1], nf, r[2], r[3], 0.142))'''

# Data
r1 = [{'i_local': 20, 'itm': 25, 'i_best': 2, 'time': 138.87268090248108, 'max_i': 50, 'best': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], 'total_i': 53, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 3, 'time': 138.5038070678711, 'max_i': 50, 'best': [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'total_i': 54, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 2, 'time': 136.3384985923767, 'max_i': 50, 'best': [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], 'total_i': 53, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 57, 'time': 281.1920394897461, 'max_i': 50, 'best': [1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1], 'total_i': 108, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 1, 'time': 133.8977756500244, 'max_i': 50, 'best': [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], 'total_i': 52, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 6, 'time': 146.13149046897888, 'max_i': 50, 'best': [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0], 'total_i': 57, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 3, 'time': 139.1329743862152, 'max_i': 50, 'best': [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0], 'total_i': 54, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 1, 'time': 133.81144881248474, 'max_i': 50, 'best': [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1], 'total_i': 52, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 5, 'time': 142.94385743141174, 'max_i': 50, 'best': [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'total_i': 56, 'fault': [('bus2', 'bus3')]}, {'i_local': 20, 'itm': 25, 'i_best': 2, 'time': 135.05856704711914, 'max_i': 50, 'best': [1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0], 'total_i': 53, 'fault': [('bus2', 'bus3')]}]

r2 = [{'time': 138.3657259941101, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 53, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 'i_best': 2, 'max_i': 50}, {'time': 132.48741626739502, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 52, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1], 'i_best': 1, 'max_i': 50}, {'time': 176.78175735473633, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 69, 'best': [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1], 'i_best': 18, 'max_i': 50}, {'time': 133.50490283966064, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 52, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1], 'i_best': 1, 'max_i': 50}, {'time': 135.89297890663147, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 53, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1], 'i_best': 2, 'max_i': 50}, {'time': 133.7201371192932, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 52, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1], 'i_best': 1, 'max_i': 50}, {'time': 134.22477912902832, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 52, 'best': [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0], 'i_best': 1, 'max_i': 50}, {'time': 244.11482954025269, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 94, 'best': [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1], 'i_best': 43, 'max_i': 50}, {'time': 271.0405731201172, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 104, 'best': [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1], 'i_best': 53, 'max_i': 50}, {'time': 157.70485830307007, 'fault': [('bus5', 'bus6')], 'itm': 25, 'i_local': 20, 'total_i': 61, 'best': [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'i_best': 10, 'max_i': 50}]

r3 = [{'max_i': 50, 'itm': 25, 'time': 155.51798582077026, 'best': [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 'i_local': 20, 'total_i': 59, 'i_best': 8, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 133.60762238502502, 'best': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 133.8426308631897, 'best': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 138.6525330543518, 'best': [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1], 'i_local': 20, 'total_i': 54, 'i_best': 3, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 143.4328248500824, 'best': [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1], 'i_local': 20, 'total_i': 56, 'i_best': 5, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 134.31947588920593, 'best': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 134.41843795776367, 'best': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 133.25437331199646, 'best': [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 133.3831286430359, 'best': [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'i_local': 20, 'total_i': 52, 'i_best': 1, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}, {'max_i': 50, 'itm': 25, 'time': 138.60339426994324, 'best': [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1], 'i_local': 20, 'total_i': 54, 'i_best': 3, 'fault': [('bus3', 'bus4'), ('bus26', 'bus27'), ('bus9', 'bus10')]}]

r4 = [{'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0], 'time': 140.5637867450714, 'i_local': 20, 'i_best': 2, 'total_i': 53, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1], 'time': 161.51574063301086, 'i_local': 20, 'i_best': 10, 'total_i': 61, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0], 'time': 142.53263759613037, 'i_local': 20, 'i_best': 4, 'total_i': 55, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], 'time': 166.5883948802948, 'i_local': 20, 'i_best': 13, 'total_i': 64, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1], 'time': 134.06549382209778, 'i_local': 20, 'i_best': 1, 'total_i': 52, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1], 'time': 133.900381565094, 'i_local': 20, 'i_best': 1, 'total_i': 52, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], 'time': 135.5028624534607, 'i_local': 20, 'i_best': 1, 'total_i': 52, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1], 'time': 145.05652117729187, 'i_local': 20, 'i_best': 5, 'total_i': 56, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 'time': 186.78692173957825, 'i_local': 20, 'i_best': 21, 'total_i': 72, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}, {'max_i': 50, 'best': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'time': 137.46450066566467, 'i_local': 20, 'i_best': 2, 'total_i': 53, 'itm': 25, 'fault': [('bus18', 'bus19'), ('bus10', 'bus11')]}]

r5 = [{'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 175.6660349369049, 'total_i': 67, 'i_local': 20, 'max_i': 50, 'i_best': 16, 'itm': 25, 'best': [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 243.1615707874298, 'total_i': 94, 'i_local': 20, 'max_i': 50, 'i_best': 43, 'itm': 25, 'best': [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 191.16433906555176, 'total_i': 74, 'i_local': 20, 'max_i': 50, 'i_best': 23, 'itm': 25, 'best': [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 141.76913452148438, 'total_i': 55, 'i_local': 20, 'max_i': 50, 'i_best': 4, 'itm': 25, 'best': [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 153.69966888427734, 'total_i': 60, 'i_local': 20, 'max_i': 50, 'i_best': 9, 'itm': 25, 'best': [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 199.7515003681183, 'total_i': 77, 'i_local': 20, 'max_i': 50, 'i_best': 26, 'itm': 25, 'best': [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 230.680114030838, 'total_i': 89, 'i_local': 20, 'max_i': 50, 'i_best': 38, 'itm': 25, 'best': [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 151.62364506721497, 'total_i': 59, 'i_local': 20, 'max_i': 50, 'i_best': 8, 'itm': 25, 'best': [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 165.41831851005554, 'total_i': 64, 'i_local': 20, 'max_i': 50, 'i_best': 13, 'itm': 25, 'best': [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]}, {'fault': [('bus4', 'bus5'), ('bus8', 'bus9'), ('bus20', 'bus21'), ('bus15', 'bus16')], 'time': 139.15335273742676, 'total_i': 54, 'i_local': 20, 'max_i': 50, 'i_best': 3, 'itm': 25, 'best': [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]}]

results = [r1, r2, r3, r4, r5]


# Analyzing the results

from tools import *
from models import model_33bus

source = 'bus0'
top = create_topology(model_33bus())

# Best solution found
def select_best(results):
	res = results.copy()
	initial = res.pop(0)
	top.set_edge_states(initial['best'])
	value = objective_function(top, source)
	index = 0
	for i, r in enumerate(res, start=1):
		top.set_edge_states(r['best'])
		v = objective_function(top, source)
		if v > value:
			value = v
			index = i
	return index, value


def show_all(results):
	for i, r in enumerate(results):
		top.set_edge_states(r['best'])
		print('%d: %d' % (i, objective_function(top, source)))