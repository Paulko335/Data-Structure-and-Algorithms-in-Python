# R-3.33
# Al and Bob are arguing about their algorithms. Al claims his O(nlog n)-
# time method is always faster than Bob’s O(n2)-time method. To settle the
# issue, they perform a set of experiments. To Al’s dismay, they find that if
# n < 100, the O(n2)-time algorithm runs faster, and only when n ≥ 100 is
# the O(nlog n)-time one better. Explain how this is possible.

print("""
It is possible for a O(n^2) to be faster than a O(nlog(n))
We must look at factors in both algorithms

-> n^2 < 16 * n * log(n), for n <= 108
""")
