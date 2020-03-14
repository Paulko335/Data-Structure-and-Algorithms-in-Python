# C-2.31
# Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the previous
# two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults.

from progressions_2_31 import Progression


class AbsoluteDifferenceProgression(Progression):

    def __init__(self, first=2, second=200):
        super().__init__(first)
        self.first = first
        self.second = second
        self.count = 2

    def _advance(self):
        if self.count == 1:
            self._current = self.first
        elif self.count == 2:
            self._current = self.second
        else:
            self._current = abs(self.second - self.first)
            self.first, self.second = self.second, self._current
        self.count += 1


if __name__ == "__main__":
    abs_progression = AbsoluteDifferenceProgression()
    abs_progression.print_progression(10)
