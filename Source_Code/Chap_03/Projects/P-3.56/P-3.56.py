# P-3.56
# Perform an experimental analysis that compares the relative running times
# of the functions shown in Code Fragment 3.10.

import matplotlib.pyplot as plt
import timeit

# average execution times for every length of input list (Y axis data)
func_1_avg_times = []
func_2_avg_times = []
func_3_avg_times = []
func_4_avg_times = []
func_5_avg_times = []

# list of integer to use as functions input (X axis data)
int_lst = []

# group average times to loop over them
avg_times_lst = [func_1_avg_times,
                 func_2_avg_times,
                 func_3_avg_times,
                 func_4_avg_times,
                 func_5_avg_times]

# measures the execution time of every algorithm for a given list length
for new_int in range(0, 100, 1):
  int_lst.append(new_int)    # generating an increasingly long list of int to swipe x-axis

  for func_index, func_avg_times in enumerate(avg_times_lst, start=1):
    if func_index != 5:
      time = timeit.timeit("""total = example{}({})""".format(func_index, int_lst),
                          setup="""from exercises import example{}""".format(func_index),
                          number=10)
    else:
      time = timeit.timeit("""total = example{}({}, {})""".format(func_index, int_lst, int_lst),
                             setup="""from exercises import example{}""".format(func_index),
                             number=10)

    func_avg_times.append(time)    # add execution time of its respective algorithm to the list of execution times

# plot every result
for avg_index, avg_times in enumerate(avg_times_lst, start=1):
  plt.plot(int_lst, avg_times, label="prefix_average{}".format(avg_index))

plt.xlabel("Length of input list")
plt.ylabel("Execution time (s)")
plt.title("Comparison of {} algorithms for different tasks\n on a log-log scale".format(len(avg_times_lst)))
plt.xscale("log", basex=2)
plt.yscale("log", basey=2)
plt.legend()

plt.show()
