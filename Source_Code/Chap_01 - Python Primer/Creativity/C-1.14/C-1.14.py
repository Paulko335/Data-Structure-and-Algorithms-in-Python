# C-1.14
# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

integers = [2, 3, 3, 5]

def find_pair_odd_product(numbers):
    second_index = 0
    for first in numbers:
        second_index += 1
        for second in numbers[second_index:]:
            if first != second:
                if (first * second) % 2 == 1:
                    return True
    return False


print(find_pair_odd_product(integers))


# A faster method using sets
def odd_pair_sets(numbers):
    odd_set = {i for i in numbers if i % 2 == 1}
    return len(odd_set) >= 2


print(odd_pair_sets(integers))
