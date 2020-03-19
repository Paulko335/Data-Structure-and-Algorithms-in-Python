# C-6.27
# Suppose you have a stack S containing n elements and a queue Q that is
# initially empty. Describe how you can use Q to scan S to see if it contains a
# certain element x, with the additional constraint that your algorithm must
# return the elements back to S in their original order. You may only use S,
# Q, and a constant number of other variables.

from array_queue_2_27 import ArrayQueue
from array_stack_2_27 import ArrayStack


def is_in_stack(element, stack):
    Q = ArrayQueue()
    occurrence = False

    # moving every item from the stack to the queue and checking if the element is present
    while not stack.is_empty():
        new_member = stack.pop()
        Q.enqueue(new_member)
        if new_member == element:
            occurrence = True

    while not Q.is_empty():
        stack.push(Q.dequeue())     # stack is now in a reversed order

    while not stack.is_empty():           # reversing the stack once again
        Q.enqueue(stack.pop())

    while not Q.is_empty():               # stack is now in the correct order
        stack.push(Q.dequeue())

    return occurrence


if __name__ == "__main__":

    S = ArrayStack()
    Q = ArrayQueue()

    for item in range(10):
        S.push(item)

    print(is_in_stack(5, S))    # is the int 5 inside the stack?

    for item in range(len(S)):  # verifying the order of the stack
        print(S.pop())
