# R-7.12
# Redo the previously problem with max as a method of the PositionalList
# class, so that calling syntax L.max( ) is supported.


from positional_list_7_12 import PositionalList
from exceptions_7_12 import Empty


class PositionalListWithMaxMethod(PositionalList):

    def max(self):
        if self.first() is None:
            raise Empty("Empty list does not have a max")

        max_value = self.first().element()  # initialise max as the first element
        for element in self:
            if element > max_value:  # if a bigger element is found, max is this new one
                max_value = element
        return max_value


my_list = PositionalListWithMaxMethod()

# adding [0, 1, 2, 3] to the list
for i in range(4):
    my_list.add_last(i)

print("The maximum of the list is: {}".format(my_list.max()))
