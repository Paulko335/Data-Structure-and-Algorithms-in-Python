# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def minmax(data):
    min = data[0]
    max = data[0]

    for number in data:
        if number > max:
            max = number
        if number < min:
            min = number

    return (min, max)


data = [1, 5, 2, 7, 3, 8, 4, 9]
print(minmax(data))
