# C-7.24
# Give a complete implementation of the stack ADT using a singly linked
# list that includes a header sentinel.

from singly_linked_list_7_24 import SinglyLinkedList
from exceptions_7_24 import Empty


class Stack_From_Singly_Linked_List():
    def __init__(self):
        self._data = SinglyLinkedList()

    def push(self, e):
        self._data.add_first(e)

    def pop(self):
        if self.is_empty():
            raise Empty("Cannot pop from an empty stack")
        return self._data.remove_first()._element

    def top(self):
        if self.is_empty():
            raise Empty("Cannot pop from an empty stack")
        return self._data.get_head()._element

    def is_empty(self):
        return self._data.is_empty()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


stack = Stack_From_Singly_Linked_List()

for i in range(4):      # stack contains [3, 2, 1, 0]
    stack.push(i)

print("stack:", stack)
print("popped first:", stack.pop())          # removes 3
print("top is :", stack.top())               # top is 2
print("stack:", stack)
print("stack is empty:", stack.is_empty())   # False
print("length:",len(stack))                  # length is 3

print("popping 3 times")
stack.pop()                                  # removes 2
stack.pop()                                  # removes 1
stack.pop()                                  # removes 0
print("stack:", stack)
print("stack is empty:", stack.is_empty())   # True
