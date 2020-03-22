# R-7.6
# Suppose that x and y are references to nodes of circularly linked lists,
# although not necessarily the same list. Describe a fast algorithm for telling
# if x and y belong to the same list.


def are_linked(x, y):
    """Returns True is both nodes are in the same list"""
    if x == y:
        return True

    walk_y = y._next
    while walk_y != y:    # walk until a full loop is completed
        if walk_y == x:
            return True
        walk_y = walk_y._next
    return False
