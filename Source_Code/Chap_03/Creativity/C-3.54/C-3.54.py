# C-3.54
# A sequence S contains n integers taken from the interval [0,4n], with repetitions
# allowed. Describe an efficient algorithm for determining an integer
# value k that occurs the most often in S. What is the running time of your
# algorithm?


def get_most_repetitive(sequence):
    """Finds the most frequent integer in a sequence
       Returns the integer and it's count"""
    sequence = sorted(sequence)
    current_max = [sequence[0]]
    possible_max = []
    for index in range(1, len(sequence)):
        if sequence[index] == current_max[0]:
            current_max.append(sequence[index])
        elif len(possible_max) == 0 or sequence[index] == possible_max[0]:
            possible_max.append(sequence[index])
            if len(possible_max) > len(current_max):
                current_max = possible_max
        else:
            possible_max = [sequence[index]]
    return current_max[0], len(current_max)


my_sequence = [0, 0, 1, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
integer, occurence = get_most_repetitive(my_sequence)
print("The most frequent integer is {}, it is written {} times.".format(integer, occurence))
