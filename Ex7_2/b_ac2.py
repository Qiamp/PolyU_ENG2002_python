class BAc2:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        self.loan = 0
        
    
    def setLoan(self, loan):
        loan = loan.replace("HKD", "")
        loan = int(loan)
        if loan <= 0:
            print(f"Invalid loan amount of HKD{loan}.")
        else:
            self.loan += float(loan)
            print(f"A loan of HKD {self.loan} is set up.")
            print(f"The current loan is HKD{self.loan}.")
    
    def retLoan(self, loan):
        loan = loan.replace("HKD", "")
        loan = int(loan)
        if loan <= 0:
            print(f"Invalid return-loan amount of HKD{loan}")
        elif self.loan < loan:
            print("Insufficient funds")
        else:
            self.loan = self.loan - float(loan)
            self.balance = self.balance - float(loan)
            print(f"A loan of HKD{self.loan} is returned.")
            print(f"The current loan is HKD{self.loan}.")
    
    def __str__(self):
        return "The balance of account number " + str(self.accountNumber) + " is HKD" + str(self.balance)