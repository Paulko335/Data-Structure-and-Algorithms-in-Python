# R-4.7
# Describe a recursive function for converting a string of digits into the integer
# it represents. For example, 13531 represents the integer 13,531.


def str_to_int(string):
    total = 0
    if len(string) == 1:
        total = int(string)
    else:
        magnitude = len(string) - 1
        total = int(string[0])*10**magnitude + str_to_int(string[1:])
    return total


string = "123456"
print(str_to_int(string))