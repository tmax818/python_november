class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

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
