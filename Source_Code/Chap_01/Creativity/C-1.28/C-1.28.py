# C-1.28
# The p-norm of a vector v = (v1,v2, . . . ,vn) in n-dimensional space is defined
# as ||v|| =p√(vp1 +vp2 +· · ·+vpn) .
# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Euclidean
# norm of a two-dimensional vector with coordinates (4,3) has a
# Euclidean norm of
# √(42+32) = √(16+9) = √(25) = 5. Give an implementation
# of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.

import math


def norm(v):
    squared_norm = sum(number * number for number in v)
    return math.sqrt(squared_norm)


def p_norm(v, p):
    p_ed_norm = sum(math.pow(number, p) for number in v)
    return math.pow(p_ed_norm, 1/p)


numbers = [3, 4]
print(norm(numbers))
print(p_norm(numbers, 2))
