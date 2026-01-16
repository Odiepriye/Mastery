"""
Decorators:
Decorators are a way to modify or enhance functions or methods.
They are used to add functionality to functions or methods without modifying their code.
They are functions that take a function as an argument and return a modified function.

If a function is a plain cup of coffee, a decorator is the barista who adds cream, sugar, or cinnamon to that coffee. 
The coffee still tastes like coffee, but it's enhanced.
"""

def square(func):
    def myinner(x):
        return func(x) ** 2
    return myinner

@square
def multiply(x):
    return x * 2

print(multiply(2))
