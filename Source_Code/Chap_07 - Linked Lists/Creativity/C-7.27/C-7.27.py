# C-7.27
# Give a recursive implementation of a singly linked list class, such that an
# instance of a nonempty list stores its first element and a reference to a list
# of remaining elements.


from singly_linked_list_7_27 import SinglyLinkedList


class SinglyLinkedListWithReverse(SinglyLinkedList):

    def reverse(self, head_node):
        if head_node._next is None:
            self._header._next = head_node
            self.head = head_node
            return head_node

        else:
            reversed_SLL = self.reverse(head_node._next)
            head_node._next._next = head_node
            head_node._next = None
            return reversed_SLL


SLL = SinglyLinkedListWithReverse()

for i in range(4):
    SLL.add_last(i)

print("SLL:", SLL)
print("Head of SLL is:", SLL.get_head()._element)

print("Reversing SLL with reverse() method")
SLL.reverse(SLL.head)

print("SLL:", SLL)
print("Head of SLL is:", SLL.get_head()._element)
