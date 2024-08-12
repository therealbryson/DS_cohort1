# bank_account.py

class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder
    
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${amount}. Current balance is ${self.account_balance}.")
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.account_balance}.")
        else:
            print("Insufficient funds. Withdrawal canceled.")
    
    def check_balance(self):
        return self.account_balance

# Creating an instance of the Account class
my_account = Account("123456789", 10000.0, "John Doe")

# Testing the methods
print("Initial balance:", my_account.check_balance())

my_account.deposit(5000.0)
my_account.withdraw(7000.0)
my_account.withdraw(1000.0)  # Attempting to withdraw more than available balance

print("Final balance:", my_account.check_balance())
