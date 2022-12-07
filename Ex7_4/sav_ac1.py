from b_ac1 import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer, account_number, interest_rate, balance=0):
        self.interest_rate = interest_rate
        super().__init__(customer, account_number, balance)

    def add_interest(self):
        self.balance *= (1. + self.interest_rate / 100)