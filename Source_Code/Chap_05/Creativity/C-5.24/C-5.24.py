# C-5.24
# Perform experiments to evaluate the efficiency of the remove method of
# Python’s list class, as we did for insert on page 205. Use known values so
# that all removals occur either at the beginning, middle, or end of the list.
# Report your results akin to Table 5.5.

import timeit

Ns = []

# creating result lists
k_0 = []
k_equal_n_over_2 = []
k_equal_n = []
running_times = [k_0, k_equal_n_over_2, k_equal_n]

min_N_magnitude = 2
max_N_magnitude = 5

# testing on 10% of elements, at different positions
ks = [["0", "n//10"], ["5*n//10", "6*n//10"], ["9*n//10", "n"]]

# Verifying runtime
for index, running_time in enumerate(running_times):
    for new_int in range(min_N_magnitude, max_N_magnitude):
        n = 10**new_int
        Ns.append(n)

        j = n//10   # testing the method on n//10 elements

        stmt = """
for i in range({}, {}):
    lst.remove(i)""".format(j, ks[index][0], ks[index][1])

        setup = """n = {}
lst = [i for i in range(n)]""".format(n)

        t = timeit.Timer(stmt, setup=setup)

        number = 10  # number of repetition to obtain average result
        total_time = sum(t.repeat(number, 1))
        avg_time = total_time / (number*j)  # divide by number and by j to obtain average time for a single pop()

        running_time.append(avg_time)

print("""\n
Average runtime of using remove() method on n/10 element of lists of length n
Lines test for varying positions for the index k, pop(k) for k = 0, n//2, n
Rows test for varying lengths of the list, going from {} to {} by factors of 10\n""".format(min_N_magnitude, max_N_magnitude))

[print(i) for i in running_times]

print("""\n
It is clear that using remove() at the end of the list is O(1), 
but using it at the beginning or in the middle is O(n)""")
