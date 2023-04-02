

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Ashish", 5000, 5)
print(account1.title)  
print(account1.balance)  
print(account1.interestRate)  

 
