def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 if the list is empty to avoid division by zero
    return sum(numbers) / len(numbers)

# Example usage
grades = [70, 85, 90, 100]
average_grade = calculate_average(grades)
print("The average is:", average_grade)




def get_number_input():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)  # Convert to float (handles integers and decimals)
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Example usage
if __name__ == "__main__":
    number = get_number_input()
    print(f"You entered: {number}")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create a Rectangle object
rect = Rectangle(5, 3)

# Display the area
print("Area of the rectangle:", rect.area())