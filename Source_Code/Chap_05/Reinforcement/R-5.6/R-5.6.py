# R-5.6
# Our implementation of insert for the DynamicArray class, as given in
# Code Fragment 5.5, has the following inefficiency. In the case when a resize
# occurs, the resize operation takes time to copy all the elements from
# an old array to a new array, and then the subsequent loop in the body of
# insert shifts many of those elements. Give an improved implementation
# of the insert method, so that, in the case of a resize, the elements are
# shifted into their final position during that operation, thereby avoiding the
# subsequent shifting.

from dynamic_array_5_6 import DynamicArray


class Dynamic_Array_5_6(DynamicArray):

    def __init__(self):
        super().__init__()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)

        if self._n == self._capacity:                  # not enough room
            #self._resize(2 * self._capacity)          # so double capacity
            B = self._make_array(2 * self._capacity)
            for i in range(k):  # for each existing value
                B[i] = self._A[i]
            B[k] = value
            for j in range(k, self._n):
                B[j+1] = self._A[j]
            self._A = B  # use the bigger array
            self._n += 1
            self._capacity = self._capacity * 2

        else:
            for j in range(self._n, k, -1):                # shift rightmost first
                self._A[j] = self._A[j-1]
            self._A[k] = value                             # store newest element
            self._n += 1


dyn_arr = Dynamic_Array_5_6()
dyn_arr.insert(0, 1)
dyn_arr.insert(0, 0)
print(dyn_arr[0], dyn_arr[1])
