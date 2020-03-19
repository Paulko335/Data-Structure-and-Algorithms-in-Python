# R-2.4
# Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:

    def __init__(self, name, petal_count, price):
        self.name = name
        self.petal_count = petal_count
        self.price = price

    def get_name(self):
        return self.name

    def get_petal_count(self):
        return self.petal_count

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name =  new_name

    def set_petals(self, new_petals):
        self.petals = new_petals

    def set_price(self, new_price):
        self.price = new_price
