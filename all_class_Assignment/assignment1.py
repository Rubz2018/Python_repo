# ✅ Looping Through Dictionary

# Sample dictionary
my_dict = {'a': 10, 'b': 25, 'c': 15, 'd': 5}

# 1. Loop through a dictionary and print each key and value
for key, value in my_dict.items():
    print(key, ":", value)

# 2. Find and print all keys that have values greater than a given number
threshold = 10
for key, value in my_dict.items():
    if value > threshold:
        print(f"Key with value > {threshold}:", key)

# 3. Count the occurrences of each value in a dictionary
from collections import Counter
value_count = Counter(my_dict.values())
print("Value occurrences:", value_count)

# 4. Filter out dictionary items where values are less than a threshold
filtered_dict = {k: v for k, v in my_dict.items() if v >= threshold}
print("Filtered dictionary:", filtered_dict)

# 5. Print dictionary items in sorted order of their keys
for key in sorted(my_dict):
    print(f"{key}: {my_dict[key]}")
# ✅ String Slicing & Iteration

text = "HelloWorldPython"

# 1. Extract the first 5 and last 5 characters
print("First 5:", text[:5])
print("Last 5:", text[-5:])

# 2. Remove every alternate character
print("Alternate characters removed:", text[::2])

# 3. Extract the substring from index 2 to 7
print("Substring (2 to 7):", text[2:8])

# 4. Iterate through a string and print each character
for char in text:
    print(char)

# 5. Reverse a string using slicing
print("Reversed string:", text[::-1])
# ✅ String Strip Functions

sample = "   Hello World   "
special = "###Welcome###"

# 1. Remove leading spaces
print("No leading space:", sample.lstrip())

# 2. Remove trailing spaces
print("No trailing space:", sample.rstrip())

# 3. Strip both leading and trailing spaces
print("Stripped:", sample.strip())

# 4. Remove specific characters (#) from the start
print("Remove #: start:", special.lstrip('#'))

# 5. Remove specific characters (#) from the end
print("Remove #: end:", special.rstrip('#'))

# 6. List comprehension: squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares 1 to 10:", squares)

# 7. List comprehension: even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers:", evens)
# ✅ List Operations (Homework)

nums = [10, 20, 30, 40, 50, 60, 70]

# 1. Slice to extract first 3 and last 3 elements
print("First 3:", nums[:3])
print("Last 3:", nums[-3:])

# 2. Add, remove, and change an item
nums.append(80)
print("After append:", nums)
nums.remove(40)
print("After remove:", nums)
nums[2] = 99
print("After change:", nums)

# 3. Copy a list and modify
copy_nums = nums.copy()
copy_nums[0] = 100
print("Original list:", nums)
print("Modified copy:", copy_nums)

# 4. Join a list into sentence
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Sentence:", sentence)

# 5. Iterate through list
for item in nums:
    print("Element:", item)

# 6. Print only even numbers
evens = [x for x in nums if x % 2 == 0]
print("Even numbers:", evens)

# 7. Use all() to check if all numbers are positive
print("All positive:", all(x > 0 for x in nums))

# 8. Use any() to check if any number > 50
print("Any > 50:", any(x > 50 for x in nums))

# 9. all() and any() for strings
names = ["apple", "banana", "apricot"]
print("All start with a:", all(name.startswith("a") for name in names))
print("Any ends with e:", any(name.endswith("e") for name in names))
# ✅ Built-in Functions

numbers = [4, 9, 16, 25, 36]

# 1. min, max, length, and sum
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Length:", len(numbers))
print("Sum:", sum(numbers))

# 2. Find the longest word
words = ["apple", "banana", "cherry", "grapefruit"]
longest = max(words, key=len)
print("Longest word:", longest)

# 3. Sum of even numbers
even_sum = sum(x for x in numbers if x % 2 == 0)
print("Sum of evens:", even_sum)

# 4. Shortest string
shortest = min(words, key=len)
print("Shortest word:", shortest)

# 5. Sort list of tuples by second element
pairs = [(1, 3), (2, 1), (5, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted tuples:", sorted_pairs)
# ✅ Dictionary Operations

student = {"name": "Alice", "age": 22}

# 1. Access an item by key
print("Name:", student["name"])

# 2. Add new key-value
student["grade"] = "A"
print("Updated dict:", student)

# 3. Remove an item
del student["age"]
print("After removal:", student)

# 4. Copy dictionary and modify
copy_student = student.copy()
copy_student["name"] = "Bob"
print("Original:", student)
print("Modified copy:", copy_student)

# 5. Loop through and print
for key, value in student.items():
    print(key, "->", value)