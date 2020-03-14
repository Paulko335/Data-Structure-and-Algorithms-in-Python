# R-5.8
# Experimentally evaluate the efficiency of the pop method of Python’s list
# class when using varying indices as a parameter, as we did for insert on
# page 205. Report your results akin to Table 5.5.

import timeit

Ns = []

# creating result lists
k_0 = []
k_equal_n_over_2 = []
k_equal_n = []
running_times = [k_0, k_equal_n_over_2, k_equal_n]

min_N_magnitude = 2
max_N_magnitude = 6

ks = ["0", "n//2", "-1"]

# Verifying runtime
for index, running_time in enumerate(running_times):
    for new_int in range(min_N_magnitude, max_N_magnitude):
        n = 10**new_int
        Ns.append(n)

        j = n//10   # testing the method on n//10 elements


        stmt = """
for i in range({}):
    lst.pop({})""".format(j, ks[index])

        setup = """n = {}
lst = [i for i in range(n)]""".format(n)

        t = timeit.Timer(stmt, setup=setup)

        number = 10  # number of repetition to obtain average result
        total_time = sum(t.repeat(number, 1))
        avg_time = total_time / (number*j)  # divide by number and by j to obtain average time for a single pop()

        running_time.append(avg_time)

print("""\n
Average runtime of using pop() method on n/10 element of lists of length n
Lines test for varying positions for the index k, pop(k) for k = 0, n//2, n
Rows test for varying lengths of the list, going from {} to {} by factors of 10\n""".format(min_N_magnitude, max_N_magnitude))

[print(i) for i in running_times]

print("""\n
It is clear that using pop() at the end of the list is O(1), 
but using it at the beginning or in the middle is O(n)""")
