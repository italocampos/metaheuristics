''' This file provides functions to support the development of
the genetic algorithm applied to the knapsac problem 0-1 '''

from random import randint, random
from time import time


# Defining global variables

# The lists that stores the values and weights of the items
weights = list()
values = list()

# The factors vector that indicate the relation value/weight for each item
factors = list()

# The max weight for the knapsac
max_weight = 49877
#max_weight = 30000

# Population size
pop_size = 50
#pop_size = 10

# The best solution found
#best = list()

# The variable that determines the end of the search
#stop = False

# Stores the actual iteration
#iteration = 1

# Stores the last iteration that improved the solution
#last_i = iteration

# Defines the maximum iteration
max_i = 200

# The maximum iteration without improve the found solution
max_ii = 100

# Mutation rate
m_rate = 0.03

# Peak of mutation rate
pm_rate = 0.07

# Limit to increase the mutation rate
m_rate_limit = 10


# Defining common functions

# Reads the file with intance data
def read(file_name = 'items.in'):
	file = open(file_name)
	for line in file:
		value, weight = line.split()
		value = int(value)
		weight = int(weight)
		values.append(value)
		weights.append(weight)
		factors.append(value/weight)


#read('items_1000.in')
read()

# The masks used into crossover
# Generates a crossing mask based on factors vector
mask_1 = [1 if e >= 1 else 0 for e in factors]

# Generates a crossing mask with 1 cut-point
mask_2 = [1 if i <= int(len(values)/2) else 0 for i in range(len(values) - 1)]

# Generates a crossing mask with 2 cut-point
mask_3 = [1 if int(1/3 * len(values)) <= i <= int(2/3 * len(values)) else 0 for i in range(len(values) - 1)]


# Generates a randomic crossing mask
def random_mask(factor = 0.5):
	mask = [0 for _ in range(len(values))]
	for _ in range(int(factor * len(values))):
		mask[randint(0, len(values) - 1)] = 1
	return mask

masks = [mask_1, mask_2, mask_3, random_mask]


# Returns the value of given `solution` into the objective funcition
def objective_function(solution):
	value = 0
	for i in range(len(solution)):
		if solution[i] == 1:
			value += values[i]
	return value


# Returns the total weight for the given `solution`
def check_weight(solution):
	weight = 0
	for i in range(len(solution)):
		if solution[i] == 1:
			weight += weights[i]
	return weight


# Returns the sum of the calculated factor for the given `solution`
def check_factor(solution):
	factor = 0
	for i in range(len(solution)):
		if solution[i] == 1:
			factor += factors[i]
	return factor


# Merge two vectors using the values of solutions into the objective function
def merge_of(vector_a, vector_b):
	merged = list()
	while vector_a != [] and vector_b != []:
		if objective_function(vector_a[0]) > objective_function(vector_b[0]):
			merged.append(vector_a.pop(0))
		else:
			merged.append(vector_b.pop(0))
	merged += vector_a + vector_b
	return merged


# Merge two vectors using the values of solutions based on the factor vector
def merge_factor(vector_a, vector_b):
	merged = list()
	while vector_a != [] and vector_b != []:
		if check_factor(vector_a[0]) > check_factor(vector_b[0]):
			merged.append(vector_a.pop(0))
		else:
			merged.append(vector_b.pop(0))
	merged += vector_a + vector_b
	return merged


# Sort a list of individuals according to passed mode
def merge_sort(vector, mode = 'of'):
	if len(vector) in [0, 1]:
		return vector
	else:
		vector_a = merge_sort(vector[:len(vector)//2], mode)
		vector_b = merge_sort(vector[len(vector)//2:], mode)
		if mode == 'of':
			return merge_of(vector_a, vector_b)
		elif mode == 'factor':
			return merge_factor(vector_a, vector_b)


# Brings a solution to feasibility
def fix(solution):
	items = []
	for i, e in enumerate(solution):
		if e == 1:
			items.append(i)
	while check_weight(solution) > max_weight:
		solution[items.pop(randint(0, len(items) - 1))] = 0


# Checks if a solution is feasible. Case no, fixes it
def validate(solution):
	if check_weight(solution) > max_weight:
		fix(solution)
	return solution


# Generates the initial population
def generate_initial_population(size = pop_size):
	pop = list()
	for _ in range(size):
		pop.append(validate([randint(0, 1) for _ in values]))
	return pop


# Makes the crossing
def cross(sol1, sol2, mask):
	s1 = sol1.copy()
	s2 = sol2.copy()
	for i in range(len(mask)):
		if mask[i] == 1:
			s1[i], s2[i] = s2[i], s1[i]
	return [s1, s2]


# Ramdomly, selects a crossing mask
def draw_mask():
	r = randint(0, len(masks) - 1)
	if r == len(masks) - 1:
		return masks[r]()
	else:
		return masks[r]


def mutation(solution, rate):
	for i in range(len(solution)):
		if random() < rate:
			solution[i] = int(not bool(solution[i]))


def run(times = 1):
	results = list()
	
	for k in range(times):
		begin = time()

		print('RUNING %d' % (k + 1))

		# Initiating local parameters
		best = list()
		stop = False
		iteration = 0
		last_i = iteration
		population = generate_initial_population()

		# MAIN LOOP ----------------------------------
		while not stop:
			print('Iteration #%d' % iteration)
			# SELECTION ------------------------------
			# Method: Tournament
			# 1st selection: 40% randomly
			selected_i = list()
			selection_1 = list()
			while len(selection_1) < int(0.4 * pop_size):
				index = randint(0, pop_size - 1)
				if index not in selected_i:
					selected_i.append(index)
					selection_1.append(population[index])
			# 2nd selection: 30% based on factor indexes
			selection_1 = merge_sort(selection_1, mode = 'factor')
			selection_2 = [selection_1[i] for i in range(int(0.3 * pop_size))]
			# 3rd selection: 20% based on value in objective function
			selection_2 = merge_sort(selection_2, mode = 'of')
			selection = [selection_2[i] for i in range(int(0.2 * pop_size))]
			# Checking if the best found solution was improved
			if objective_function(selection[0]) > objective_function(best):
				best = selection[0].copy()
				last_i = iteration
				print('  Solution improved at %d: %d' % (iteration, objective_function(best)))
			# ----------------------------------------

			# CROSSOVER ------------------------------
			# Method: Masks
			population = list()
			# Step 1: Uses the best to gererate 20% of the new population
			# Each crossing generates 2 individuals, so, the value 0.1 is used
			for _ in range(int(0.1 * pop_size)):
				population += cross(selection[0], selection[randint(1, len(selection) - 1)], draw_mask())
			# Step 2: Crosses the individuals pair to pair
			for j, i in enumerate(range(len(selection) - 1), start = 1):
				population += cross(selection[i], selection[j], draw_mask())
			# Step 3: Makes crosses ramdomly until fulfill the new generation
			while len(population) < pop_size:
				i = randint(0, len(selection) - 1)
				j = randint(0, len(selection) - 1)
				while i == j:
					j = randint(0, len(selection) - 1)
				population += cross(selection[i], selection[j], draw_mask())
			# ----------------------------------------

			# MUTATION -------------------------------
			r = m_rate
			# Check the mutation rate
			if iteration - last_i >= m_rate_limit:
				r = pm_rate
			# Make mutations
			for _ in range(int(0.5 * pop_size)):
				mutation(population[randint(0, len(population) - 1)], r)
			# ----------------------------------------

			# Validating the generated individuals
			for i in range(len(population)):
				validate(population[i])
			

			# TERMINATION CRITERIA -------------------
			if iteration - last_i >= max_ii or iteration >= max_i: #or objective_function(best) == max_weight:
				stop = True
			# ----------------------------------------

			iteration += 1

		print('Best solution found: %d.' % (objective_function(best)))

		results.append({'best': best, 'iterations': iteration - 1, 'time': time() - begin})

	return results