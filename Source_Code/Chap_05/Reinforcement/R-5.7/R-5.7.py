# R-5.7
# Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive,
# with exactly one repeated. Describe a fast algorithm for finding the
# integer in A that is repeated.

# This algorithm runs in O(n log(n) + n) = O(n log(n))


def find_repeated(A):
    dict = {i:0 for i in range(len(A))}
    print(dict)
    for value in A:
        dict[value] += 1
        if dict[value] == 2:
            return value
    return None


A = [1, 3, 3, 4, 5]
print(find_repeated(A))
