# C-1.20
# Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.

from random import randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def randint_shuffle(numbers):
    for index in range(len(numbers)):
        new_index = randint(0, len(numbers)-1)
        numbers[index], numbers[new_index] = numbers[new_index], numbers[index]


print(numbers)
randint_shuffle(numbers)
print(numbers)
