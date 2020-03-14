# R-1.6
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def sum_odd_squared(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i * i
    return sum


print(sum_odd_squared(6))
print(1*1 + 3*3 + 5*5)
