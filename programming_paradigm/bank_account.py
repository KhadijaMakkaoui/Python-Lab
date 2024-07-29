class BankAccount:
    account_balance = 0

    @classmethod
    def __init__(cls, initial_balance=0):
        cls.account_balance = initial_balance
    
    @classmethod
    def deposit(cls, amount):
        if amount > 0:
            cls.account_balance += amount            
    
    @classmethod
    def withdraw(cls, amount):
        if amount > 0:
            if cls.account_balance >= amount:
                cls.account_balance -= amount
                return True
            else:
                return False

    @classmethod
    def display_balance(cls):
        print("Current Balance: $" + str(format(cls.account_balance, ".2f")))