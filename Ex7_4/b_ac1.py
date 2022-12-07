class BankAccount:
    currency = 'HKD'
    def __init__(self, customer, account_number, balance=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit amount:', amount)

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount:', amount)

    def check_balance(self):
        print('The balance of account number {:d} is {:s}{:.2f}'.format(self.account_number, self.currency, self.balance))