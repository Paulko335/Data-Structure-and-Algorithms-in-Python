# R-2.15
# The Vector class of Section 2.3.3 provides a constructor that takes an integer
# d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates
# <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it produces
# a vector with coordinates based on that sequence.

# Added construction by a sequence in __init__

import collections


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            try:
                self._coords = [value for value in d]
            except:
                raise ValueError("Parameter must be a valid iterable")

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return the sum of an iterable and the vector"""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __sub__(self, other):
        """Return dif of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __mul__(self, other):
        """Defines scalar multiplication of a vector"""
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
            return result
        elif isinstance(other, (Vector, list)):
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            else:
                result = 0
                for i in range(len(self)):
                    result += self[i] * other[i]
                return result
        else:
            raise TypeError("Invalid parameter type.")

    def __rmul__(self, other):
        """Defines scalar multiplication of a vector"""
        if isinstance(other, (int, float)):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
            return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other             # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    def __neg__(self):
        """Returns the opposite vector"""
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return  result

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords


if __name__ == '__main__':

    v1 = Vector(2)
    v1[0] = 1
    v1[1] = 1
    v2 = Vector(2)
    v2[0] = 3
    v2[1] = 4

    v3 = v1 - v2
    print(v3)
    print(-v3, "\n")           # __neg__

    print(v1 + [2, 2])         # __add__
    print([2, 2] + v1, "\n")   # __radd__

    print(v1 * 3)              # __mul__
    print(3 * v1, "\n")        # __rmul__

    print(v1 * v2)             # __mul__

    v4 = Vector([0, 1, 2, 3])  # __init__
    print(v4)
