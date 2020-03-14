# C-4.11
# Describe an efficient recursive function for solving the element uniqueness
# problem, which runs in time that is at most O(n2) in the worst case
# without using sorting.

def unique(sequence):
    if len(sequence) <= 1:
        return True
    else:
        first = sequence[0]
        first_is_unique = True
        if first in sequence[1:]:
            first_is_unique = False
    return first_is_unique and unique(sequence[1:])

sequence_1 = [6, 7, 8, 9]
print(unique(sequence_1))

sequence_2 = [6, 7, 8, 9, 9]
print(unique(sequence_2))