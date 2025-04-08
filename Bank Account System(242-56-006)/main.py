# main.py

from manager import Manager
from user import Customer
from bank import Bank

# Initialize bank system
bank = Bank()
manager = Manager(1, "Mr. Digonta")

# Manager creates accounts
manager.create_account(1001, "Wasique", 500.0)
manager.create_account(1002, "Azad", 300.0)

# Display all accounts
manager.display_accounts()

# Customer performs actions
customer = Customer(201, "Wasique")
account = bank.find_account(1001)  # Find Wasique's account from bank

if account:
    customer.deposit(account, 200)
    customer.withdraw(account, 100)
else:
    print("Account not found!")

print(f"The final balance of {account.acc_id}:{account.holder_name} is ${account.balance}")
# Save updated data
bank.accounts = manager.accounts  # Sync created accounts to bank system
bank.save_data()
