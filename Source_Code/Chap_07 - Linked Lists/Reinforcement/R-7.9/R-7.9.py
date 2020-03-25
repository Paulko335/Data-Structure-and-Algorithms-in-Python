# R-7.9
# Give a fast algorithm for concatenating two doubly linked lists L and M,
# with header and trailer sentinel nodes, into a single list LM.

from doubly_linked_base_7_9 import _DoublyLinkedBase
from exceptions_7_9 import Empty


def DLL_append_M_to_L(L, M):
    """Concatenate both lists by adding M to the end of L"""
    L_tail = L._trailer._prev   # keeping reference for the tail of L
    M_head = M._header._next    # keeping reference for the head of M

    L_tail._next = M_head       # tying the tail of L with the head of M
    M_head._prev = L_tail

    L._trailer = M._trailer     # the new trailer of L is the trailer of M
    L._size += M._size          # must add sizes for this implementation of a DLL

    return L


L = _DoublyLinkedBase()
M = _DoublyLinkedBase()

# adding [0, 1] to L
for i in range(2):
    L._insert_between(i, L._trailer._prev, L._trailer)


# adding [2, 3] to M
for i in range(2, 4):
    M._insert_between(i, M._trailer._prev, M._trailer)


LM = DLL_append_M_to_L(L, M)

# LM now contains [0, 1, 2, 3]
while not LM.is_empty():
    print(LM._delete_node(LM._header._next))
