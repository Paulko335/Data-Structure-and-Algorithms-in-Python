# C-2.30
# At the close of Section 2.4.1, we suggest a model in which the CreditCard
# class supports a nonpublic method, set balance(b), that could be used
# by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the
# CreditCard and PredatoryCreditCard classes accordingly.

from credit_card_2_30 import CreditCard


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


if __name__ == "__main__":
    card = PredatoryCreditCard("John", "BigBank", "0123 4567 8910 1112", 5000, 0.20)
    card.charge(5000)            # we full the card
    print(card.get_balance())    # balance is 5000

    card._set_balance(0)         # we reset the card
    print(card.get_balance())    # balance is 0
