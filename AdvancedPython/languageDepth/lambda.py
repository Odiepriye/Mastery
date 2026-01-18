"""
Lambda is python's answer to anonymous functions.
you use ONCE and pass as an argument to another function.

SYNTAX:
(lambda) (arguments): (expression)

KEY: Lambda returns a value implicitly (no 'return' keyword needed)
"""

# BASIC EXAMPLE: Comparing lambda to regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25
print(square(10))  # 100


"""
REAL-WORLD USE CASE 1: Sorting with Custom Logic
This is the #1 reason to use lambdas
"""

people = [
    {'name': 'Alice', 'age': 30, 'salary': 50000},
    {'name': 'Bob', 'age': 25, 'salary': 60000},
    {'name': 'Carol', 'age': 30, 'salary': 55000}
]

# Sort by age
sorted_by_age = sorted(people, key=lambda p: p['age'])
print("\nSorted by age:")
for person in sorted_by_age:
    print(f"  {person['name']}: {person['age']}")

# Sort by salary (descending)
sorted_by_salary = sorted(people, key=lambda p: p['salary'], reverse=True)
print("\nSorted by salary (descending):")
for person in sorted_by_salary:
    print(f"  {person['name']}: {person['salary']}")

# Sort by age, THEN by salary (tuple key)
sorted_complex = sorted(people, key=lambda p: (p['age'], p['salary']))
print("\nSorted by age, then salary:")
for person in sorted_complex:
    print(f"  {person['name']}: age {person['age']}, salary {person['salary']}")


"""
REAL-WORLD USE CASE 2: Map - Transform Every Item
Apply a function to every item in a sequence
"""

numbers = [1, 2, 3, 4, 5]

# Without lambda: Need a throwaway function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(f"\nDoubled (with function): {doubled}")

# With lambda: Express intent inline
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled (with lambda): {doubled}")

# More complex transformation
prices = [10, 20, 30]
with_tax = list(map(lambda p: p * 1.1, prices))  # Add 10% tax
print(f"Prices with 10% tax: {with_tax}")


"""
REAL-WORLD USE CASE 3: Filter - Keep Only Items Where Condition is True
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEven numbers: {evens}")

# Get only numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {greater_than_5}")

# Filter strings
words = ["apple", "banana", "ant", "apricot", "bear"]
starts_with_a = list(filter(lambda w: w.startswith('a'), words))
print(f"Words starting with 'a': {starts_with_a}")

"""
PATTERN 1: Sort by Multiple Criteria
Use tuples to sort by multiple fields
"""

products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Mouse', 'category': 'Electronics', 'price': 25},
    {'name': 'Desk', 'category': 'Furniture', 'price': 300},
    {'name': 'Chair', 'category': 'Furniture', 'price': 150}
]

# Sort by category, THEN by price
sorted_products = sorted(products, key=lambda p: (p['category'], p['price']))
print("\n=== Sorted by category, then price ===")
for product in sorted_products:
    print(f"  {product['category']}: {product['name']} (${product['price']})")


"""
PATTERN 2: Map + Filter (Nested)
Transform and filter in one pipeline
"""

scores = [45, 78, 92, 34, 88, 56, 100]

# Get passing scores (>60), then add curve (+5 points)
curved_passing = list(map(lambda x: x + 5, filter(lambda x: x >= 60, scores)))
print(f"\nPassing scores with +5 curve: {curved_passing}")


"""
PATTERN 3: Event Handlers / Callbacks
Lambda is perfect for quick one-off behavior
"""

# Simulating a button click handler
def on_button_click(handler):
    print("Button clicked!")
    handler()

# Without lambda: Need a named function
def say_hello():
    print("Hello!")

on_button_click(say_hello)

# With lambda: Express behavior inline
on_button_click(lambda: print("Goodbye!"))


"""
WHEN NOT TO USE LAMBDA

DON'T: Use lambda for complex logic
Instead: Use a regular function

DON'T: Use lambda if you need multiple lines
Instead: Use a regular function

DON'T: Use lambda for reusable functions
Instead: Use a regular function with a name

DON'T: Use lambda if it makes code LESS readable
Instead: Use list comprehension or regular function
"""

"""
BEST PRACTICES

USE LAMBDA when:
✅ Sorting with a custom key
✅ Passing a one-off function to map/filter/sorted
✅ Event handlers / callbacks
✅ The logic fits on one line and is clear

DON'T USE LAMBDA when:
❌ The logic is complex (multiple lines)
❌ You use the function more than once (name it!)
❌ It makes code less readable
❌ You need to debug (lambdas have no name)

READABILITY RULE:
If someone reads your lambda and has to think "what does this do?",
use a regular function with a descriptive name instead.
"""
