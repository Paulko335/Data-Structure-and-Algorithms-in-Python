# R-7.15
# Provide support for a reversed method of the PositionalList class that
# is similar to the given iter , but that iterates the elements in reversed
# order.


from positional_list_7_15 import PositionalList
from exceptions_7_15 import Empty


class PositionalListWithFindMethod(PositionalList):

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)


my_list = PositionalListWithFindMethod()

# adding [0, 1, 2, 3] to the list
for i in range(4):
    my_list.add_last(i)

for i in reversed(my_list):
    print(i)
