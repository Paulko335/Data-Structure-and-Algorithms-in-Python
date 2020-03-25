# R-7.14
# Repeat the previous process using recursion. Your method should not
# contain any loops. How much space does your method use in addition to
# the space used for L?

# This method using recursion does not use much more space than the loop method
# It passes the reference of the node, not the whole list.


from positional_list_7_14 import PositionalList
from exceptions_7_14 import Empty


class PositionalListWithFindMethod(PositionalList):


    def find(self, e, first_node="Initialization"):
        """Returns the first node containing the element e or a ValueError"""
        if first_node is "Initialization":  # cannot use None as initialization because of class implementation
            first_node = self.first()       # if it's the first call to the method, first_note is the head

        if first_node is None:
            raise ValueError("{} is not in list".format(e))     # ValueError if e not in list
        elif first_node.element() == e:
            return first_node                                   # returns node if e is in the node

        return self.find(e, self.after(first_node))             # returns itself recursively


my_list = PositionalListWithFindMethod()

# adding [0, 1, 2, 3] to the list
for i in range(4):
    my_list.add_last(i)

found_node = my_list.find(3)
print("The maximum of the list is: {}".format(found_node))
print("It contains: {} {}".format(type(found_node.element()), found_node.element()))
