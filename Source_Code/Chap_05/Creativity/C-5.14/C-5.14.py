# C-5.14
# The shuffle method, supported by the random module, takes a Python
# list and rearranges it so that every possible ordering is equally likely.
# Implement your own version of such a function. You may rely on the
# randrange(n) function of the random module, which returns a random
# number between 0 and n−1 inclusive.

from random import randrange

def shuffle(lst):
    n = len(lst)
    for index, value in enumerate(lst):
        new_index = randrange(n)
        lst[index], lst[new_index] = lst[new_index], lst[index]
    return lst

lst = list(range(10))
print(lst)

lst = shuffle(lst)
print(lst)