# C-1.13
# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

a_list = [0, 1, 2, 3]


def reversed_list(list):
    n = len(list)
    reversed = []
    for i in range(n):
        reversed.append(list[-(i+1)])
    return reversed


print(reversed_list(a_list))
