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

    def transfer_money(self, amount, other_user):
        self.make_withdraw(amount)
        other_user.make_deposit(amount)


john = User('John', 'jdog@gmail.com')
john.make_deposit(2000)
troy = User('Troy', 'handsome95@hotmail.com')
john.transfer_money(1000, troy)
print(john.account.balance)
print(troy.account.balance)
