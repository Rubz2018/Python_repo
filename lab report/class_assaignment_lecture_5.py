### 1. Analyzing Sales Data
# scenario: You are given a list of sales transactions. Each transaction contains a sales amount in dollars. You need to:
# Use lambda to define small functions.
# Use filter to extract sales above a threshold.
# Use map to apply a discount to all sales.
# Use reduce to compute the total sales amount.
class Vehicle:
    def __init__(self, make, model, year, color, price):
        """ Base class for all vehicles with common attributes """
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


### 2. Student Grades Processing
#Scenario: Given a list of student scores, filter out passing grades, curve scores, and find the highest score.
from functools import reduce

# Sample student scores (assuming passing grade is 60)
student_scores = [85, 42, 76, 57, 92, 61, 39, 68, 74, 51]

# 1. Filter out passing grades (>= 60)
passing_threshold = 60
passing_scores = list(filter(lambda x: x >= passing_threshold, student_scores))
print(f"Passing scores (≥{passing_threshold}): {passing_scores}")

# 2. Curve scores by adding 5 points to each (without exceeding 100)
curved_scores = list(map(lambda x: min(x + 5, 100), student_scores))
print(f"\nCurved scores (+5 points): {curved_scores}")

# 3. Find the highest score
highest_score = reduce(lambda x, y: x if x > y else y, student_scores)
print(f"\nHighest original score: {highest_score}")

# 4. Bonus: Calculate average score
average_score = reduce(lambda x, y: x + y, student_scores) / len(student_scores)
print(f"\nAverage score: {average_score:.2f}")

# 5. Bonus: Find all scores between 70-90 (B range)
b_range_scores = list(filter(lambda x: 70 <= x <= 90, student_scores))
print(f"\nB range scores (70-90): {b_range_scores}")


### 3. E-commerce Product Price Analysis
# Scenario: You have a list of product prices and need to apply discounts, filter expensive items, and calculate total revenue.
from functools import reduce

# Sample product prices in dollars
product_prices = [45.99, 129.99, 24.50, 89.95, 199.99, 15.25, 59.00, 149.95]

# 1. Apply 15% discount to all products
discounted_prices = list(map(lambda price: round(price * 0.85, 2), product_prices))
print(f"Discounted prices (15% off): {discounted_prices}")

# 2. Filter expensive items (price > $100 after discount)
expensive_threshold = 100.00
expensive_items = list(filter(lambda price: price > expensive_threshold, discounted_prices))
print(f"\nExpensive items (>${expensive_threshold}): {expensive_items}")

# 3. Calculate total revenue from original prices
total_revenue = reduce(lambda x, y: x + y, product_prices)
print(f"\nTotal revenue (original prices): ${total_revenue:.2f}")

# 4. Calculate potential revenue after discount
total_discounted_revenue = reduce(lambda x, y: x + y, discounted_prices)
print(f"Potential revenue (after 15% discount): ${total_discounted_revenue:.2f}")

# 5. Bonus: Count premium products (price > $150 original price)
premium_count = len(list(filter(lambda price: price > 150.00, product_prices)))
print(f"\nNumber of premium products (>$150): {premium_count}")

# 6. Bonus: Find average product price
average_price = total_revenue / len(product_prices)
print(f"Average product price: ${average_price:.2f}")

# 7. Bonus: Apply tiered discount (20% off >$100, 10% off others)
def tiered_discount(price):
    return round(price * 0.8, 2) if price > 100 else round(price * 0.9, 2)

tiered_discounted = list(map(tiered_discount, product_prices))
print(f"\nTiered discounted prices: {tiered_discounted}")

### 4. Word Processing: Sentence Transformation
#Scenario: Given a list of words, filter long words, capitalize all words, and count total characters.

from functools import reduce

# Sample list of words
words = ["python", "is", "an", "excellent", "programming", "language", "for", "data", "analysis"]

# 1. Filter long words (length > 4 characters)
long_words = list(filter(lambda word: len(word) > 4, words))
print(f"Long words (>4 chars): {long_words}")

# 2. Capitalize all words
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(f"\nCapitalized words: {capitalized_words}")

# 3. Count total characters in original list
total_chars = reduce(lambda count, word: count + len(word), words, 0)
print(f"\nTotal characters: {total_chars}")

# 4. Bonus: Filter and capitalize in one step
long_capitalized = [word.capitalize() for word in words if len(word) > 4]
print(f"\nLong and capitalized: {long_capitalized}")

# 5. Bonus: Find the longest word
longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(f"\nLongest word: '{longest_word}' ({len(longest_word)} characters)")

# 6. Bonus: Create a sentence from capitalized words
sentence = " ".join(capitalized_words) + "."
print(f"\nFormatted sentence: {sentence}")

### 5. Employee Salary Processing
#Scenario: Given employee salaries, apply a bonus, filter high earners, and find the highest salary.
from functools import reduce

# Sample employee salaries (in thousands)
salaries = [85, 92, 78, 54, 63, 45, 120, 150, 68, 72]

# 1. Apply 5% bonus to all salaries
bonus_salaries = list(map(lambda salary: round(salary * 1.05, 2), salaries))
print(f"Salaries with 5% bonus: {bonus_salaries}")

# 2. Filter high earners (salary > $100K after bonus)
high_earner_threshold = 100
high_earners = list(filter(lambda salary: salary > high_earner_threshold, bonus_salaries))
print(f"\nHigh earners (>${high_earner_threshold}K): {high_earners}")

# 3. Find the highest salary (original)
highest_salary = reduce(lambda x, y: x if x > y else y, salaries)
print(f"\nHighest original salary: ${highest_salary}K")

# 4. Calculate total salary expenditure (after bonus)
total_salaries = reduce(lambda x, y: x + y, bonus_salaries)
print(f"\nTotal salary expenditure (with bonus): ${total_salaries:.2f}K")

# 5. Bonus: Calculate average salary
average_salary = total_salaries / len(bonus_salaries)
print(f"Average salary (with bonus): ${average_salary:.2f}K")

# 6. Bonus: Apply tiered bonuses (10% for <$60K, 5% for others)
def tiered_bonus(salary):
    return round(salary * 1.10, 2) if salary < 60 else round(salary * 1.05, 2)

tiered_salaries = list(map(tiered_bonus, salaries))
print(f"\nTiered bonus salaries: {tiered_salaries}")

# 7. Bonus: Find salary range
lowest_salary = reduce(lambda x, y: x if x < y else y, salaries)
print(f"\nSalary range: ${lowest_salary}K-${highest_salary}K")

### 6. List of Numbers: Even Filtering and Summation
#Scenario: Given a list of numbers, filter even numbers, square all numbers, and sum them up.
from functools import reduce

# Sample list of numbers
numbers = [12, 7, 24, 15, 8, 19, 32, 5, 11, 18]

# 1. Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 2. Square all numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"\nSquared numbers: {squared_numbers}")

# 3. Sum of all squared numbers
sum_squared = reduce(lambda x, y: x + y, squared_numbers)
print(f"\nSum of squared numbers: {sum_squared}")

# 4. Bonus: Sum of squared even numbers
sum_squared_evens = reduce(lambda x, y: x + y, 
                          map(lambda x: x ** 2, 
                              filter(lambda x: x % 2 == 0, numbers)))
print(f"\nSum of squared even numbers: {sum_squared_evens}")

# 5. Bonus: Combined operation (filter evens, square, then sum)
result = sum(x ** 2 for x in numbers if x % 2 == 0)
print(f"\nPythonic sum of squared evens: {result}")

# 6. Bonus: Count of even numbers
even_count = len(even_numbers)
print(f"\nCount of even numbers: {even_count}")