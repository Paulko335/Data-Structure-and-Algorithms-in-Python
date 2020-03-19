# P-5.32
# Write a Python function that takes two three-dimensional numeric data
# sets and adds them componentwise.


def sum_3d_numeric_data(A, B):
    """ Sums two three-dimensional numeric data sets componentwise
        Data A and B must be of same dimensions"""
    dim_A = [len(A), len(A[0]), len(A[0][0])]
    C = [[[A[i][j][k] + B[i][j][k] for k in range(dim_A[2])] for j in range(dim_A[1])] for i in range(dim_A[0])]
    return C


def print_3d_data(data):
    print("")
    [[print(data[i][j]) for j in range(len(data))] for i in range(len(data[0][0]))]
    print("")


a = b = c = 3  # matrix dimensions
A = [[[i*a*b + j*b + k for k in range(c)] for j in range(b)] for i in range(a)]
print_3d_data(A)

B = A
print_3d_data(B)

C = sum_3d_numeric_data(A, B)
print_3d_data(C)
