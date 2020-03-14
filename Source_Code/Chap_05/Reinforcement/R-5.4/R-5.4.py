# R-5.4
# Our DynamicArray class, as given in Code Fragment 5.3, does not support
# use of negative indices with getitem . Update that method to better
# match the semantics of a Python list.

from dynamic_array import DynamicArray

class DynamicArray_5_4(DynamicArray):

    def __init__(self):
        super().__init__()

    def __getitem__(self, k):
        """Return element at index k."""
        if not -self._n <= k < self._n:
          raise IndexError('invalid index')
        return self._A[k]                              # retrieve from array

dyn_arr = DynamicArray_5_4()
dyn_arr.append(1)
dyn_arr.append(2)
print(dyn_arr[-1])