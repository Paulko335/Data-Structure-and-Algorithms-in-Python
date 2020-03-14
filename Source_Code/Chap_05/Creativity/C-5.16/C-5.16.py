# C-5.16
# Implement a pop method for the DynamicArray class, given in Code Fragment
# 5.3, that removes the last element of the array, and that shrinks the
# capacity, N, of the array by half any time the number of elements in the
# array goes below N/4.

from dynamic_array import DynamicArray

class DynamicArray_5_16(DynamicArray):

    def __init__(self):
        super().__init__()

    def pop(self):
        """Removes the last element of the array and shrinks the capacity when needed"""
        if self._n == 0:
            raise ValueError("List is empty, cannot remove last element.")
        else:
            self._A[-1] = None
            self._n = self._n - 1
            if self._n < self._capacity / 4:
                self._resize(self._capacity // 2)

my_arr = DynamicArray_5_16()

my_arr.append(0)
print(my_arr.pop())
print(my_arr.pop())

