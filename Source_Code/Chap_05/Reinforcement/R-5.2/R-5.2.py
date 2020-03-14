# R-5.2
# In Code Fragment 5.1, we perform an experiment to compare the length of
# a Python list to its underlying memory usage. Determining the sequence
# of array sizes requires a manual inspection of the output of that program.
# Redesign the experiment so that the program outputs only those values of
# k at which the existing capacity is exhausted. For example, on a system
# consistent with the results of Code Fragment 5.2, your program should
# output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . .

import sys
data = []
n = 27
old_size = sys.getsizeof(data)
array_capacities = []
for k in range(n):
    length = len(data)
    new_size = sys.getsizeof(data)
    if new_size != old_size:
        array_capacities.append(str(k-1)) # Capacity was exhausted one iteration ago
        old_size = new_size
    data.append(None)

print("The sequence of array capacities are {},...".format(", ".join(array_capacities)))
