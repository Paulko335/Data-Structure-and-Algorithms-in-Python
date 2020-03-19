# R-1.7
# Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.

number = 6
print(sum(i*i for i in range(number) if i%2 != 0))
