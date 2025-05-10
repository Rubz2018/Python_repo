
class Inventory:
    def __init__(self):
        self.items = {}  # Store items in format: item_name: quantity

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            print(f"{item_name} already exists. Use 'Update Item' to change quantity.")
        else:
            self.items[item_name] = quantity
            print(f"{item_name} added with quantity {quantity}.")

    def update_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] = quantity
            print(f"{item_name} updated to quantity {quantity}.")
        else:
            print(f"{item_name} not found in inventory.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("\n--- Inventory List ---")
            for name, qty in self.items.items():
                print(f"{name}: {qty}")
            print("----------------------")

# Main menu loop
def main():
    inventory = Inventory()

    while True:
        print("\n=== Inventory Menu ===")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            inventory.add_item(name, qty)

        elif choice == '2':
            name = input("Enter item name to update: ")
            qty = int(input("Enter new quantity: "))
            inventory.update_item(name, qty)

        elif choice == '3':
            name = input("Enter item name to remove: ")
            inventory.remove_item(name)

        elif choice == '4':
            inventory.view_inventory()

        elif choice == '5':
            print("Exiting Inventory System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
