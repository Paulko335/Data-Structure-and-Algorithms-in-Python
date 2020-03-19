# C-3.36
# Describe an efficient algorithm for finding the ten largest elements in a
# sequence of size n. What is the running time of your algorithm?


def find_ten_largest(A):
    A = sorted(A)
    return A[-10:]


print(find_ten_largest(range(20)))
