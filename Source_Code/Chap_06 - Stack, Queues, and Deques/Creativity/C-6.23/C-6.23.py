# C-6.23
# Suppose you have three nonempty stacks R, S, and T. Describe a sequence
# of operations that results in S storing all elements originally in T below all
# of S’s original elements, with both sets of those elements in their original
# order. The final configuration for R should be the same as its original
# configuration. For example, if R = [1,2,3], S = [4,5], and T = [6,7,8,9],
# the final configuration should have R = [1,2,3] and S = [6,7,8,9,4,5].

from array_stack_6_23 import ArrayStack

# Added __str__ method to ArrayStack
#
# def __str__(self):
#     string = "".join(str(element) for element in self._data)
#     if string == "":
#         string = "This stack is empty"
#     return string


def combine_two_stacks(A, B, C):
    a_original_length = len(A)

    while len(C) > 0:
        A.push(C.pop())
    while len(B) > 0:
        C.push(B.pop())
    while len(A) != a_original_length:
        B.push(A.pop())
    while len(C) > 0 :
        B.push(C.pop())


R = ArrayStack()
R.push(1)
R.push(2)
R.push(3)

S = ArrayStack()
S.push(4)
S.push(5)

T = ArrayStack()
T.push(6)
T.push(7)
T.push(8)
T.push(9)

combine_two_stacks(R, S, T)

print(R)
print(S)
print(T)
