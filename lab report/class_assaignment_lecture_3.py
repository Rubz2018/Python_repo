###### Looping Through Dictionary
##Loop through a dictionary and print each key and value.
my_dict = {'a': 10, 'b': 20, 'c': 30}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

## Find and print all keys that have values greater than a given number.
def keys_with_values_greater_than(dictionary, threshold):
    return [key for key, value in dictionary.items() if value > threshold]

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 5}
threshold = 15
result = keys_with_values_greater_than(my_dict, threshold)
print(f"Keys with values > {threshold}: {result}")

## Count the occurrences of each value in a dictionary.
from collections import defaultdict

def count_value_occurrences(dictionary):
    counts = defaultdict(int)
    for value in dictionary.values():
        counts[value] += 1
    return dict(counts)

my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
value_counts = count_value_occurrences(my_dict)
print("Value occurrences:", value_counts)


##Filter out dictionary items where values are less than a threshold.
def filter_dict_by_value(dictionary, threshold):
    return {key: value for key, value in dictionary.items() if value >= threshold}

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 5}
threshold = 15
filtered_dict = filter_dict_by_value(my_dict, threshold)
print(f"Dictionary after filtering values < {threshold}:", filtered_dict)

##Print dictionary items in sorted order of their keys.
my_dict = {'c': 30, 'a': 10, 'b': 20, 'e': 50, 'd': 40}

print("Dictionary items sorted by key:")
for key in sorted(my_dict.keys()):
    print(f"{key}: {my_dict[key]}")
### String Slicing & Iteration
## Extract the first 5 and last 5 characters from a given string.
def extract_first_last_5(text):
    first_5 = text[:5]
    last_5 = text[-5:]
    return first_5, last_5

sample_text = "HelloWorldPythonProgramming"
first, last = extract_first_last_5(sample_text)
print(f"First 5: {first}, Last 5: {last}")

## Remove every alternate character from a string.
def remove_alternate_chars(text):
    return text[::2]

sample_text = "abcdefghijklmnop"
result = remove_alternate_chars(sample_text)
print("After removing alternate characters:", result)

## Extract the substring from index 2 to 7.
def extract_substring(text):
    return text[2:8]  # Note: end index is exclusive, so 8 to get up to 7

sample_text = "PythonProgramming"
substring = extract_substring(sample_text)
print("Substring from index 2 to 7:", substring)

## Iterate through a string and print each character.
def print_each_char(text):
    for char in text:
        print(char)

sample_text = "Hello"
print("Printing each character:")
print_each_char(sample_text)

## Reverse a string using slicing.
def reverse_string(text):
    return text[::-1]

sample_text = "Python"
reversed_text = reverse_string(sample_text)
print(f"Original: {sample_text}, Reversed: {reversed_text}")

### String Strip Functions
##Remove leading spaces using lstrip().
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"After lstrip(): '{text.lstrip()}'")

##Remove trailing spaces using rstrip().
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"After rstrip(): '{text.rstrip()}'")

##Strip both leading and trailing spaces from a string.
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"After strip(): '{text.strip()}'")

##Remove specific characters (e.g., #) from the start of a string.
text = "###Hello World"
print(f"Original: '{text}'")
print(f"After lstrip('#'): '{text.lstrip('#')}'")

##Remove specific characters from the end of a string.
text = "Hello World!!!"
print(f"Original: '{text}'")
print(f"After rstrip('!'): '{text.rstrip('!')}'")

## Using List comprehension Generate a list of squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

## Using List Comprehension Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", evens)


### List Operations
## Slice a list to extract the first 3 and last 3 elements.
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
first_3 = my_list[:3]
last_3 = my_list[-3:]
print("First 3 elements:", first_3)
print("Last 3 elements:", last_3)

## Add an item to a list, remove an item, and change an item at a given index.
my_list = ['apple', 'banana', 'cherry']

# Add an item
my_list.append('date')
print("After append:", my_list)

# Remove an item
my_list.remove('banana')
print("After remove:", my_list)

# Change item at index
my_list[1] = 'blueberry'
print("After modification:", my_list)

## Copy a list and verify that modifying the copy does not affect the original.
original = [1, 2, 3]
copy = original.copy()

copy.append(4)
print("Original:", original)
print("Copy:", copy)
print("Are they the same object?", original is copy)

## Join a list of words into a sentence using .join().
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print("Joined sentence:", sentence)

## Iterate through a list and print each element.
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

## Print only the even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in numbers if num % 2 == 0]
print("Even numbers:", evens)

## Use all() to check if all numbers in a list are positive.
numbers = [5, 10, 15, 20]
all_positive = all(num > 0 for num in numbers)
print("All positive?", all_positive)

## Use any() to check if any number in a list is greater than 50.
numbers = [25, 30, 45, 60, 15]
any_gt_50 = any(num > 50 for num in numbers)
print("Any > 50?", any_gt_50)

## Use all() and any() to check conditions in a list of strings.
words = ['apple', 'banana', 'avocado', 'apricot']

# Check if all start with 'a'
all_start_a = all(word.startswith('a') for word in words)
print("All start with 'a'?", all_start_a)

# Check if any contains 'nana'
any_has_nana = any('nana' in word for word in words)
print("Any contains 'nana'?", any_has_nana)


### Built-in Functions
## Find the minimum, maximum, length, and sum of a list.
numbers = [15, 23, 8, 42, 4, 16]

# Find minimum, maximum, length, and sum
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Length:", len(numbers))
print("Sum:", sum(numbers))

## Find the longest word in a list of words.
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Method 1: Using max() with key parameter
longest_word = max(words, key=len)
print("Longest word:", longest_word)

# Method 2: Using list comprehension
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Longest words:", longest_words)

## Compute the sum of even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using sum() with generator expression
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)

## Find the shortest string in a list.
words = ["cat", "dog", "elephant", "bee", "ant"]

# Method 1: Using min() with key parameter
shortest_word = min(words, key=len)
print("Shortest word:", shortest_word)

# Method 2: Using list comprehension
min_length = min(len(word) for word in words)
shortest_words = [word for word in words if len(word) == min_length]
print("Shortest words:", shortest_words)

## Sort a list of tuples based on the second element.
tuples = [("apple", 3), ("banana", 1), ("cherry", 2), ("date", 4)]

# Method 1: Using sorted() with key parameter
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print("Sorted by second element:", sorted_tuples)

# Method 2: Using itemgetter
from operator import itemgetter
sorted_tuples = sorted(tuples, key=itemgetter(1))
print("Sorted using itemgetter:", sorted_tuples)



### Dictionary Operations
## Access an item in a dictionary by key.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])  # Using square brackets
print("Age:", my_dict.get('age'))  # Using get() method

# Handling missing keys
print("Occupation:", my_dict.get('occupation', 'Not specified'))  # Default value

## Add a new key-value pair to a dictionary.
my_dict = {'name': 'Alice', 'age': 25}

# Adding new items
my_dict['city'] = 'New York'  # Add new key-value
my_dict.update({'occupation': 'Engineer', 'hobby': 'Reading'})  # Multiple items

print("Updated dictionary:", my_dict)

## Remove an item from a dictionary.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Different removal methods
del my_dict['age']  # Method 1: del keyword
removed_value = my_dict.pop('city')  # Method 2: pop() - returns value
my_dict.popitem()  # Method 3: popitem() - removes last inserted item

print("After removals:", my_dict)
print("Removed city value:", removed_value)

## Copy a dictionary and modify it without affecting the original.
original = {'a': 1, 'b': 2, 'c': 3}

# Shallow copy methods
copy1 = original.copy()  # Method 1
copy2 = dict(original)   # Method 2

# Modify the copies
copy1['d'] = 4
copy2['a'] = 10

print("Original:", original)
print("Copy 1:", copy1)
print("Copy 2:", copy2)

## Loop through a dictionary and print keys and values.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Different iteration methods
print("\nMethod 1: items()")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\nMethod 2: keys()")
for key in my_dict.keys():
    print(f"{key}: {my_dict[key]}")

print("\nMethod 3: Direct iteration")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")