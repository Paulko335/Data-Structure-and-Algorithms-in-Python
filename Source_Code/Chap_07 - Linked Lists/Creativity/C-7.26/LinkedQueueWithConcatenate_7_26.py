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


if __name__ == "__main__":
    queue = Queue_From_Singly_Linked_List()

    for i in range(4):  # stack contains [3, 2, 1, 0] with 0 being the first element
        queue.enqueue(i)

    print("queue is:", queue)
    print("first is:", queue.first())
    print("dequeued first:", queue.dequeue())  # removes 0
    print("queue is:", queue)

    print("first is:", queue.first())  # top is 1
    print("queue is empty", queue.is_empty())  # False
    print("length of queue is:", len(queue))  # length is 3

    print("dequeuing the whole queue")
    print("queue is:", queue)

    queue.dequeue()  # removes 0
    print("queue is:", queue)

    queue.dequeue()  # removes 0
    print("queue is:", queue)
    queue.dequeue()  # removes 0

    print("queue is empty:", queue.is_empty())  # True
