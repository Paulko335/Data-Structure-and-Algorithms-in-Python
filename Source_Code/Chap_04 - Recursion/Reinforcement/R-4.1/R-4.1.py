# R-4.1
# Describe a recursive algorithm for finding the maximum element in a sequence,
# S, of n elements. What is your running time and space usage?

# Running time is O(n log(n))
# Space usage is O(log(n))

import random


def get_max_recursively(sequence):
    if len(sequence) == 1:
        return sequence[0]

    else:
        mid = len(sequence) // 2
        high = get_max_recursively(sequence[:mid])
        low = get_max_recursively(sequence[mid:])
        if low > high:
            high = low
        return high


sequence = list(range(100))
random.shuffle(sequence)

if max(sequence) == get_max_recursively(sequence):
    print(True)


# -> It prints True