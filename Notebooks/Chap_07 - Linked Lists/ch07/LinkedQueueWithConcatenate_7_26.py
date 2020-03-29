# Implementation of a queue ADT using a singly linked list as data.
# It originates from the exercice 7.26


from singly_linked_list_7_26 import SinglyLinkedList

class Queue_From_Singly_Linked_List(SinglyLinkedList):
    def __init__(self):
        self._data = SinglyLinkedList()

    def enqueue(self, e):
        """enqueue the item e"""
        self._data.add_last(e)

    def dequeue(self):
        """dequeue the first item enqueued"""
        if self.is_empty():
            raise Empty("Cannot dequeue from an empty queue")

        return self._data.remove_first()._element

    def first(self):
        """returns the first item in the queue"""
        if self.is_empty():
            raise Empty("Empty queue does not have a first element")
        return self._data.get_head()._element

    def is_empty(self):
        """returns True if the queue is empty"""
        return self._data.is_empty()

    def __len__(self):
        """returns the length of the queue"""
        return len(self._data)

    def __str__(self):
        return str(self._data)
