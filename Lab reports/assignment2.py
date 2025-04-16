# ✅ 1. Analyzing Sales Data

from functools import reduce

sales = [120, 75, 300, 450, 80, 150]

# 1. Filter sales above threshold (e.g., $100)
high_sales = list(filter(lambda x: x > 100, sales))
print("Sales > $100:", high_sales)

# 2. Apply 10% discount to all sales
discounted_sales = list(map(lambda x: x * 0.9, sales))
print("Discounted sales:", discounted_sales)

# 3. Compute total sales
total_sales = reduce(lambda x, y: x + y, sales)
print("Total sales amount:", total_sales)
# ✅ 2. Student Grades Processing

from functools import reduce

scores = [45, 78, 88, 59, 92, 30, 66]

# 1. Filter passing grades (pass mark = 60)
passing = list(filter(lambda x: x >= 60, scores))
print("Passing grades:", passing)

# 2. Curve scores by adding 5 points
curved = list(map(lambda x: x + 5, scores))
print("Curved scores:", curved)

# 3. Find highest score
highest = reduce(lambda x, y: x if x > y else y, scores)
print("Highest score:", highest)
# ✅ 3. E-commerce Product Price Analysis

from functools import reduce

prices = [250, 100, 499, 50, 700, 120]

# 1. Apply 20% discount to all
discounted = list(map(lambda x: x * 0.8, prices))
print("Discounted prices:", discounted)

# 2. Filter expensive items (above 300 after discount)
expensive = list(filter(lambda x: x > 300, discounted))
print("Expensive items:", expensive)

# 3. Calculate total revenue
total_revenue = reduce(lambda x, y: x + y, discounted)
print("Total revenue:", total_revenue)
# ✅ 4. Word Processing: Sentence Transformation

from functools import reduce

words = ["python", "is", "powerful", "and", "flexible"]

# 1. Filter words longer than 5 characters
long_words = list(filter(lambda w: len(w) > 5, words))
print("Long words:", long_words)

# 2. Capitalize all words
capitalized = list(map(lambda w: w.capitalize(), words))
print("Capitalized:", capitalized)

# 3. Count total characters in all words
total_chars = reduce(lambda x, y: x + len(y), words, 0)
print("Total characters:", total_chars)
# ✅ 5. Employee Salary Processing

from functools import reduce

salaries = [3000, 4500, 6000, 2800, 7500]

# 1. Apply 10% bonus
bonus_salaries = list(map(lambda s: s * 1.1, salaries))
print("With bonus:", bonus_salaries)

# 2. Filter high earners (above $5000)
high_earners = list(filter(lambda s: s > 5000, bonus_salaries))
print("High earners:", high_earners)

# 3. Find the highest salary
highest_salary = reduce(lambda x, y: x if x > y else y, bonus_salaries)
print("Highest salary:", highest_salary)
# ✅ 6. List of Numbers: Even Filtering and Summation

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# 2. Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)

# 3. Sum all squared numbers
total_sum = reduce(lambda x, y: x + y, squared)
print("Sum of squares:", total_sum)
