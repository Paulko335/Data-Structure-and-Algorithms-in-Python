# R-6.11
# Give a simple adapter that implements our queue ADT while using a
# collections.deque instance for storage.

from collections import deque


class AdapterQueue:

    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._queue[0]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._queue.popleft()

    def enqueue(self, e):
        self._queue.append(e)
