# C-6.16
# Modify the ArrayStack implementation so that the stack’s capacity is limited
# to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If push is called when the stack is at
# full capacity, throw a Full exception (defined similarly to Empty).

from array_stack_6_16 import ArrayStack

stack = ArrayStack(maxlen=1)
stack.push(0)
stack.push(1)
