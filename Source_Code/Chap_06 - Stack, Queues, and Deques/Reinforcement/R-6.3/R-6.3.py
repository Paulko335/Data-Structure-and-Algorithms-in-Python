# R-6.3
# Implement a function with signature transfer(S, T) that transfers all elements
# from stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.


def transfer(S, T):
    """Transfer all elements from stack S onto stack T in reversed order"""
    while len(S) > 0:
        T.push(S.pop())
    return T
