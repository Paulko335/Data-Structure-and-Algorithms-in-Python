# R-5.11
# Use standard control structures to compute the sum of all numbers in an
# n×n data set, represented as a list of lists.

def sum_list_of_list(lst):
    total = 0
    for line in lst:
        for element in line:
            total += element
    return total

n = 3
my_list = [[n*j + i  for i in range(3)] for j in range(3)]
print(my_list)
print(sum_list_of_list(my_list))