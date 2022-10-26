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
        
    def display_user_balance(self):
        self.account.display_account_info()
    
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.make_deposit(amount)


jahmil = User('Jahmil', 'jdog@aol.com')
jahmil.make_deposit(10000)
roy = User('roy', 'roydog@aol.com')
ryan = User('ryan', 'rydog@aol.com')
jahmil.transfer_money(1000, ryan)
