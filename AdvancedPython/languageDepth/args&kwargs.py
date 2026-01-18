"""
args are short for arguments and kwargs are short for keyword arguments
*args is used to pass a variable number of positional arguments to a function and are passed as a tuple
**kwargs is used to pass a variable number of keyword arguments to a function and are passed as a dictionary

*args and **kwargs let you write functions that accept flexible numbers of arguments
without knowing ahead of time how many you'll get.
"""
# Without *args: Limited flexibility
def add(a, b):
    return a + b

add(1, 2)           # Works
# add(1, 2, 3)         ERROR: takes 2 positional arguments but 3 were given


# example with *args: Flexible!
def add(*args):
    return sum(args)

add(1, 2)           # Works: 3
add(1, 2, 3)        # Works: 6
add(1, 2, 3, 4, 5)  # Works: 15


# example with **kwargs: Flexible!
def print_person(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Kwargs: {kwargs}")

print_person(name="Alice", age=30, city="NYC")
# Output:
# Type: <class 'dict'>
# Kwargs: {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Access like a dict:
def greet(**kwargs):
    name = kwargs.get('name', 'Unknown')
    age = kwargs.get('age', '?')
    print(f"Hello {name}, you are {age}")

greet(name="Bob", age=25)  # Hello Bob, you are 25
greet(name="Carol")         # Hello Carol, you are ?

"""
When to use *args and **kwargs:
*args is used when you don't know how many arguments will be passed to the function
**kwargs is used when you want to pass a variable number of keyword arguments to the function

when using both together positional arguments must come before keyword arguments
*args must also come before **kwargs when defining the function"""
# RIGHT: *args before **kwargs
def right(a, *args, **kwargs):
    pass

# WRONG: **kwargs before *args
# def wrong(a, **kwargs, *args):  SyntaxError!
    # pass

"""
Real-World Use Cases
Case 1: Decorator with Flexible Arguments
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):  # Accept ANY arguments so can wrap any function
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)  # Pass them through
        print(f"Done")
        return result
    return wrapper

@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")                    # Works
greet("Bob", greeting="Hi")       # Works
greet("Carol", greeting="Hey")    # Works
# Decorator doesn't need to know what args the function takes!

"""
Case 2: Flexible Data Structure
"""
# Create dictionaries with flexible keys
def create_config(**kwargs):
    return kwargs

config = create_config(
    host="localhost",
    port=8080,
    debug=True,
    timeout=30
)
print(config)  # {'host': 'localhost', 'port': 8080, ...}

"""
Case 3: Function Composition
"""
def call_multiple(*functions, **kwargs):
    for func in functions:
        result = func(**kwargs)
        print(f"{func.__name__} returned {result}")

def process_user(**kwargs):
    return f"User: {kwargs.get('name')}"

def validate_email(**kwargs):
    return f"Email valid: {kwargs.get('email')}"

call_multiple(
    process_user,
    validate_email,
    name="Alice",
    email="alice@example.com"
)

"""
* and ** can also be used to unpack arguments
"""
def add(*nums):
    return sum(nums)

numbers = [1, 2, 3, 4, 5]
print(add(*numbers))  # 15

def print_person(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Kwargs: {kwargs}")

person = {"name": "Alice", "age": 30, "city": "NYC"}
print_person(**person)  # {'name': 'Alice', 'age': 30, 'city': 'NYC'}