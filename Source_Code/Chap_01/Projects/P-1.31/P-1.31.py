# P-1.31
# Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.


# I added an argument to use your own monetary system
def make_change(charged, given, monetary_system):
    difference = round(given - charged, 2)
    currencies = {}
    for currency in monetary_system:
        currencies[currency] = int(difference // currency)
        difference = difference % currency
    return currencies.values()


american_money = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05, 0.01]
print(make_change(213.56, 300, american_money))
