# C-6.18
# Show how to use the transfer function, described in Exercise R-6.3, and
# two temporary stacks, to replace the contents of a given stack S with those
# same elements, but in reversed order.


# transfer function from Exercise R-6.3
def transfer(S, T):
    """Transfer all elements from stack S onto stack T in reversed order"""
    while len(S) > 0:
        T.push(S.pop())
    return T

# S = Stack([0, 1, 2, 3])    # S contains [0, 1, 2, 3]
# Temp1 = Stack()
# Temp2 = Stack()
#
# transfer(S, Temp1)         # Temp1 contains [3, 2, 1, 0]
# transfer(Temps, Temps2)    # Temp2 contains [0, 1, 2, 3]
# transfer(Temps, S)         # S contains [3, 2, 1, 0]
