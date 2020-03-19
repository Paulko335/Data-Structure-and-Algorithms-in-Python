# Functions studied in this exercise
# They both combine two lists
# func1 uses list comprehension
# func2 uses repeated append()


def func1(length):
    squares = [k*k for k in range(1, length+1)]
    return squares

def func2(length):
    squares = []
    for k in range(1, length+1):
        squares.append(k*k)
    return squares
