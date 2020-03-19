# R-3.23-27
# Give a big-Oh characterization, in terms of n, of the running time of the
# example(1, 2, 3, 4, 5) function shown in Code Fragment 3.10.

# total += S[j] is executed j times, where j = n
#                        -> n
#                        -> O(n)


def example1(S):
    """Return the sum of the elements in sequence S."""
    n = len(S)
    total = 0
    for j in range(n):  # loop from 0 to n-1
        total += S[j]
    return total


# total += S[j] is executed j times, where j = n/2
#                        -> n/2
#                        -> O(n)
def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S)
    total = 0
    for j in range(0, n, 2):  # note the increment of 2
        total += S[j]
    return total


# total += S[j] is executed j * k times, where k = 1 + j
#                        -> j * (1 + j) = j^2 + 1 and j = n
#                        -> n^2 + n
#                        -> O(n^2)
def example3(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    total = 0
    for j in range(n):  # loop from 0 to n-1
        for k in range(1 + j):  # loop from 0 to j
            total += S[k]
    return total


# += is executed twice for each j, where j = n
#                          -> 2*n
#                             O(n)
def example4(S):
    """Return the sum of the prefix sums of sequence S."""
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total


# i is executed n times
# j is executed n times for every i
# k is executed j + 1 times for every j
# B[i] == total is O(n) because it is true at most n times
#
# -> i * (j * (k))
# -> n * (n(n+1)/2 + n)
# -> n * (n(n+3)/2)
# -> n^2 * (n+3)/2
# -> O(n^2)
#
def example5(A, B):  # assume that A and B have equal length
    """Return the number of elements in B equal to the sum of prefix sums in A."""
    n = len(A)
    count = 0
    for i in range(n):  # loop from 0 to n-1
        total = 0
        for j in range(n):  # loop from 0 to n-1
            for k in range(1 + j):  # loop from 0 to j
                total += A[k]
        if B[i] == total:
            count += 1
    return count
