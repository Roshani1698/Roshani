## Create a BankAccount class with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.balance=balance
        self.owner=owner

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}, Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{self.owner}, Withdrawn: {amount}, New Balance: {self.balance}")

    def check_balance(self):
        print(f"{self.owner}, Your Balance is : {self.balance}")

acc1 = BankAccount("Roshani", 5000)
acc1.deposit(2000)
acc1.withdraw(2000)
acc1.check_balance()