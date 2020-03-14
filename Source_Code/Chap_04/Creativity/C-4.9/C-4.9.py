# C-4.9
# Write a short recursive Python function that finds the minimum and maximum
# values in a sequence without using any loops.

def find_min_max(sequence):
    minimum = sequence[0]
    maximum = sequence[0]

    if len(sequence) >= 2:
        possible_min, possible_max = find_min_max(sequence[1:])

        if possible_min < minimum:
            minimum = possible_min

        if possible_max > maximum:
            maximum = possible_max

    return minimum, maximum

sequence = [5,6,7,8,2,16,3,4]
print(find_min_max(sequence))