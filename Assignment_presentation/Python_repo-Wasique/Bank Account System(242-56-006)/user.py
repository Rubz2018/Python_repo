class User:
    def __init__(self, user_id, name):
        self.user_id = user_id  # User ID
        self.name = name  # Name of the user

class Customer(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.my_accounts = []  # Accounts owned by the customer

    def deposit(self, account, amount):
        if amount > 0:
            account.balance += amount
            print(f"{amount:.2f} BDT deposited to Account ID {account.acc_id}")
        else:
            print("Invalid amount.")

    def withdraw(self, account, amount):
        if 0 < amount <= account.balance:
            account.balance -= amount
            print(f"{amount:.2f} BDT withdrawn from Account ID {account.acc_id}")
        else:
            print("Insufficient funds or invalid amount.")
