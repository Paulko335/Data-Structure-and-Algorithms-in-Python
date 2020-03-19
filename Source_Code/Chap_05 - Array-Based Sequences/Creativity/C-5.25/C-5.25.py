# C-5.25
# The syntax data.remove(value) for Python list data removes only the first
# occurrence of element value from the list. Give an implementation of a
# function, with signature remove all(data, value), that removes all occurrences
# of value from the given list, such that the worst-case running time
# of the function is O(n) on a list with n elements. Not that it is not efficient
# enough in general to rely on repeated calls to remove.


def remove_all(data, value):
    cleaned_data = [data[i] for i in range(len(data)) if data[i] != value]
    return cleaned_data


lst = [0, 1, 2, 2, 2, 3, 4]
print(lst)
print(remove_all(lst, 2))
