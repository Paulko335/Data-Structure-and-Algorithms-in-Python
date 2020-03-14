# R-2.7
# Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.

# R-2.6
# If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.

# R-2.7
# The CreditCard class of Section 2.3 initializes the balance of a new account
# to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Must charge a number")

        if price + self._balance > self._limit:  # if charge would exceed limit,
            return False  # cannot accept charge
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if amount < 0:
            raise ValueError("Can't make a negative payment")
        else:
            self._balance -= amount
