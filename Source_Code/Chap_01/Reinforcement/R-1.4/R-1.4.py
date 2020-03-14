# R-1.4
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.


def sum_int_squared(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


print(sum_int_squared(4))
print(1*1 + 2*2 + 3*3)
