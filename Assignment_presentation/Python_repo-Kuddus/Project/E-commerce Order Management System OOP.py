#E-commerce Order Management System (OOP Python with User Inheritance)
#Md. Tanjim Mahmud Tuhin
#251-56-12

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []
    
    def place_order(self, order):
        self.orders.append(order)
    
    def get_order_history(self):
        return self.orders
    
    def __str__(self):
        return f"{self.user_id}: {self.name} ({self.email})"

class Customer(User):
    def __init__(self, user_id, name, email, shipping_address):
        super().__init__(user_id, name, email)
        self.shipping_address = shipping_address
        self.loyalty_points = 0
    
    def update_shipping_address(self, new_address):
        self.shipping_address = new_address
    
    def add_loyalty_points(self, points):
        self.loyalty_points += points
    
    def __str__(self):
        return f"{super().__str__()}\nShipping Address: {self.shipping_address}\nLoyalty Points: {self.loyalty_points}"

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def __str__(self):
        return f"{self.product_id}: {self.name} - ${self.price} (Qty: {self.quantity})"

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ${self.get_total():.2f}"

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.status = "Pending"
        self.order_date = "2023-11-15"  # In real implementation, use datetime.now()
    
    def add_item(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append(OrderItem(product, quantity))
            product.quantity -= quantity
            return True
        else:
            print(f"Not enough stock for {product.name}")
            return False
    
    def get_total(self):
        return sum(item.get_total() for item in self.items)
    
    def update_status(self, new_status):
        self.status = new_status
        if new_status == "Completed":
            self.customer.add_loyalty_points(int(self.get_total() / 10))  # 1 point per $10
    
    def __str__(self):
        order_details = [
            f"Order ID: {self.order_id}",
            f"Customer: {self.customer.name}",
            f"Date: {self.order_date}",
            f"Status: {self.status}",
            "Items:"
        ]
        for item in self.items:
            order_details.append(f"  - {item}")
        order_details.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(order_details)

class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        self.products[product.product_id] = product
    
    def get_product(self, product_id):
        return self.products.get(product_id)
    
    def list_products(self):
        for product in self.products.values():
            print(product)

# Sample usage
if __name__ == "__main__":
    # Create inventory
    inventory = Inventory()
    inventory.add_product(Product("P100", "Laptop", 999.99, 10))
    inventory.add_product(Product("P101", "Mouse", 19.99, 50))
    inventory.add_product(Product("P102", "Keyboard", 49.99, 30))
    
    # Create a customer
    customer = Customer("C100", "John Doe", "john@example.com", "123 Main St, Anytown")
    
    # Create a new order
    order1 = Order("ORD-001", customer)
    
    # Add items to order
    order1.add_item(inventory.get_product("P100"), 1)
    order1.add_item(inventory.get_product("P101"), 2)
    
    # Update order status to completed
    order1.update_status("Completed")
    
    # Customer places the order
    customer.place_order(order1)
    
    # Display order details
    print("=== Order Details ===")
    print(order1)
    
    # Display customer information
    print("\n=== Customer Information ===")
    print(customer)
    
    # Display inventory after order
    print("\n=== Updated Inventory ===")
    inventory.list_products()
    
    # Display customer's order history
    print("\n=== Customer Order History ===")
    for order in customer.get_order_history():
        print(order)
        print("-" * 30)