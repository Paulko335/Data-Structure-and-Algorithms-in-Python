# C-1.23
# Give an example of a Python code fragment that attempts to write an element
# to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”


def write_to_list(list):
    for index in range(len(list) + 1):
        try:
            list[index] = None
            print("I will erase all your valuable information!")
        except IndexError:
            print("Don't try buffer overflow attacks in Python!")


list = [0, 1, 2, 3]
write_to_list(list)

