''' This file provides functions to support the development of
the genetic algorithm applied to the knapsac problem 0-1 '''

from random import randint, random


# Defining global variables

# The lists that stores the values and weights of the items
weights = list()
values = list()

# The vector of factors that indicate the relation value/weight for each item
factors = list()

# The max weight for the knapsac
max_weight = 49877

# Population size
pop_size = 50

# The best solution found
best = list()

# The variable that determines the end of the search
stop = False


# Defining common functions

def clear():
	weights = list()
	values = list()
	factors = list()


def read(file_name = 'items.in'):
	clear()
	file = open(file_name)
	for line in file:
		value, weight = line.split()
		value = int(value)
		weight = int(weight)
		values.append(value)
		weights.append(weight)
		factors.append(value/weight)


read('items_100.in')


def objective_function(solution):
	value = 0
	for i in range(len(solution)):
		if solution[i] == 1:
			value += values[i]
	return value


def check_weight(solution):
	weight = 0
	for i in range(len(solution)):
		if solution[i] == 1:
			weight += weights[i]
	return weight


def merge(vector_a, vector_b):
	merged = list()
	while vector_a != [] and vector_b != []:
		if objective_function(vector_a[0]) > objective_function(vector_b[0]):
			merged.append(vector_a.pop(0))
		else:
			merged.append(vector_b.pop(0))
	merged += vector_a + vector_b
	return merged


# Sort a list of individuals according to the objective function
def merge_sort(vector):
	if len(vector) in [0, 1]:
		return vector
	else:
		vector_a = merge_sort(vector[:len(vector)//2])
		vector_b = merge_sort(vector[len(vector)//2:])
		return merge(vector_a, vector_b)


# Generates the initial population
def generate_initial_population():
	pop = list()
	for _ in range(pop_size):
		pop.append([randint(0, 1) for _ in values])
	return pop

population = generate_initial_population()

# MAIN LOOP ----------------------------------
# primeira seleção: 40%
# segunda seleção: 30%
# terceira seleção: 20%
while not stop:
	stop = True
