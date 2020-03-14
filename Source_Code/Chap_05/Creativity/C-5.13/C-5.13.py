# C-5.13
# In the experiment of Code Fragment 5.1, we begin with an empty list. If
# data were initially constructed with nonempty length, does this affect the
# sequence of values at which the underlying array is expanded? Perform
# your own experiments, and comment on any relationship you see between
# the initial length and the expansion sequence.


import sys
for base_length in [0, 35]:
    data = [i for i in range(base_length)]
    n = 200
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

print("""
We observe that the difference between capacities remain de same.
The first sequence has the numbers 35, 46, 58, 72, ...
If we substract theses numbers by the first, we get 0, 11, 23, 37, ...
As we can see, this is exacly the second sequence!
""")
