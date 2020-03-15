# R-6.5
# Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.

from array_stack_6_5 import ArrayStack

def reverse(lst):
    S = ArrayStack()
    for element in lst:
        S.push(element)
    for index in range(len(lst)):
        lst[index] = S.pop()
    return lst

a_list = [0, 1, 2, 3]
print(a_list)
print(reverse(a_list))
