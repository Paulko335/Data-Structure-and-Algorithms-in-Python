# C-5.22
# Develop an experiment to compare the relative efficiency of the extend
# method of Python’s list class versus using repeated calls to append to
# accomplish the equivalent task.

import matplotlib.pyplot as plt
import timeit

# average execution times for every length of input list (Y axis data)
func_1_avg_times = []
func_2_avg_times = []

# list of integer to use as functions input (X axis data)
int_lst = []

# group average times to loop over them
avg_times_lst = [func_1_avg_times,
                 func_2_avg_times]

# measures the execution time of every algorithm for a given list length
for new_int in range(100, 20000, 500):
    int_lst.append(new_int)     # generating an increasingly long list of int to swipe x-axis

    # Printing to show progression, you can remove this part to clear the console
    print("Computing times for two lists of {} characters".format(new_int))

    for func_index, func_avg_times in enumerate(avg_times_lst, start=1):

        stmt = """func{}(A, B)""".format(func_index)
        setup = """from list_merging_functions import func{}
A = ["A"] * {}
B = ["B"] * {}""".format(func_index, new_int, new_int)

        t = timeit.Timer(stmt, setup)

        # repeat multiple times for every list length to obtain average times
        number = 30
        total_time = sum(t.repeat(number, 1))   # execute once per repeat to measure only the function run time
        avg_time = total_time / number

        # Append y-axis values
        func_avg_times.append(avg_time)

# function labels
labels = ["extend()", "append()"]

# plot every result
for avg_index, avg_times in enumerate(avg_times_lst):
    plt.plot(int_lst, avg_times, label=labels[avg_index])

plt.xlabel("Length of input lists")
plt.ylabel("Execution time (s)")
plt.title("Comparison of {} algorithms for the same task".format(len(avg_times_lst)))
plt.legend()

plt.show()
