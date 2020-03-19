# P-3.57
# Perform experimental analysis to test the hypothesis that Python’s sorted
# method runs in O(nlog n) time on average.

# It takes about a minute to compute with original inputs
# Graphic shows about a constant function with y data divided by xlog(x)

import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

xs = []                 # x axis values (number of integers : n)
avg_sorting_times = []   # y axis values (time required to sort n integers)

# measuring average sorting times
for new_int in range(100, 5000, 10):
    print(new_int)
    # statement to measure
    stmt = """
lst = sorted(lst)
"""
    # generating and shuffling the list, it is not included in measured time
    setup = """import random
lst = list(range({}))
random.shuffle(lst)""".format(new_int)

    t = timeit.Timer(stmt, setup)

    # repeat multiple times for every list length to obtain average times
    number = 30
    total_time = sum(t.repeat(number, 1)) # execute once per repeat to measure only the sorting time
    avg_time = total_time / number

    # Append x and y values
    xs.append(new_int)
    avg_sorting_times.append(avg_time/(new_int * np.log2(new_int))) #

plt.plot(xs, avg_sorting_times, label="sorted()")
plt.xlabel("List length")
plt.ylabel("Sorting time (s) divided by xlog(x)")
plt.title("Average computation time for python's\n sorted function (average of 30 runs)")

plt.show()