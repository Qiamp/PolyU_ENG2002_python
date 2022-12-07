from b_ac1 import BankAccount


class CurrentAccount(BankAccount):

    def __init__(self, customer, account_number, annualFee, transactionLimit, balance=0):
        self.annual_fee = annualFee
        self.transaction_limit = transactionLimit
        super().__init__(customer, account_number, balance)

    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid withdrawal amount:', amount)
            return
        if amount > self.balance:
            print('Insufficient funds')
            return
        if amount > self.transaction_limit:
            print('{0:s}{1:.2f} exceeds the single transaction limit of {0:s}{2:.2f}'.format(self.currency, amount,self.transaction_limit))
            return
        self.balance -= amount

    def apply_annual_fee(self):
        self.balance = max(0., self.balance - self.annual_fee)