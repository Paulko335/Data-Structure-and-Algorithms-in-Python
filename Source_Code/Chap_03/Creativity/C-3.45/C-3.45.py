# C-3.45
# A sequence S contains n−1 unique integers in the range [0,n−1], that
# is, there is one number from this range that is not in S. Design an O(n)-
# time algorithm for finding that number. You are only allowed to use O(1)
# additional space besides the sequence S itself.


def find_missing_integer(sequence):
    """Returns the first missing integer from a sequence"""
    for index in range(len(sequence) - 1 ):
        diff = sequence[index + 1] - sequence[index]
        if diff != 1:
            return sequence[index] + 1
    return "No missing integer"


# Integer 2 is missing from the sequence
sequence_1= [0, 1, 3, 4]
print(find_missing_integer(sequence_1))

# Complete sequence
sequence_2= [0, 1, 2, 3]
print(find_missing_integer(sequence_2))
