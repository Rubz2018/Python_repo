### Class Assignment Problems:
##1. "Bank Account Management System where we create a BankAccount class that allows a user to deposit and withdraw money. Possible variables are account_name, balance"

class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        """Initialize a bank account with account name and optional initial balance"""
        self.account_name = account_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def __str__(self):
        """String representation of the account"""
        return f"Account Name: {self.account_name}, Balance: ₹{self.balance:.2f}"


# Demonstration of the BankAccount class
if __name__ == "__main__":
    # Create a new account
    account = BankAccount("John Doe", 1000)
    print(account)
    
    # Make deposits
    account.deposit(500)
    account.deposit(250.75)
    
    # Make withdrawals
    account.withdraw(300)
    account.withdraw(1500)  # Should show insufficient funds
    
    # Try invalid operations
    account.deposit(-100)  # Invalid deposit
    account.withdraw(-50)  # Invalid withdrawal
    
    # Check final balance
    print(f"\nFinal account status: {account}")
    print(f"Current balance: ₹{account.get_balance():.2f}")


##2. ("Hospital Management System :  This system has a base class Person and two subclasses: Doctor and Patient that inherit attributes and define additional ones.Base/parent class (Person) attributes : name , age, genderPerson/sub class Doctor attributes : name,age, gender, speciality, salaryPerson/sub class Patient attributes : name,age, gender, Disease, Fee)"

class Person:
    def __init__(self, name, age, gender):
        """Base class for all people in the hospital system"""
        self.name = name
        self.age = age
        self.gender = gender
    
    def display_info(self):
        """Display basic information about the person"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Doctor(Person):
    def __init__(self, name, age, gender, specialty, salary):
        """Doctor subclass with additional medical professional attributes"""
        super().__init__(name, age, gender)
        self.specialty = specialty
        self.salary = salary
    
    def display_info(self):
        """Display doctor's information"""
        super().display_info()
        print(f"Specialty: {self.specialty}")
        print(f"Salary: ₹{self.salary:,.2f}")


class Patient(Person):
    def __init__(self, name, age, gender, disease, fee):
        """Patient subclass with medical treatment attributes"""
        super().__init__(name, age, gender)
        self.disease = disease
        self.fee = fee
    
    def display_info(self):
        """Display patient's information"""
        super().display_info()
        print(f"Disease: {self.disease}")
        print(f"Treatment Fee: ₹{self.fee:,.2f}")


# Demonstration of the Hospital Management System
if __name__ == "__main__":
    print("\nHospital Management System\n")
    
    # Create some doctors
    dr_sharma = Doctor("Dr. Amit Sharma", 45, "Male", "Cardiology", 250000)
    dr_patel = Doctor("Dr. Priya Patel", 38, "Female", "Pediatrics", 180000)
    
    # Create some patients
    patient1 = Patient("Rahul Verma", 32, "Male", "Hypertension", 5000)
    patient2 = Patient("Neha Gupta", 27, "Female", "Asthma", 3500)
    
    # Display information
    print("\nDoctors:")
    dr_sharma.display_info()
    print("\n" + "-"*40)
    dr_patel.display_info()
    
    print("\nPatients:")
    patient1.display_info()
    print("\n" + "-"*40)
    patient2.display_info()

    
### Home Assignemnt
##1. A system where a SmartDevice class represents a smart home device (like a light bulb) that can be turned on or off.
class SmartDevice:
    def __init__(self, device_name, device_type="Generic Smart Device"):
        """Initialize a smart home device"""
        self.device_name = device_name
        self.device_type = device_type
        self.is_on = False  # Default state is off
        self.brightness = 0  # For devices that support brightness (0-100)
    
    def turn_on(self):
        """Turn the device on"""
        if not self.is_on:
            self.is_on = True
            self.brightness = 50  # Default brightness when turned on
            print(f"{self.device_name} is now ON")
        else:
            print(f"{self.device_name} is already ON")
    
    def turn_off(self):
        """Turn the device off"""
        if self.is_on:
            self.is_on = False
            self.brightness = 0
            print(f"{self.device_name} is now OFF")
        else:
            print(f"{self.device_name} is already OFF")
    
    def set_brightness(self, level):
        """Set brightness level (0-100)"""
        if self.is_on:
            if 0 <= level <= 100:
                self.brightness = level
                print(f"{self.device_name} brightness set to {level}%")
            else:
                print("Brightness must be between 0 and 100")
        else:
            print(f"Cannot set brightness - {self.device_name} is OFF")
    
    def toggle(self):
        """Toggle the device state (on/off)"""
        if self.is_on:
            self.turn_off()
        else:
            self.turn_on()
    
    def status(self):
        """Return the current status of the device"""
        state = "ON" if self.is_on else "OFF"
        return {
            "device_name": self.device_name,
            "device_type": self.device_type,
            "state": state,
            "brightness": self.brightness
        }
    
    def __str__(self):
        """String representation of the device"""
        state = "ON" if self.is_on else "OFF"
        return (f"{self.device_type}: {self.device_name} "
                f"(State: {state}, Brightness: {self.brightness}%)")


# Subclass for specific device types
class SmartLight(SmartDevice):
    def __init__(self, device_name):
        """Smart light subclass"""
        super().__init__(device_name, "Smart Light")
        self.color = "white"  # Default color
    
    def set_color(self, color):
        """Set light color"""
        if self.is_on:
            self.color = color.lower()
            print(f"{self.device_name} color changed to {self.color}")
        else:
            print(f"Cannot set color - {self.device_name} is OFF")
    
    def status(self):
        """Return status including color"""
        base_status = super().status()
        base_status["color"] = self.color
        return base_status


# Demonstration of the SmartDevice system
if __name__ == "__main__":
    print("\nSmart Home Device System\n")
    
    # Create some devices
    living_room_light = SmartLight("Living Room Light")
    bedroom_light = SmartLight("Bedroom Light")
    generic_device = SmartDevice("Smart Plug")
    
    # Test operations
    living_room_light.turn_on()
    living_room_light.set_brightness(75)
    living_room_light.set_color("warm white")
    
    bedroom_light.toggle()  # Turns on
    bedroom_light.toggle()  # Turns off
    
    generic_device.turn_on()
    generic_device.turn_off()
    
    # Print status
    print("\nDevice Status:")
    print(living_room_light)
    print(bedroom_light)
    print(generic_device)
    
    # Show detailed status
    print("\nLiving Room Light Details:")
    for key, value in living_room_light.status().items():
        print(f"{key.title()}: {value}")

###2. A system where a Book class manages book information and checks if a book is available for borrowing.

class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        """
        Initialize a book with:
        - title: Book title
        - author: Author name
        - isbn: International Standard Book Number
        - total_copies: Total copies available (default 1)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.borrowed_copies = 0
    
    def borrow(self):
        """Borrow a copy of the book if available"""
        if self.is_available():
            self.borrowed_copies += 1
            return True
        return False
    
    def return_book(self):
        """Return a borrowed copy of the book"""
        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1
            return True
        return False
    
    def is_available(self):
        """Check if any copies are available for borrowing"""
        return self.borrowed_copies < self.total_copies
    
    def available_copies(self):
        """Get the number of available copies"""
        return self.total_copies - self.borrowed_copies
    
    def __str__(self):
        """String representation of the book"""
        status = "Available" if self.is_available() else "Checked Out"
        return (f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - "
                f"{status} ({self.available_copies()}/{self.total_copies} copies)")
    
    def get_details(self):
        """Get complete book details as a dictionary"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "total_copies": self.total_copies,
            "borrowed_copies": self.borrowed_copies,
            "available_copies": self.available_copies(),
            "is_available": self.is_available()
        }


# Library class to manage multiple books
class Library:
    def __init__(self):
        """Initialize a library to manage books"""
        self.books = {}
    
    def add_book(self, book):
        """Add a book to the library"""
        if book.isbn in self.books:
            # If book already exists, increase the total copies
            self.books[book.isbn].total_copies += book.total_copies
        else:
            self.books[book.isbn] = book
    
    def find_book(self, isbn):
        """Find a book by ISBN"""
        return self.books.get(isbn)
    
    def borrow_book(self, isbn):
        """Borrow a book by ISBN"""
        book = self.find_book(isbn)
        if book and book.borrow():
            return True
        return False
    
    def return_book(self, isbn):
        """Return a book by ISBN"""
        book = self.find_book(isbn)
        if book and book.return_book():
            return True
        return False
    
    def list_books(self):
        """List all books in the library"""
        for isbn, book in self.books.items():
            print(book)


# Demonstration of the Book Management System
if __name__ == "__main__":
    print("\nBook Management System\n")
    
    # Create a library
    my_library = Library()
    
    # Add some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 2)
    book3 = Book("1984", "George Orwell", "9780451524935", 1)
    
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    
    # Display all books
    print("Library Catalog:")
    my_library.list_books()
    
    # Test borrowing and returning
    print("\nBorrowing '1984':")
    if my_library.borrow_book("9780451524935"):
        print("Successfully borrowed '1984'")
    else:
        print("Could not borrow '1984'")
    
    print("\nAttempting to borrow '1984' again:")
    if my_library.borrow_book("9780451524935"):
        print("Successfully borrowed '1984'")
    else:
        print("Could not borrow '1984' - no available copies")
    
    print("\nReturning '1984':")
    if my_library.return_book("9780451524935"):
        print("Successfully returned '1984'")
    
    # Show updated status
    print("\nUpdated Library Catalog:")
    my_library.list_books()
    
    # Show detailed information for one book
    print("\nDetailed information for 'The Great Gatsby':")
    gatsby = my_library.find_book("9780743273565")
    for key, value in gatsby.get_details().items():
        print(f"{key.replace('_', ' ').title()}: {value}")

        
    ### A system where a Book class manages book information and checks if a book is available for borrowing.#$$
class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        """
        Initialize a Book object with title, author, ISBN, and total copies available.
        By default, total_copies is 1 if not specified.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.borrowed_copies = 0  # Initially no copies are borrowed
    
    def is_available(self):
        """
        Check if the book is available for borrowing.
        Returns True if at least one copy is available, False otherwise.
        """
        return self.borrowed_copies < self.total_copies
    
    def borrow_book(self):
        """
        Borrow a copy of the book if available.
        Returns True if successful, False if no copies available.
        """
        if self.is_available():
            self.borrowed_copies += 1
            return True
        return False
    
    def return_book(self):
        """
        Return a borrowed copy of the book.
        Returns True if successful, False if no copies are currently borrowed.
        """
        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1
            return True
        return False
    
    def available_copies(self):
        """
        Get the number of available copies.
        """
        return self.total_copies - self.borrowed_copies
    
    def __str__(self):
        """
        String representation of the book.
        """
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - " \
               f"Available: {self.available_copies()}/{self.total_copies}"


# Example usage
if __name__ == "__main__":
    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 3)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    
    # Display book information
    print(book1)
    print(book2)
    
    # Borrow some books
    print("\nBorrowing books:")
    print(f"Borrowing book1: {'Success' if book1.borrow_book() else 'Failed'}")
    print(f"Borrowing book2: {'Success' if book2.borrow_book() else 'Failed'}")
    print(f"Borrowing book2 again: {'Success' if book2.borrow_book() else 'Failed'}")  # Should fail
    
    # Check availability
    print("\nAvailability:")
    print(f"Is book1 available? {'Yes' if book1.is_available() else 'No'}")
    print(f"Is book2 available? {'Yes' if book2.is_available() else 'No'}")
    
    # Return a book
    print("\nReturning book2:")
    print(f"Returning book2: {'Success' if book2.return_book() else 'Failed'}")
    print(f"Is book2 now available? {'Yes' if book2.is_available() else 'No'}")
    
    # Final status
    print("\nFinal status:")
    print(book1)
    print(book2)

## Vehicle Management System: This system has a base class Vehicle and two subclasses: Car and Bike that inherit common attributes and define additional ones.
class Vehicle:
    def __init__(self, make, model, year, color, price):
        """
        Base class for all vehicles with common attributes
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.mileage = 0
        self.is_available = True
    
    def display_info(self):
        """Display basic vehicle information"""
        info = (
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Year: {self.year}\n"
            f"Color: {self.color}\n"
            f"Price: ${self.price:,.2f}\n"
            f"Mileage: {self.mileage} miles\n"
            f"Available: {'Yes' if self.is_available else 'No'}"
        )
        return info
    
    def update_mileage(self, new_mileage):
        """Update the vehicle's mileage"""
        if new_mileage >= self.mileage:
            self.mileage = new_mileage
        else:
            print("Warning: Mileage cannot be decreased!")
    
    def sell(self):
        """Mark the vehicle as sold"""
        if self.is_available:
            self.is_available = False
            print(f"{self.make} {self.model} has been sold.")
        else:
            print("Vehicle is already sold!")
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, color, price, num_doors, fuel_type):
        """
        Car subclass with additional car-specific attributes
        """
        super().__init__(make, model, year, color, price)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
        self.trunk_capacity = None  # in cubic feet
    
    def set_trunk_capacity(self, capacity):
        """Set the trunk capacity"""
        self.trunk_capacity = capacity
    
    def display_info(self):
        """Display car information including specific attributes"""
        base_info = super().display_info()
        car_info = (
            f"\nVehicle Type: Car\n"
            f"Number of Doors: {self.num_doors}\n"
            f"Fuel Type: {self.fuel_type}\n"
            f"Trunk Capacity: {self.trunk_capacity if self.trunk_capacity else 'Not specified'} cubic feet"
        )
        return base_info + car_info


class Bike(Vehicle):
    def __init__(self, make, model, year, color, price, bike_type, frame_size):
        """
        Bike subclass with additional bike-specific attributes
        """
        super().__init__(make, model, year, color, price)
        self.bike_type = bike_type  # e.g., Road, Mountain, Hybrid
        self.frame_size = frame_size  # in inches
        self.has_basket = False
    
    def add_basket(self):
        """Add a basket to the bike"""
        self.has_basket = True
        print("Basket added to the bike.")
    
    def display_info(self):
        """Display bike information including specific attributes"""
        base_info = super().display_info()
        bike_info = (
            f"\nVehicle Type: Bike\n"
            f"Bike Type: {self.bike_type}\n"
            f"Frame Size: {self.frame_size} inches\n"
            f"Has Basket: {'Yes' if self.has_basket else 'No'}"
        )
        return base_info + bike_info


# Example usage
if __name__ == "__main__":
    print("=== Vehicle Management System ===")
    
    # Create a car
    car1 = Car("Toyota", "Camry", 2022, "Blue", 25000, 4, "Hybrid")
    car1.set_trunk_capacity(15.1)
    
    # Create a bike
    bike1 = Bike("Trek", "FX 2", 2023, "Black", 799, "Hybrid", 19)
    bike1.add_basket()
    
    # Display vehicle information
    print("\n=== Car Information ===")
    print(car1.display_info())
    
    print("\n=== Bike Information ===")
    print(bike1.display_info())
    
    # Test vehicle methods
    print("\n=== Testing Vehicle Operations ===")
    car1.update_mileage(1500)
    print(f"\nUpdated mileage for {car1}: {car1.mileage} miles")
    
    print("\nAttempting to sell the car:")
    car1.sell()
    car1.sell()  # Second attempt should show already sold
    
    print("\nUpdated car info after selling:")
    print(car1.display_info())