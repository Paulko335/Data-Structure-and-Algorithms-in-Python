# R-7.3
# Describe a recursive algorithm that counts the number of nodes in a singly
# linked list.

from singly_linked_list_7_3 import SinglyLinkedList


def count_nodes(head):
    if head._next is None:
        return 0
    else:
        return 1 + count_nodes(head._next)


sll = SinglyLinkedList()
for i in range(4):
    sll.add_last(i)
print(count_nodes(sll.get_head()))
