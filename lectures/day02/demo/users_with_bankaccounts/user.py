from bank_account import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	self.account.deposit(amount)
    
    
    def make_withdraw(self, amount):
    	self.account.withdraw(amount)


jahmil = User('Jahmil', 'jdog@aol.com')
