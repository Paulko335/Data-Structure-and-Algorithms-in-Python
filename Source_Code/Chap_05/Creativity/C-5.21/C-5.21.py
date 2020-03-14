# C-5.21
# In Section 5.4.2, we described four different ways to compose a long
# string: (1) repeated concatenation, (2) appending to a temporary list and
# then joining, (3) using list comprehension with join, and (4) using generator
# comprehension with join. Develop an experiment to test the efficiency
# of all four of these approaches and report your findings.

# Execution takes about a minute.
# You can remove the print() in the first loop to clear the console
# Keep it to show progression
#
# Every function exhibit linear behavior, but they do not share the same constant factor
# function #3 (list comprehension) seems to be the best one,
# even though the author says the best one should be #4 (generator comprehension)


import matplotlib.pyplot as plt
import timeit

# average execution times for every length of input list (Y axis data)
func_1_avg_times = []
func_2_avg_times = []
func_3_avg_times = []
func_4_avg_times = []

# list of integer to use as functions input (X axis data)
int_lst = []

# group average times to loop over them
avg_times_lst = [func_1_avg_times,
                 func_2_avg_times,
                 func_3_avg_times,
                 func_4_avg_times]

# measures the execution time of every algorithm for a given list length
for new_int in range(5000, 100000, 5000):
    int_lst.append(new_int)    # generating an increasingly long list of int to swipe x-axis

    # Printing to show progression, you can remove this part to clear the console
    print("Computing times for a document of {} characters".format(new_int))

    for func_index, func_avg_times in enumerate(avg_times_lst, start=1):

        stmt = """func{}(document)""".format(func_index)
        setup = """from string_composition_functions import func{}
document = "A" * {} """.format(func_index, new_int)

        t = timeit.Timer(stmt, setup)

        # repeat multiple times for every list length to obtain average times
        number = 30
        total_time = sum(t.repeat(number, 1)) # execute once per repeat to measure only the function run time
        avg_time = total_time / number

        # Append y-axis values
        func_avg_times.append(avg_time) #(new_int * np.log2(new_int))) #


# plot every result
for avg_index, avg_times in enumerate(avg_times_lst, start=1):
    plt.plot(int_lst, avg_times, label="func{}".format(avg_index))

plt.xlabel("Length of input list")
plt.ylabel("Execution time (s)")
plt.title("Comparison of {} algorithms for the same task".format(len(avg_times_lst)))
plt.legend()

plt.show()
