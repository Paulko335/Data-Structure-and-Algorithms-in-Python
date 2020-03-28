# R-7.2
# Describe a good algorithm for concatenating two singly linked lists L and
# M, given only references to the first node of each list, into a single list L
# that contains all the nodes of L followed by all the nodes of M.

from singly_linked_list_7_2 import SinglyLinkedList


# This would be a class method
def concatenate_SLL(L, M):
    """Concatenate two Singly Linked List."""
    L.get_tail()._next = M.get_head()
    L._size += M._size      # Must add sizes for this particular implementation of a SLL
    return L


L = SinglyLinkedList()
M = SinglyLinkedList()

for i in range(4):
    L.add_last(i)
    M.add_last(4 + i)

print("L:", L)
print("M:", M)

print("Concatenating both lists")
LM = concatenate_SLL(L, M)
print("LM:", LM)
