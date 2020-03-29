# Implementation of a singly link list
# Based from scripts examples in the book, but it was never completely built
# This class would not work correctly as is was presented.
#
# I added some functionalities to this class for it to work and for testing purposes:
#   - a header to initialise the list and to avoid boundary conditions
#   - a __str__ method easily verify the content of the list
#   - a __len__ method to verify the length
#   - a get_head method to return the first node of the list if it exists
#   - a get_tail method to return the last node of the list if it exists
#   - a tail attribute to remember access it without cycling through the list

from exceptions_7_27 import *


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
        """Initialise the list with a header but it still has a size of zero"""
        self._header = self.Node(None, None)
        self.head = None
        self.tail = None
        self._size = 0

    # ----------------------- linked list methods ------------------------
    def add_first(self, e):
        """Adds e to the beginning of the list, after the header"""
        newest = self.Node(e, None)

        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:
            newest._next = self.head
            self.head = newest

        self._header._next = newest
        self._size += 1

    def add_last(self, e):
        """Adds e to the end of the list"""
        newest = self.Node(e, None)

        if self.is_empty():
            self.head = newest
            self.tail = newest
            self._header._next = newest
        else:
            self.tail._next = newest
            self.tail = newest

        self._size += 1

    def remove_first(self):
        """Removes the first item of the list if it exists"""
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        head = self.head
        if self._size == 1:
            self.head = None
            self.tail = None
            self._header._next = None
        else:
            self.head = head._next
            self._header._next = self.head

        head._next = None                  # helps garbage collection
        self._size -= 1
        return head

    def remove_last(self):
        # This is an inefficient way to find the last element of the list,
        # it runs in O(n), but this is the only way to find it, because it is a singly linked list,
        # not a doubly linked list. This class is only for testing purposes anyway (small lists).

        """Removes the last item of the list if it exists"""
        if self.is_empty():
            raise Empty("Cannot remove from an empty list.")

        old_tail = self.tail
        if self._size == 1:
            self.head = None
            self.tail = None
            self._header._next = None
        else:
            new_tail = self._header
            while new_tail._next._next is not None:
                new_tail = new_tail._next
            new_tail._next = None
            self.tail = new_tail
        self._size -= 1
        return old_tail

    def get_head(self):
        """Returns the head element of the list"""
        if self.is_empty():
            raise Empty("Empty list does not have a head")
        return self.head

    def get_tail(self):
        """Finds and returns the tail element of the list"""
        if self.is_empty():
            raise Empty("Empty list does not have a tail")
        return self.tail

    def is_empty(self):
        """Returns True if empty"""
        return self._size == 0

    def get_size(self):
        """Returns the length of the list"""
        return self._size

    def __str__(self):
        """Printing the content of the list for visualisation and tests"""
        elements = []
        node = self._header
        while node._next is not None:  # for every node of the list besides _trailer
            node = node._next
            elements.append(str(node._element))
        return "[{}]".format(", ".join(elements))

    def __len__(self):
        """Enables len(SLL)"""
        return self._size
