# R-6.4
# Give a recursive method for removing all the elements from a stack


def remove_all(stack):
    if len(stack) == 0:
        return
    stack.pop()
    return remove_all(stack)
