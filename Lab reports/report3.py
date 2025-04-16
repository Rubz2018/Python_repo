# ✅ Class Assignment Problems
# 1. Bank Account Management System

class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is {self.balance}")

# Example usage
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(300)
# 2. Hospital Management System (Inheritance)

# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Doctor class inherits from Person
class Doctor(Person):
    def __init__(self, name, age, gender, speciality, salary):
        super().__init__(name, age, gender)
        self.speciality = speciality
        self.salary = salary

    def show_info(self):
        print(f"Doctor: {self.name}, Speciality: {self.speciality}, Salary: {self.salary}")

# Patient class inherits from Person
class Patient(Person):
    def __init__(self, name, age, gender, disease, fee):
        super().__init__(name, age, gender)
        self.disease = disease
        self.fee = fee

    def show_info(self):
        print(f"Patient: {self.name}, Disease: {self.disease}, Fee: {self.fee}")

# Example usage
doc = Doctor("Dr. John", 45, "Male", "Cardiologist", 100000)
pat = Patient("Emma", 30, "Female", "Flu", 500)

doc.show_info()
pat.show_info()
# ✅ Home Assignment Problems
# 1. Smart Device System

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.status = "Off"

    def turn_on(self):
        self.status = "On"
        print(f"{self.name} is now On")

    def turn_off(self):
        self.status = "Off"
        print(f"{self.name} is now Off")

# Example usage
light = SmartDevice("Living Room Light")
light.turn_on()
light.turn_off()
# 2. Book Management System

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is not available")

    def return_book(self):
        self.available = True
        print(f"You returned '{self.title}'")

# Example usage
book1 = Book("Python Basics", "John Doe")
book1.borrow()
book1.borrow()  # try again
book1.return_book()
# 3. Vehicle Management System (Inheritance)

# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Car class
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def show_info(self):
        super().show_info()
        print(f"Doors: {self.doors}")

# Bike class
class Bike(Vehicle):
    def __init__(self, brand, model, type_bike):
        super().__init__(brand, model)
        self.type_bike = type_bike

    def show_info(self):
        super().show_info()
        print(f"Type: {self.type_bike}")

# Example usage
car1 = Car("Toyota", "Corolla", 4)
bike1 = Bike("Yamaha", "FZ", "Sports")

car1.show_info()
bike1.show_info()