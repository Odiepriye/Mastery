"""
Decorators:
Decorators are a way to modify or enhance functions or methods.
They are used to add functionality to functions or methods without modifying their code.
They are functions that take a function as an argument and return a modified function.

If a function is a plain cup of coffee, a decorator is the barista who adds cream, sugar, or cinnamon to that coffee. 
The coffee still tastes like coffee, but it's enhanced.
"""
# e.g. 
def square(func):
    def myinner(x):
        return func(x) ** 2
    return myinner

@square
def multiply(x):
    return x

print(multiply(81))

"""
An important note about decorators is that they are executed differently than regular functions.
1 when the decorator is defined, the decorator is executed (At definition time )
2 when the decorated function is called, the wrapper function is executed (At call time )
Decorators are executed at definition time, so the decorator is executed when the module is imported.
"""
def my_decorator(func): 
    print(f"DECORATOR EXECUTING: Decorating {func.__name__}")
    
    def wrapper():
        print("WRAPPER: About to call the function")
        result = func()
        print("WRAPPER: Function returned")
        return result
    
    print("DECORATOR: Returning wrapper")
    return wrapper


print("=== STEP 1: Defining the decorated function ===")
@my_decorator
def say_hello():
    print("FUNCTION: Hello!")

print("\n=== STEP 2: Calling the decorated function ===")
say_hello()

print("\n=== STEP 3: Calling again ===")
say_hello()

"""
Decorator Nesting comes in 2 ways:
Without parenthesis/without parameters - the decorator is executed at definition time
Layer 1 (decorator) captures the function being decorated (greet)
Layer 2 (wrapper) captures the arguments to the function (name)
"""
# Layer 1: The decorator itself (receives the function)
def decorator_without_parenthesis(func):
    # Layer 2: The wrapper (receives the function's arguments)
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@decorator_without_parenthesis
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
"""
With parenthesis/with parameters - the decorator is executed at call time
Layer 1 (factory) captures the decorator arguments ("important_config")
Layer 2 (decorator) captures the function being decorated (greet)
Layer 3 (wrapper) captures the arguments to the function (name)
"""
# Layer 1: The FACTORY (receives decorator parameters)
def decorator_with_parenthesis(config):
    # Layer 2: The DECORATOR (receives the function being decorated)
    def decorator(func):
        # Layer 3: The WRAPPER (receives the function's arguments)
        def wrapper(*args, **kwargs):
            print(f"Config: {config}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@decorator_with_parenthesis("important_config")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

"""
Why use decorators over helper functions?
"""
#helper functions
import time

def log_execution(func_name):
    print(f"Function {func_name} is running")

def measure_time(start_time):
    elapsed = time.time() - start_time
    print(f"Took {elapsed:.2f} seconds")

def get_user(user_id):
    log_execution("get_user")
    start = time.time()
    
    time.sleep(1)  # Simulate work
    result = {"id": user_id, "name": "Alice"}
    
    measure_time(start)
    return result

def update_user(user_id, data):
    log_execution("update_user")
    start = time.time()
    
    time.sleep(0.5)  # Simulate work
    result = {"id": user_id, **data}
    
    measure_time(start)
    return result

get_user(1)
update_user(1, {"name": "Bob"})

#decorators
from functools import wraps

"""
Benefits:
- DRY — logic lives in ONE place
- Reusable — apply to ANY function
- Readable — @log_and_time tells you what's happening
- Maintainable — change timing logic once, affects everywhere
- Composable — stack multiple decorators
"""

def log_and_time(func):
    # @wraps preserves the original function's name, docstring, and other metadata. Tools that inspect code rely on this.
    @wraps(func)  
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is running")
        start = time.time()
        
        result = func(*args, **kwargs)
        
        elapsed = time.time() - start
        print(f"Took {elapsed:.2f} seconds")
        return result
    return wrapper

@log_and_time
def get_user(user_id):
    time.sleep(1)
    return {"id": user_id, "name": "Alice"}

@log_and_time
def update_user(user_id, data):
    time.sleep(0.5)
    return {"id": user_id, **data}

get_user(1)
update_user(1, {"name": "Bob"})

"""
DECORATORS VS HELPER FUNCTIONS: When to Use Each

Helper Functions: Use when the function's OUTPUT or BEHAVIOR changes based on the helper's work
- The decorated function ACTIVELY NEEDS the helper's result
- Example: validate_email() must be called because we need validation to succeed
- The logic is PART OF the function's core behavior

Decorators: Use when you want to WRAP/ENHANCE behavior without changing the function's core logic
- The decorated function is UNAWARE it's been decorated
- The function works the SAME, just with stuff happening around it
- Example: @require_auth() adds a guard, but the function doesn't know or care about auth

KEY INSIGHT: Decorators solve "cross-cutting concerns" - behaviors that apply to MANY functions
but shouldn't clutter their core logic.

Cross-cutting concerns (USE DECORATORS):
1. Timing/Performance monitoring
2. Logging/Tracing
3. Caching/Memoization
4. Authentication/Authorization
5. Retry logic
6. Rate limiting
7. Input validation (wrapper style)

Function-specific logic (USE HELPER FUNCTIONS):
1. Data validation that fails the operation
2. Data transformation that changes the result
3. Calculations needed for the function to work
4. State that the function depends on
"""

# EXAMPLE: When to use Decorator vs Helper Function

# Example 1: HELPER FUNCTION
# The function NEEDS the validation result
def validate_email(email):
    """Validate email format"""
    if "@" not in email:
        raise ValueError("Invalid email")
    return True

def register_user(email, password):
    """Register a new user"""
    validate_email(email)  # We NEED this to succeed
    # Create user...
    return {"email": email, "status": "registered"}

# register_user("test@example.com", "pass123")


# Example 2: DECORATOR
# The function doesn't need to know about authentication
def require_auth(func):
    """Decorator: adds authentication check without function knowing"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Simulate auth check
        is_authenticated = True
        if not is_authenticated:
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def delete_user(user_id):
    """Delete a user"""
    # This function doesn't know or care about auth
    # The decorator adds that concern
    return {"id": user_id, "status": "deleted"}

# delete_user(123)


# Example 3: MULTIPLE DECORATORS (Cross-cutting concerns)
def require_admin(func):
    """Decorator: adds admin check"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_admin = True
        if not is_admin:
            raise PermissionError("Admin only")
        return func(*args, **kwargs)
    return wrapper

def audit_log(func):
    """Decorator: logs the action"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"AUDIT: {func.__name__} called with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"AUDIT: {func.__name__} returned {result}")
        return result
    return wrapper

@require_admin        # Applied LAST (outermost)
@audit_log            # Applied SECOND
@log_and_time         # Applied FIRST (innermost)
def dangerous_operation(user_id):
    """A dangerous operation that needs multiple checks"""
    time.sleep(0.2)
    return {"user_id": user_id, "operation": "completed"}

# dangerous_operation(1)
# Notice: The function is clean and focused
# All cross-cutting concerns are handled by decorators


# QUIZ: Which should be Decorator, which Helper?
"""
1. A function that checks if a user has permission to edit a post
   → DECORATOR (auth concern, many functions need it)

2. A function that measures how many database queries a function makes
   → DECORATOR (monitoring concern, applied across the app)

3. A function that transforms a string to uppercase
   → HELPER (part of the function's core logic)

4. A function that retries an operation if it fails
   → DECORATOR (retry logic wraps the function, function doesn't care)

5. A function that fetches user data from database
   → HELPER (core logic the function depends on)

6. A function that rate limits API calls
   → DECORATOR (applies to many endpoints, they don't need to know about it)
"""
