# C-2.32
# Write a Python class that extends the Progression class so that each value
# in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your constructor
# should accept an optional parameter specifying the start value, using
# 65,536 as a default.

from progressions_2_32 import Progression
from math import sqrt

class SqrtProgression(Progression):

    def __init__(self, start=65536):
        super().__init__(start)

    def _advance(self):
        self._current = sqrt(self._current)


if __name__ == "__main__":
    sqrt_progression = SqrtProgression()
    sqrt_progression.print_progression(5)
