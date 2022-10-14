
class BankAccount:

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f"You just lost $5, Bro! Nice try! Your balance is now {self.display_account_info()}.")


    def display_account_info(self):
        print(f"Your balance is: {self.balance}")
        return self.balance


    def yield_interest(self):
        self.balance += self.balance * self.int_rate

checking = BankAccount()
savings = BankAccount(.1, 200000)

checking.deposit(1000)
checking.yield_interest()

print(checking.balance)