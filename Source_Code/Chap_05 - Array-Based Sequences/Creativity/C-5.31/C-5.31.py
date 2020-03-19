# C-5.31
# Describe a way to use recursion to add all the numbers in an n×n data
# set, represented as a list of lists.


def sum_recursively(lst_of_lst, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return sum(lst_of_lst[start])
    else:
        mid = (start + stop) // 2
        return sum_recursively(lst_of_lst, start, mid) + sum_recursively(lst_of_lst, mid, stop)


n = 3
data_set = [[n*j + i for i in range(n)] for j in range(n)]
print(data_set)
print(sum_recursively(data_set, 0, n))
