class BankAccount:
    
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        print(self)

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You don't have the money, Bro!!!")
            self.balance -= 5
    
    def display_account_info(self):
        print(f" Your balance is: ${self.balance}")
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(f"balance: {account.balance}, interest rate: {account.int_rate}")
