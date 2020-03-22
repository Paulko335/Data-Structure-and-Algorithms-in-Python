# Implementation of a circularly linked list, based on notions seen in the book

from exceptions_7_5 import Empty


class CircularlyLinkedList:
    """Implementation of a circularly linked list."""

    # ----------------------- nested Node class ------------------------
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ----------------------- linked list methods ------------------------
    def __init__(self):
        self._tail = self.Node(None, None)
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def add_first(self, e):
        """Adds item as the new head"""
        newest = self.Node(e, None)

        if self.is_empty():
            newest._next = newest   # initialize circularly
            self._tail = newest     # the tail is the only item of the list
        else:
            newest._next = self._tail._next     # newest goes between _tail and _tail._next
            self._tail._next = newest           # head is now newest
        self._size += 1

    def add_last(self, e):
        """Adds item as the new tail"""
        latest = self.Node(e, None)

        if self.is_empty():
            latest._next = latest               # initialize circularly
            self._tail = latest                 # the tail is the only item of the list
        else:
            latest._next = self._tail._next     # latest goes between _tail and _tail._next
            self._tail._next = latest           # tail points to latest
            self._tail = latest                 # latest is now the tail
        self._size += 1

    def get_head(self):
        """Returns the head of the list"""
        if self.is_empty():
            raise Empty("List is empty, cannot return the head")
        return self._tail._next

    def get_tail(self):
        """Returns the tail of the list"""
        if self.is_empty():
            raise Empty("List is empty, cannot return the tail")
        return self._tail

    def rotate(self):
        """Moves the list forward by one item"""
        if not self.is_empty():
            self._tail = self._tail._next

    def __str__(self):
        """Printing itself in an easily readable format."""
        readable_list = []
        for item in range(self._size):
            readable_list.append(str(self._tail._next._element))
            self.rotate()
        return "[{}]".format(", ".join(readable_list))


if __name__ == "__main__":
    CLL = CircularlyLinkedList()
    CLL.add_first(0)
    CLL.add_first(1)
    CLL.add_first(2)
    print(CLL)
    print("head: ", CLL.get_head()._element)
    print("tail: ", CLL.get_tail()._element)
    print("")

    CLL2 = CircularlyLinkedList()
    CLL2.add_last(0)
    CLL2.add_last(1)
    CLL2.add_last(2)
    print(CLL2)
    print("head: ", CLL2.get_head()._element)
    print("tail: ", CLL2.get_tail()._element)
    print("")

    CLL3 = CircularlyLinkedList()
    print("Empty list:", CLL3)