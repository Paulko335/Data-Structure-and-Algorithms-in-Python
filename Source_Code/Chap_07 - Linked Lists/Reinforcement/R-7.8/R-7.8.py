# R-7.8
# Describe a nonrecursive method for finding, by link hopping, the middle
# node of a doubly linked list with header and trailer sentinels. In the case
# of an even number of nodes, report the node slightly left of center as the
# “middle.” (Note: This method must only use link hopping; it cannot use a
# counter.) What is the running time of this method?

# The runtime of this method is O(n), because we walk across half the list
# from both ends. -> O(n/2) + O(n/2) = O(n)

from doubly_linked_base_7_8 import _DoublyLinkedBase
from exceptions_7_8 import Empty


def find_middle_node(doubly_linked_list):
    """Finds and returns the middle node of a doubly linked list
       If the list is even, returns the node slighthly left of center"""
    head = doubly_linked_list._header._next
    tail = doubly_linked_list._trailer._prev

    # walking head and tail toward the middle until they meet
    while tail._next != head:
        if tail._prev == head:
            return head
        elif tail == head:
            return head

        head = head._next
        tail = tail._prev

    raise Empty("Empty list does not have a middle node")


even_DLL = _DoublyLinkedBase()
odd_DLL = _DoublyLinkedBase()

# adding [0, 1, 2, 3] to the even doubly linked list. Middle node contains (int 1)
for i in range(4):
    even_DLL._insert_between(i, even_DLL._trailer._prev, even_DLL._trailer)

# adding [0, 1, 2, 3, 5] to the odd doubly linked list. Middle node contains (int 2)
for i in range(5):
    odd_DLL._insert_between(i, odd_DLL._trailer._prev, odd_DLL._trailer)


print("The middle node content of the even list is: {}".format(find_middle_node(even_DLL)._element))
print("The middle node content of the odd list is: {}".format(find_middle_node(odd_DLL)._element))
