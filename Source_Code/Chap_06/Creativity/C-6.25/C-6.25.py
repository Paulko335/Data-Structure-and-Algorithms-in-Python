# C-6.25
# Describe how to implement the queue ADT using two stacks as instance
# variables, such that all queue operations execute in amortized O(1) time.
# Give a formal proof of the amortized bound.

# The first stack (_incoming) is used as an income stack. Enqueued elements are simply added to it with push()
# The second stack (_buffer) is the buffer for dequeues. It contains pushed element but in a reversed order.
# therefore, it pops element in the right order for a queue
#
# If _buffer is empty but _incoming is not, _switch_stack method transfers every element in a reversed order

from array_stack_6_25 import ArrayStack
from exceptions_6_25 import Empty

class Queue_From_Two_Stacks:

    def __init__(self):
        self._incoming = ArrayStack()
        self._buffer = ArrayStack()

    def __len__(self):
        """Return the total length of the stacks"""
        return len(self._incoming) + len(self._buffer)

    def _switch_stacks(self):
        for _ in range(len(self._incoming)):
            self._buffer.push(self._incoming.pop())

    def is_empty(self):
        """Return True if total length is zero """
        return len(self._incoming) + len(self._buffer) == 0

    def enqueue(self, e):
        self._incoming.push(e)

    def dequeue(self):
        if len(self._buffer) == 0:              # if both stacks are empty, raise exception
            if len(self._incoming) == 0:
                raise Empty("Queue is empty")
            else:                               # if self._incoming isn't empty, transfer to self._buffer
                self._switch_stacks()
        return self._buffer.pop()               # return the first value

    def first(self):
        if len(self._buffer) == 0:              # if both stacks are empty, raise exception
            if len(self._incoming) == 0:
                raise Empty("Queue is empty")
            else:                               # if self._incoming isn't empty, transfer to self._buffer
                self._switch_stacks()
        return self._buffer.top()               # return the first value

if __name__ == "__main__":
    Q = Queue_From_Two_Stacks()
    print("Length of Q: {}".format(len(Q)))
    print("Q if empty: {}".format(Q.is_empty()))

    Q.enqueue(0)
    print("Length of Q: {}".format(len(Q)))
    print("Q if empty: {}".format(Q.is_empty()))

    Q.enqueue(1)
    print(Q.dequeue())

    Q.enqueue(2)
    Q.enqueue(3)

    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
