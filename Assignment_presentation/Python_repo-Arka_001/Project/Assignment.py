class User:
    """Base User class"""
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email
    
    def display_info(self):
        """Display user information - demonstrates polymorphism when overridden"""
        return f"User: {self._name} ({self._email})"


class Customer(User):
    """Customer class inheriting from User"""
    def __init__(self, user_id, name, email, address):
        # Inheritance from parent class
        super().__init__(user_id, name, email)
        self._address = address
        self._orders = []
    
    def display_info(self):
        """Override display_info method - demonstrates polymorphism"""
        return f"Customer: {self._name} ({self._email}) - {self._address}"
    
    def add_order(self, order):
        """Add an order to customer's history"""
        self._orders.append(order)
    
    def get_orders(self):
        """Return customer's orders"""
        return self._orders


class Product:
    """Product class for inventory items"""
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock
    
    def is_available(self, quantity=1):
        """Check if product is available"""
        return self._stock >= quantity
    
    def update_stock(self, quantity_change):
        """Update product stock"""
        new_stock = self._stock + quantity_change
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = new_stock
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def product_id(self):
        return self._product_id


class OrderItem:
    """Item within an order"""
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.item_total = product.price * quantity


class Order:
    """Order class to manage purchases"""
    def __init__(self, order_id, customer):
        self._order_id = order_id
        self._customer = customer
        self._items = []
        self._status = "pending"
        self._total = 0
        
        # Add this order to the customer's orders
        customer.add_order(self)
    
    def add_item(self, product, quantity):
        """Add product to order"""
        if not product.is_available(quantity):
            raise ValueError(f"Not enough stock for {product.name}")
        
        item = OrderItem(product, quantity)
        self._items.append(item)
        self._total += item.item_total
        return item
    
    def confirm_order(self):
        """Process the order by updating stock"""
        for item in self._items:
            # Decrease stock for each product
            item.product.update_stock(-item.quantity)
        
        self._status = "confirmed"
    
    def get_total(self):
        """Get order total"""
        return self._total
    
    def get_status(self):
        """Get order status"""
        return self._status
    
    def display_items(self):
        """Display all items in the order"""
        return "\n".join([f"- {item.quantity}x {item.product.name}: ${item.item_total:.2f}" for item in self._items])


class ECommerceSystem:
    """Main system class - demonstrates abstraction"""
    def __init__(self):
        self._products = {}
        self._customers = {}
        self._orders = {}
        self._next_order_id = 1
    
    def add_product(self, product_id, name, price, stock):
        """Add product to inventory"""
        product = Product(product_id, name, price, stock)
        self._products[product_id] = product
        return product
    
    def add_customer(self, user_id, name, email, address):
        """Register a new customer"""
        customer = Customer(user_id, name, email, address)
        self._customers[user_id] = customer
        return customer
    
    def create_order(self, customer_id):
        """Create a new order"""
        if customer_id not in self._customers:
            raise ValueError("Customer not found")
        
        order_id = self._next_order_id
        self._next_order_id += 1
        
        order = Order(order_id, self._customers[customer_id])
        self._orders[order_id] = order
        return order
    
    def get_product(self, product_id):
        """Get product by ID"""
        if product_id in self._products:
            return self._products[product_id]
        raise ValueError("Product not found")
    
    def get_customer_orders(self, customer_id):
        """Get all orders for a customer"""
        if customer_id not in self._customers:
            raise ValueError("Customer not found")
        return self._customers[customer_id].get_orders()


# Example usage
def run_example():
    # Create system
    system = ECommerceSystem()
    
    # Add products
    laptop = system.add_product(101, "Laptop", 999.99, 5)
    phone = system.add_product(102, "Smartphone", 499.99, 10)
    
    # Add customer
    alice = system.add_customer(1, "Alice Smith", "alice@example.com", "123 Main St")
    
    # Create order
    order = system.create_order(1)
    order.add_item(laptop, 1)
    order.add_item(phone, 2)
    
    # Confirm order
    order.confirm_order()
    
    # Display results
    print(f"Customer: {alice.display_info()}")
    print(f"Order Status: {order.get_status()}")
    print(f"Order Items:\n{order.display_items()}")
    print(f"Order Total: ${order.get_total():.2f}")
    
    # Check updated stock
    print(f"Laptop stock: {laptop._stock}")  # Should be reduced by 1
    print(f"Phone stock: {phone._stock}")    # Should be reduced by 2


if __name__ == "__main__":
    run_example()