# C-7.25
# Give a complete implementation of the queue ADT using a singly linked
# list that includes a header sentinel.


from singly_linked_list_7_25 import SinglyLinkedList
from exceptions_7_25 import Empty


class Queue_From_Singly_Linked_List():
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
            raise Empty("Empty queue has no first element")
        head = self._data.get_head()
        return head._element

    def is_empty(self):
        """returns True if the queue is empty"""
        return self._data.is_empty()

    def __len__(self):
        """returns the length of the queue"""
        return len(self._data)

    def __str__(self):
        return str(self._data)


queue = Queue_From_Singly_Linked_List()

for i in range(4):      # stack contains [3, 2, 1, 0] with 0 being the first element
    queue.enqueue(i)

print("queue is:", queue)
print("first is:", queue.first())
print("dequeued first:", queue.dequeue())          # removes 0
print("queue is:", queue)

print("first is:", queue.first())          # top is 1
print("queue is empty", queue.is_empty())     # False
print("length of queue is:", len(queue))           # length is 3

print("dequeuing the whole queue")

queue.dequeue()                 # removes 2
print("queue is:", queue)

queue.dequeue()                 # removes 0
print("queue is:", queue)

queue.dequeue()                 # removes 0
print("queue is:", queue)

print("queue is empty:", queue.is_empty())     # True
