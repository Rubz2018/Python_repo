# account.py

class Account:
    def __init__(self, acc_id, holder_name, balance):
        self.acc_id = acc_id  # Unique account ID
        self.holder_name = holder_name  # Name of account holder
        self.balance = balance  # Initial balance

    def display_info(self):
        return f"Account ID: {self.acc_id}, Holder: {self.holder_name}, Balance: ${self.balance:.2f}"
