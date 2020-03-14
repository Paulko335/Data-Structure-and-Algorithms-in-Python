# Functions studied in this exercise
# They both combine two lists
# func1 uses the extend() method on the first list
# func2 uses repeated append()

def func1(A, B):
    A.extend(B)
    return A

def func2(A, B):
    for element in B:
        A.append(element)
    return A
