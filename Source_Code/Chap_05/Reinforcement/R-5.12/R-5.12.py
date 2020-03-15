# R-5.12
# Describe how the built-in sum function can be combined with Python’s
# comprehension syntax to compute the sum of all numbers in an n×n data
# set, represented as a list of lists.

n = 3
my_list = [[n*j + i for i in range(3)] for j in range(3)]
print(my_list)

total = sum([sum(line) for line in my_list])
print(total)
