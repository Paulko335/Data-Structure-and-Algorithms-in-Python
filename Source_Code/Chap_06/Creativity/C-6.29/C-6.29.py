# C-6.29
# In certain applications of the queue ADT, it is common to repeatedly
# dequeue an element, process it in some way, and then immediately enqueue
# the same element. Modify the ArrayQueue implementation to include
# a rotate( ) method that has semantics identical to the combination,
# Q.enqueue(Q.dequeue( )). However, your implementation should
# be more efficient than making two separate calls (for example, because
# there is no need to modify size).

from array_queue_6_29 import ArrayQueue


class ArrayQueue_6_29(ArrayQueue):

    def __init__(self):
        super().__init__()

    def rotate(self):
        front_item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        avail = (self._front + self._size - 1) % len(self._data)
        self._data[avail] = front_item


Q = ArrayQueue_6_29()
for i in range(4):      # Q contains [0, 1, 2, 3], where 0 is the first in line
    Q.enqueue(i)

Q.rotate()              # Q now contains [1, 2, 3, 0], because of rotate method

for i in range(4):      # Proof of the new queue order
    print(Q.dequeue())
