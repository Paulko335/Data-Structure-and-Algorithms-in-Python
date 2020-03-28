# R-7.4
# Describe in detail how to swap two nodes x and y (and not just their contents)
# in a singly linked list L given references only to x and y. Repeat
# this exercise for the case when L is a doubly linked list. Which algorithm
# takes more time?

from singly_linked_list_7_4 import SinglyLinkedList
from doubly_linked_base_7_4 import _DoublyLinkedBase


####################################################################################
#                             For a Singly Linked List                             #
####################################################################################


def find_prev(SLL, current_node):
    if current_node is SLL._header:
        raise Exception("header does not have a previous node")
    prev = SLL._header
    while prev._next != current_node:
        prev = prev._next
    return prev


def get_k_th_node(SLL, k):
    """Returns the kth element of the singly linked list"""
    if k < 0 or k >= SLL.get_size():  # if k is not in the list
        raise IndexError("list index out of range")
    k_th_node = SLL._header._next
    for _ in range(k):          # cycle through the list to get the node at index k
        k_th_node = k_th_node._next
    return k_th_node


def swap_x_y_SLL(SLL, x, y):
    if x == y:
        pass
    elif x._next == y:
        xprev = find_prev(SLL, x)
        ynext = y._next

        xprev._next = y
        y._next = x
        x._next = ynext
    else:
        xprev = find_prev(SLL, x)
        xnext = x._next
        yprev = find_prev(SLL, y)
        ynext = y._next

        xprev._next = y
        y._next = xnext

        yprev._next = x
        x._next = ynext

    return SLL


SLL = SinglyLinkedList()

for i in range(3):
    SLL.add_last(i)

print("# ---------------- For a Singly Linked List ---------------- ")
print("Original SSL: {}\n".format(SLL))

for index in range(0, 3):
    x = SLL.get_head()
    y = get_k_th_node(SLL, index)
    swap_x_y_SLL(SLL, x, y)
    print("Swapped nodes {} and {}, new SLL:".format(0, y._element), SLL)
    print("\n")


####################################################################################
#                             For a Doubly Linked List                             #
####################################################################################

# I used the doubly_linked_base shown in the book
# I had to use some workarounds to limit myself with the basic method of the class
# This is why I must print in a strange way and use an external list to save the content
# It would be better to simply add and use the same methods that I added in the Singly Linked List,
# but I did not want to change de base class

def swap_x_y_DLL(DLL, x, y):
    if x == y:
        pass
    elif x._next == y:
        xprev = x._prev
        ynext = y._next

        x._next = ynext
        ynext._prev = x

        xprev._next = y
        y._prev = xprev

        y._next = x
        x._prev = y

    else:
        xprev = x._prev
        xnext = x._next
        yprev = y._prev
        ynext = y._next

        xprev._next = y
        y._prev = xprev

        y._next = xnext
        xnext._prev = y

        yprev._next = x
        x._prev = yprev

        x._next = ynext
        ynext._prev = x

    return DLL


print("# ---------------- For a Doubly Linked List ---------------- ")
DLL = _DoublyLinkedBase()

current_DLL = ["0", "1", "2", "3", "4"]
# adding [0, 1, 2, 3, 4] in DLL
for i in range(5):
    DLL._insert_between(i, DLL._trailer._prev, DLL._trailer)
print("Original DLL content: [{}]".format(", ".join(current_DLL)))


#####################
# Case where y is x #
#####################

x = DLL._header._next._next
y = x
swap_x_y_DLL(DLL, x, y)
current_DLL = []
while not DLL.is_empty():
    current_DLL.append(str(DLL._delete_node(DLL._header._next)))

print("Swapped nodes {} and {}, current DLL content:".format(1, 1), "[{}]".format(", ".join(current_DLL)))


####################################
# Case where y is directly after x #
####################################
# adding current_DLL to DLL
for i in current_DLL:
    DLL._insert_between(i, DLL._trailer._prev, DLL._trailer)

x = DLL._header._next._next
y = x._next
swap_x_y_DLL(DLL, x, y)
current_DLL = []
while not DLL.is_empty():
    current_DLL.append(str(DLL._delete_node(DLL._header._next)))

print("Swapped nodes {} and {}, current DLL content:".format(1, 2), "[{}]".format(", ".join(current_DLL)))


#########################################
# Case where y more than 1 node after x #
#########################################
# adding current_DLL to DLL
for i in current_DLL:
    DLL._insert_between(i, DLL._trailer._prev, DLL._trailer)

x = DLL._header._next._next
y = x._next._next._next
swap_x_y_DLL(DLL, x, y)
current_DLL = []
while not DLL.is_empty():
    current_DLL.append(str(DLL._delete_node(DLL._header._next)))

print("Swapped nodes {} and {}, current DLL content:".format(1, 4), "[{}]".format(", ".join(current_DLL)))
print("""
It is faster to swap a doubly linked list, because you already have the nodes before x and y.
You do not have to cycle trough the list until to find them, like with the find_prev function """)


####################################################################################
#                                Testing runtime                                  #
####################################################################################
# This section runs in a Jupyter Notebook!

# print("# ---------------- Testing runtime ------------------------- ")
#
# # SLL now contains [0, 4, 1, 3, 2]
# SLL = SinglyLinkedList()
# for i in current_DLL:
#     SLL.add_last(i)
#
# # DLL now contains [0, 4, 1, 3, 2]
# for i in current_DLL:
#     DLL._insert_between(i, DLL._trailer._prev, DLL._trailer)
#
# print("")
# print("SLL: ", SLL)
# print("DLL: ", current_DLL)
#
# print("""
# It is faster to swap a doubly linked list, because you already know what are the nodes before x and y.
# You do not have to cycle trough the list to find them, like with the find_prev function \n""")
#
#
# x = SLL.get_head()          # x is node 0
# y = get_k_th_node(SLL, 3)   # y is node 3
# print("SLL swap time: ")
# %timeit swap_x_y_SLL(SLL, x, y)
# print("")
#
# x = DLL._header._next       # x is node 0
# y = x._next._next._next     # y is node 3
# print("DLL swap time: ")
# %timeit swap_x_y_DLL(DLL, x, y)
#