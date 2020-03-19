# C-6.24
# Describe how to implement the stack ADT using a single queue as an
# instance variable, and only constant additional local memory within the
# method bodies. What is the running time of the push(), pop(), and top()
# methods for your design?

from exceptions_6_24 import Empty
from array_queue_6_24 import ArrayQueue

class Stack_Using_Queue:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = ArrayQueue()   # Using a queue instead of a list

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)      # Using ArrayQueue len method

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.enqueue(e)       # append() becomes enqueue()

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            for _ in range(len(self._data) - 1):    # cycling trough elements in the queue
                self._data.enqueue(self._data.dequeue())
            top = self._data.first()
            self._data.enqueue(self._data.dequeue())
        return top   # accessing first element with the method first,
                                    # intead of using self._data[0]

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        for _ in range(len(self._data) - 1):    # cycling trough elements in the queue
            self._data.enqueue(self._data.dequeue())
        return self._data.dequeue()                 # returning the last element of the queue
                                                # it is equivalent to returning the first of the stack


if __name__ == "__main__":
    S = Stack_Using_Queue()
    S.push(0)
    S.push(1)
    S.push(2)
    S.push(3)
    print("{} is at the top of the stack".format(S.top()))
    print("{} comes out of the stack first".format(S.pop()))

    # push() is O(1), because Q.enqueue() is O(1)
    # pop is O(n), because it cycles trough the whole queue before returning
    # top() is O(n), because it cycles trough the whole queue before returning
