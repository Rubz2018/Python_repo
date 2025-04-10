import json
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []  # All accounts in the bank
        self.load_data()

    def load_data(self):
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
                for acc in data:
                    self.accounts.append(Account(**acc))  # Unpack JSON data into Account object
        except FileNotFoundError:
            pass  # If file not found, start with empty list

    def save_data(self):
        with open("accounts.json", "w") as file:
            json.dump([acc.__dict__ for acc in self.accounts], file)  # Convert objects to dict

    def find_account(self, acc_id):
        return next((acc for acc in self.accounts if acc.acc_id == acc_id), None)  # Search account by ID
