from account import Account
from user import User

class Manager(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.accounts = []  # List to store created accounts

    def create_account(self, acc_id, holder_name, balance):
        new_acc = Account(acc_id, holder_name, balance)
        self.accounts.append(new_acc)
        print(f"Account created for {holder_name} with ID {acc_id}")

    def remove_account(self, acc_id):
        self.accounts = [acc for acc in self.accounts if acc.acc_id != acc_id]
        print(f"Account ID {acc_id} removed")

    def display_accounts(self):
        for acc in self.accounts:
            print(acc.display_info())
