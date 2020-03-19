# C-4.12
# Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.


def product(m, n):
    if n == 0:
        total = 0
    else:
        total = m + product(m, n-1)
    return total


print(product(8, 3))
