class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal of {amount} impossible")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(self.balance)

    def __str__(self):
        return f"Name: {self.owner}, Balance: {self.balance}"

a = Account(str(input()), int(input()))

print(a)  

a.deposit(100)  
a.withdraw(100)  

