# C-2.29
# Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer
# is assigned a minimum monthly payment, as a percentage of the
# balance, and so that a late fee is assessed if the customer does not subsequently
# pay that minimum amount before the next monthly cycle.

# Added _minimum_monthly_payment variable to CreditCard class to track the amount to pay
# Added _monthly_payment_made variable to CreditCard class to track the amount paid
# Updated process_month method to add a late fee if _monthly_payment_made is not made

from credit_card_2_29 import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self._balance += 5  # assess penalty
        return success  # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor

        if self._monthly_payment_made < self._minimum_monthly_payment:
            self._balance += 10                        # late fee

        # must repay at least 10% of balance per month
        self._minimum_monthly_payment = self._balance * 0.10
        # Reset variable to zero for the next month
        self._monthly_payment_made = 0

    def get_minimum_monthly_payment(self):
        return self._minimum_monthly_payment


if __name__ == "__main__":
    card = PredatoryCreditCard("John", "BigBank", "0123 4567 8910 1112", 5000, 0.20)
    card.charge(100)
    print(card.get_balance())   # balance is 100$
    card.process_month()        # balance is 101.53

    print(card.get_minimum_monthly_payment()) # must pay at least 10.15$
    card.make_payment(20)                     # paid 20$
    print(card.get_balance())                 # balance is  81.53$

    card.process_month()                      # add interest but no extra fee
    print(card.get_balance())                 # balance is 82.78$

    print(card.get_minimum_monthly_payment()) # must pay at least 8.28
    card.process_month()                      # did not pay in time
    print(card.get_balance())                 # add interests and extra fees, balance is 94.05
