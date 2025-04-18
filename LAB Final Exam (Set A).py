
### 1.# write a python function named calculate_average that accepts 
# a list of numbers and returns the average.
# Use the function to compute the average of [70, 85, 90, 100]

def calculate_average(numbers):
    if not numbers:
        return 0  # Avoid division by zero
    return sum(numbers) / len(numbers)

# Using the function
scores = [70, 85, 90, 100]
average = calculate_average(scores)
print("Average:", average)


### 2. create a class rectangle with attributes length and width. Include:
 ## a constructor to initialize them,
 ## a method area() to calculate and return the area.
## Create an object and display the area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating an object of Rectangle
my_rectangle = Rectangle(10, 5)

# Displaying the area
print("Area of the rectangle:", my_rectangle.area())


### 3. Write a python program that asks the user to enter a number and handle the following exception:
## If the input is not a number, catch the eroor and print "invalid input. Please enter a numeric value"


try:
    user_input = input("Enter a number: ")
    number = float(user_input)  # Convert input to a float (works for both integers and decimals)
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
