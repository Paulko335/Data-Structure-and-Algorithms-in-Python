# R-7.11
# Implement a function, with calling syntax max(L), that returns the maximum
# element from a PositionalList instance L containing comparable
# elements.

from positional_list_7_11 import PositionalList
from exceptions_7_11 import Empty


def positional_list_max(L):
    if L.first() is None:
        raise Empty("Empty list does not have a max")

    max_value = L.first().element()       # initialise max as the first element
    for element in L:
        if element > max_value:    # if a bigger element is found, max is this new one
            max_value = element
    return max_value



my_list = PositionalList()

# adding [0, 1, 2, 3] to the list
for i in range(4):
    my_list.add_last(i)

print("The maximum of the list is: {}".format(positional_list_max(my_list)))
