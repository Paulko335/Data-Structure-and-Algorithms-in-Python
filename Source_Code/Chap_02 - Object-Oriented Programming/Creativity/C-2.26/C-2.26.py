# C-2.26
# The SequenceIterator class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The first call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.


class ReversedSequenceIterator():
    """A reverse iterator for any sequence"""
    def __init__(self, sequence):
        """Storing the sequence and the current position"""
        self.sequence = sequence
        self.k = len(sequence)

    def __next__(self):
        """Returns the sequence in reverse order"""
        self.k -= 1
        if self.k >= 0:
            return self.sequence[self.k]
        else:                            # If we reach the end
            raise StopIteration()

    def __iter__(self):
        return self


def main():
    sequence = ["a", "bb", "ccc"]
    for item in ReversedSequenceIterator(sequence):
        print(item)


if __name__ == "__main__":
    main()
