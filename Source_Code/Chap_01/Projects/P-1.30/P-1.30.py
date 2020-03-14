# P-1.30
# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

from math import log


# Using loops
def count_div_by_two(number):
    cpt = 0
    while number >= 4:
        number = number / 2
        cpt += 1
    return cpt


# Using logarithms


def log_count_div_by_two(number):
    return int((log(number, 2) - 1))


test_number = 16
print(count_div_by_two(test_number))
print(log_count_div_by_two(test_number))
