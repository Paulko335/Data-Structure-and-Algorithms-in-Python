# C-6.26
# Describe how to implement the queue ADT using two stacks as instance
# variables, such that all queue operations execute in amortized O(1) time.
# Give a formal proof of the amortized bound.

from array_stack_6_26 import ArrayStack
from exceptions_6_26 import Empty

class Deque_From_Two_Stacks:

    def __init__(self):
        self._top_stack = ArrayStack()
        self._bottom_stack = ArrayStack()

    def __len__(self):
        """Return total length of stacks"""
        return len(self._top_stack) + len(self._bottom_stack)

    def _switch_stacks(self):
        """Transfers element from the not empty one to the empty one"""
        empty = self._top_stack         # top stack is marked as the empty one
        nonempty = self._bottom_stack
        if len(nonempty) == 0:          # if top stack was is fact the not empty one, reverse them
            empty, nonempty = nonempty, empty

        for _ in range(len(nonempty)):  # transfer every element from nonempty to empty
            empty.push(nonempty.pop())

        # print to show that this method is performing correctly, remove it when using the class
        print("_switch_stacks performed")

    def is_empty(self):
        return len(self._top_stack) + len(self._bottom_stack) == 0

    def add_first(self, e):
        self._top_stack.push(e)

    def add_last(self, e):
        self._bottom_stack.push(e)

    def delete_first(self):
        if len(self._top_stack) == 0:
            if len(self._bottom_stack) == 0:
                raise Empty("Deque is empty.")
            else:
                self._switch_stacks()
        return self._top_stack.pop()

    def delete_last(self):
        if len(self._bottom_stack) == 0:
            if len(self._top_stack) == 0:
                raise Empty("Deque is empty.")
            else:
                self._switch_stacks()
        return self._bottom_stack.pop()

    def first(self):
        if len(self._top_stack) == 0:
            if len(self._bottom_stack) == 0:
                raise Empty("Deque is empty.")
            else:
                self._switch_stacks()
        return self._top_stack.top()

    def last(self):
        if len(self._bottom_stack) == 0:
            if len(self._top_stack) == 0:
                raise Empty("Deque is empty.")
            else:
                self._switch_stacks()
        return self._bottom_stack.top()


Deque = Deque_From_Two_Stacks()
Deque.add_first(2)
Deque.add_first(3)
Deque.add_last(1)
Deque.add_last(0)
print("Deque now contains [0, 1, 2 ,3], where 0 is the last element")

print(Deque.delete_last())
print(Deque.delete_last())
print(Deque.delete_last())      # _bottom_stack is empty, _switch_stacks method is used
print(Deque.delete_first())     # _top_stack is empty, _switch_stacks method is used


# The only problem with this implementation is if you pop successively from top
# and then bottom when only one of the stack has elements. For every pop, the
# class transfers every elements to the other stack, resulting in a O(n^2) in
# the worst case.
# --> It is the sum of : n + (n-1) + (n-2) + ... + 3 + 2 + 1 = n(n+1)/2 element transfered
