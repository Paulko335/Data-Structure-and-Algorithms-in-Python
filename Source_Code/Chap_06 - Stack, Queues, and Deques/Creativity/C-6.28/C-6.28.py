# C-6.28
# Modify the ArrayQueue implementation so that the queue’s capacity is
# limited to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If enqueue is called when the queue
# is at full capacity, throw a Full exception (defined similarly to Empty).

# modified enqueue method and added self._maxlen attribute

from array_queue_6_28 import ArrayQueue

Q = ArrayQueue(maxlen=2)

for index in range(3):
    try:
        Q.enqueue(0)
        print("enqueued {}".format(index))
    except Exception as e:
        print(e)
