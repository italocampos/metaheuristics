demands = [(1, 2), (2, 3), (3, 4)]

for i, demand in enumerate(demands, start = 0):
	print('%d, p = %f, q = %f' % (i, demand[0]/1e6, demand[1]/1e6))


resistances = [(0, 1, 0.0922, 0.0470), (1, 2, 0.4930, 0.2511), (2, 3, 0.3660, 0.1864), (3, 4, 0.3811, 0.1941), (4, 5, 0.8190, 0.7070), (5, 6, 0.1872, 0.6188), (6, 7, 1.7114, 1.2351), (7, 8, 1.0300, 0.7400), (8, 9, 1.0440, 0.7400), (9, 10, 0.1966, 0.0650), (10, 11, 0.3744, 0.1238), (11, 12, 1.4680, 1.1550), (12, 13, 0.5416, 0.7219), (13, 14, 0.5910, 0.5260), (14, 15, 0.7463, 0.5450), (15, 16, 1.2890, 1.7210), (16, 17, 0.7320, 0.5740), (1, 18, 0.1640, 0.1565), (18, 19, 1.5042, 1.3554), (19, 20, 0.4095, 0.4784), (20, 21, 0.7089, 0.9373), (2, 22, 0.4512, 0.3083), (22, 23, 0.8980, 0.7091), (23, 24, 0.8960, 0.7011), (5, 25, 0.2030, 0.1034), (25, 26, 0.2842, 0.1447), (26, 27, 1.0590, 0.9337), (27, 28, 0.8042, 0.7006), (28, 29, 0.5075, 0.2585), (29, 30, 0.9744, 0.9630), (30, 31, 0.3105, 0.3619), (31, 32, 0.3410, 0.5302), (7, 20, 2.0000, 2.0000), (8, 14, 2.0000, 2.0000), (11, 21, 2.0000, 2.0000), (17, 32, 0.5000, 0.5000), (24, 28, 0.5000, 0.5000)]

for i, r in enumerate(resistances, start = 1):
	nf = 210
	if r[0] >= 1:
		nf = 11
	print('%d, from = %d, to = %d, nf = %d, r = %f, x = %f, max_i = %f' % (i, r[0], r[1], nf, r[2], r[3], 0.142))