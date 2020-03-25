# R-7.13
# Update the PositionalList class to support an additional method find(e),
# which returns the position of the (first occurrence of ) element e in the list
# (or None if not found).

from positional_list_7_13 import PositionalList
from exceptions_7_13 import Empty


class PositionalListWithFindMethod(PositionalList):

    def find(self, e):
        cursor = self.first()
        while cursor is not None:
            if cursor.element() == e:
                return cursor
            cursor = self.after(cursor)
        return None


my_list = PositionalListWithFindMethod()

# adding [0, 1, 2, 3] to the list
for i in range(4):
    my_list.add_last(i)

found_node = my_list.find(3)
print("The maximum of the list is: {}".format(found_node))
print("It contains: {} {}".format(type(found_node.element()), found_node.element()))
