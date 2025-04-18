"""Write a function is_square(number) that returns a square of a given number."""

def is_square(number):
    return number * number

print(is_square(5))   # 25
print(is_square(10))  # 100


"""=============================================================================="""
 
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee ID: {self.emp_id} Name: {self.name} Salary: {self.salary}")

emp1 = Employee(101, "Tuhin", 55000)
emp1.display()

 
 
 
"""============================================================================="""
def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error")                   #Division by zero is not allowed.

divide_numbers()

