# R-7.7
# Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
# has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
# queue. Implement such a method for the LinkedQueue class of Section
# 7.1.2 without the creation of any new nodes.


from linked_queue_7_7 import LinkedQueue

class LinkedQueueWithRotate(LinkedQueue):

    def rotate(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        self._tail._next = self._head  # moving the head after the tail (the end)
        self._head = self._head._next  # new head is the node after the old head
        self._tail = self._tail._next  # new tail is the node after the tail
        self._tail._next = None        # new tail must point to None


testing_rotate = LinkedQueueWithRotate()


for i in range(4):
    testing_rotate.enqueue(i)
print("Queue contains [0, 1, 2, 3]\n")

print("using rotate method")
testing_rotate.rotate()
print("using rotate method\n")

testing_rotate.rotate()
print("Queue contains [2, 3, 0, 1]\n")

print("proof:")
for i in range(4):
    print(testing_rotate.dequeue())
