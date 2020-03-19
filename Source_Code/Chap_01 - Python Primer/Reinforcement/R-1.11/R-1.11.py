# R-1.11
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

powers_of_two = [pow(2, i) for i in range(9)]
print(powers_of_two)