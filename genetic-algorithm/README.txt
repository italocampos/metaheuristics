To run the method, run

>> from ga import *
>> run(times = 1)

The run() method runs the method for `times` times and return a list with the results. The dictionaries is under this form:

{'best': list(), # the best found solution
'iterations': int, # The taken number of iterations
'time': float} # The taken time
