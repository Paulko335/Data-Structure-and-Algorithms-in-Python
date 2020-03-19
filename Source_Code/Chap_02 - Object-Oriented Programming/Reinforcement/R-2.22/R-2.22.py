# R-2.22
# The collections.Sequence abstract base class does not provide support for
# comparing two sequences to each other. Modify our Sequence class from
# Code Fragment 2.14 to include a definition for the eq method, so
# that expression seq1 == seq2 will return True precisely when the two
# sequences are element by element equivalent

from abc import ABCMeta, abstractmethod           # need these definitions


class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:                          # found match
                return True
        return False

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                match = self[i] == other[i]
                if not match:                         # They are not equal
                    return False
        return True

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:                          # leftmost match
                return j
        raise ValueError('value not in sequence')     # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:                          # found a match
                k += 1
        return k
