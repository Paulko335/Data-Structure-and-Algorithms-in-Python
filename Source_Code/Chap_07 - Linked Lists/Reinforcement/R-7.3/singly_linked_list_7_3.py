# Implementation of a singly link list
# Based from scripts examples in the book, but it was never completely built
# This class would not work correctly as is was presented.
#
# I added some functionalities to this class for it to work and for testing purposes:
#   - a header and a trailer to initialise the list and to avoid boundary conditions
#   - a __str__ method easily verify the content of the list
#   - a __len__ method to verify the length


from exceptions_7_3 import *

class SinglyLinkedList:
    """Singly linked list implementation"""

    # ----------------------- nested Node class ------------------------
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Initialise the list with a trailer and a header but it still has a size of zero"""
        self._trailer = self.Node(None, None)
        self._header = self.Node(None, self._trailer)
        self._size = 0

    # ----------------------- linked list methods ------------------------
    def add_first(self, e):
        """Adds e to the beginning of the list, after the header"""
        newest = self.Node(e, self._header._next)
        self._header._next = newest
        self._size += 1

    def add_last(self, e):
        """Adds e to the end of the list, before the trailer"""
        # This is an inefficient way to find the last element of the list before the trailer,
        # it runs in O(n), but this is the only way to find it, because it is a singly linked list,
        # not a doubly linked list. This class is only for testing purposes anyway (small lists).
        # beginning
        newest = self.Node(e, self._trailer)
        tail = self._header
        while tail._next._next is not None:
            tail = tail._next
        tail._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        self._header._next = self._header._next._next
        self._size -= 1

    def remove_last(self):
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        new_tail = self._header._next
        while new_tail._next._next is not None:
            new_tail = new_tail._next

        old_tail = new_tail._next
        old_tail._next = None           # For garbage collection

        new_tail._next = self._trailer
        self._size -= 1

    def get_head(self):
        if self.is_empty():
            raise Empty("Empty list cannot have a head")
        return self._header._next

    # This implementation of a SLL has a trailer after the true tail
    # Therefore, we can use the function from exercise 7_1 to get the tail of the first list
    def get_tail(self):
        """Finds and returns the tail of the list, not the trailer"""
        if self.is_empty():
            raise Empty("Empty list cannot have a tail")
        tail = self._header
        while tail._next._next is not None:
            tail = tail._next
        return tail

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def __str__(self):
        """Printing the content of the list for visualisation and tests"""
        elements = []
        node = self._header
        while node._next._next is not None:  # for every node of the list besides _trailer and _header
            node = node._next
            elements.append(str(node._element))
        return "[{}]".format(", ".join(elements))

    def __len__(self):
        return self._size

if __name__ == "__main__":
    SLL = SinglyLinkedList()

    for i in range(4):
        SLL.add_last(i)
    print("Added 0, 1, 2, 3 at the end, SSL contains: {}".format(SLL))

    SLL.remove_first()
    print("Removed first element, SSL contains: {}".format(SLL))

    SLL.remove_last()
    print("Removed last element, SSL contains: {}".format(SLL))

    print("The length of SSL is: {}".format(len(SLL)))