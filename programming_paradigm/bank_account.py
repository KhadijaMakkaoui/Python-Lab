class BankAccount:
    def __init__(self,initial_balance=0):
        self.account_balance=initial_balance
    def deposit(amount):
        if amount>0:
            account_balance+= amount            
    
    def withdraw(amount):
        if amount > 0:
            if account_balance >= amount:
                account_balance -= amount
                return True
            else:
                return False
           
                


    def display_balance():
        print("Current Balance: $"+str(format(account_balance, ".2f")))

        