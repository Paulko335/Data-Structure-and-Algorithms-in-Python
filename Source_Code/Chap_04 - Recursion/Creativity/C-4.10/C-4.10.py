# C-4.10
# Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.


def int_log2(n):
    if n < 2:
        return 0
    else:
        return 1 + int_log2(n//2)


n = 16
print(int_log2(n))
