"""
A context manager is a way to manage resources in a program.
it is a class with 2 special methods: __enter__ and __exit__
__enter__ is called when the context manager is entered
__exit__ is called when the context manager is exited
"""
# e.g. 1 - MyContextManager
class MyContextManager:
    def __enter__(self):
        print("Entering the context manager")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context manager")

with MyContextManager() as cm:
    print("Inside the context manager")

# e.g. 2 - FileManager
class FileManager:
    def __enter__(self):
        """Runs when you enter the 'with' block"""
        print("SETUP: Opening resource")
        return self  # This is what becomes 'f' in 'with ... as f:'
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Runs when you exit the 'with' block, even if error happens"""
        print("CLEANUP: Closing resource")
        return False  # Return True to suppress exceptions


# How you use it:
with FileManager() as f:
    print("INSIDE: Using resource")
    # If error happens here, __exit__ still runs!

"""
THE PARAMETERS OF __EXIT__ ARE WHERE THE MAGIC HAPPENS:

def __exit__(self, exc_type, exc_val, exc_tb):
    exc_type: The exception class (None if no error, e.g., ValueError)
    exc_val: The exception instance (the actual error message)
    exc_tb: The traceback object (where the error happened)

RETURN VALUE MEANINGS:
- return False: Exception propagates normally (re-raise)
- return True: Exception is suppressed (swallowed, not raised)

Most of the time you return False so errors bubble up.
Return True only when you specifically want to hide/handle errors.

With this you can detect errors and handle cleanup differently!
"""
class SafeConnection:
    def __enter__(self):
        print("Connecting to database...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"ERROR! Rolling back transaction: {exc_val}")
            # Do rollback logic
        else:
            print("Success! Committing transaction")
            # Do commit logic
        return False  # Let exception propagate


with SafeConnection() as conn:
    # If an error happens here, rollback triggers
    # If no error, commit triggers
    pass
"""
Examples of context managers:
"""

# EXAMPLE 3: Timer Context Manager (Your Quiz Answer!)
import time

class Timer:
    def __enter__(self):
        print("Timer started")
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Took {elapsed:.2f} seconds")
        return False

# Usage:
with Timer():
    time.sleep(1)
    # Output:
    # Timer started
    # Took 1.00 seconds


# EXAMPLE 4: Demonstrating Cleanup Always Happens (Even with Errors)
class GuaranteedCleanup:
    def __enter__(self):
        print("Setup: Acquiring resource")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleanup: Releasing resource")
        if exc_type is not None:
            print(f"  (Exception occurred: {exc_type.__name__})")
        return False  # Let exception propagate

# No error:
print("=== Test 1: No error ===")
with GuaranteedCleanup():
    print("Doing work...")

# With error:
print("\n=== Test 2: With error ===")
try:
    with GuaranteedCleanup():
        print("Doing work...")
        raise ValueError("Something went wrong!")
except ValueError:
    print("Exception was caught outside")

# KEY INSIGHT: Cleanup ALWAYS happens, whether error or not!


# EXAMPLE 5: Suppressing Exceptions (return True)
class ErrorSuppressor:
    """This context manager SUPPRESSES exceptions"""
    def __enter__(self):
        print("Setting up")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Caught and suppressed: {exc_val}")
            return True  # THIS SUPPRESSES THE EXCEPTION
        return False

# The error is hidden:
print("\n=== Test 3: Suppressed exception ===")
with ErrorSuppressor():
    print("About to raise an error...")
    raise ValueError("This will be suppressed!")

print("Code continues! Error was hidden by context manager")


# EXAMPLE 6: Real-World Use Case - File Management
class MyFileManager:
    """A context manager for safely handling files"""
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        
        if exc_type is not None:
            print(f"Error occurred while using file: {exc_val}")
        
        return False


# Usage:
with MyFileManager("/tmp/test.txt", "w") as f:
    f.write("Hello, World!")
    # File closes automatically, even if write() fails


# CONTEXT MANAGERS VS DECORATORS
"""
DECORATOR: Wraps FUNCTION behavior
CONTEXT MANAGER: Manages RESOURCE lifecycle

Decorator example:
@timing
def my_function():
    pass
# Every time function is called, timing runs

Context Manager example:
with Timer():
    # code here
# Timer runs for this code block

WHEN TO USE EACH:
- Decorator: Apply behavior to multiple function calls
- Context Manager: Manage a resource for a block of code

THEY CAN WORK TOGETHER:
A decorator might use a context manager internally!
"""


# EXAMPLE 7: Combining Decorators and Context Managers
from functools import wraps

def with_timer(func):
    """Decorator that uses a context manager internally"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Timer():
            return func(*args, **kwargs)
    return wrapper

@with_timer
def slow_task():
    time.sleep(0.5)
    return "Done"

# Call it:
# slow_task()
# Output:
# Timer started
# Took 0.50 seconds


# BUILTIN CONTEXT MANAGERS YOU ALREADY USE
"""
1. File operations:
   with open('file.txt') as f:
       data = f.read()
   # File closes automatically

2. Threading/locking:
   with lock:
       # Critical section
   # Lock is released automatically

3. Database transactions:
   with db.transaction():
       db.insert(data)
   # Transaction commits or rolls back

4. Changing settings temporarily:
   with settings.debug(True):
       # Debug mode is on
   # Debug mode is off
"""


# KEY TAKEAWAYS
"""
1. Context managers ensure cleanup happens, even if errors occur
2. __enter__ runs on entering the 'with' block
3. __exit__ runs on exiting, with error information
4. return False = let exceptions propagate
5. return True = suppress exceptions (rarely needed)
6. Use them for resource management (files, connections, locks)
7. They guarantee safety and make code more readable
"""


# WHEN TO USE CONTEXT MANAGERS
"""
Context managers follow this pattern:
1. SETUP (acquire a resource)
2. DO WORK (use the resource)
3. CLEANUP (release the resource) — MUST HAPPEN, NO MATTER WHAT

USE CONTEXT MANAGERS WHEN:
- Opening files (guaranteed close)
- Database connections (guaranteed disconnect)
- Transactions (guaranteed commit/rollback)
- Resource locks (guaranteed release, prevents deadlocks)
- Temporary settings (guaranteed restore)
- Rate limiting (guaranteed token release)
- Logging context (guaranteed context removal)

DON'T USE CONTEXT MANAGERS WHEN:
- No cleanup is needed
- No resource is acquired
- The code can't error (simple calculations)

DECISION TREE:
1. Do I acquire a resource? → YES
2. Do I need to release/clean up? → YES
3. Could errors skip cleanup? → YES
→ USE CONTEXT MANAGER!

FORMULA: Resource + Cleanup + Error Risk = Context Manager
"""


# EXAMPLE 8: Database Transaction (Full Implementation)
class DatabaseTransaction:
    """Context manager for database transactions with auto-commit/rollback"""
    def __init__(self, database):
        self.db = database
    
    def __enter__(self):
        print("Transaction: STARTED")
        # In real code: self.db.begin_transaction()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Transaction: ROLLING BACK (error: {exc_val})")
            # In real code: self.db.rollback()
        else:
            print("Transaction: COMMITTED")
            # In real code: self.db.commit()
        return False


# Usage:
class FakeDB:
    pass

db = FakeDB()

# Success case:
print("=== Transaction Success ===")
with DatabaseTransaction(db):
    print("Inserting user...")
    print("Inserting order...")

# Error case:
print("\n=== Transaction Error ===")
try:
    with DatabaseTransaction(db):
        print("Inserting user...")
        raise ValueError("Invalid email!")
        print("Inserting order...")
except ValueError:
    print("Exception caught")

# Notice: Rollback happened automatically!


# CONTEXT MANAGERS WITH PARAMETERS (Similar to Decorators!)
class DebugMode:
    """Temporarily enable debug mode"""
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.old_debug = None
    
    def __enter__(self):
        # Save old value
        self.old_debug = False  # Pretend this was the old value
        print(f"Enabling debug mode")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Restoring debug mode to: {self.old_debug}")
        return False


# Usage with parameters:
with DebugMode(enabled=True):
    print("Debug is ON")
    print("Debug is ON")

print("Debug is OFF (automatically restored)")


# COMPARISON: WHEN TO USE WHAT
"""
DECORATORS: Wrap FUNCTION calls with behavior
@timing
def my_function():
    pass
# Timing happens EVERY TIME function is called

CONTEXT MANAGERS: Wrap CODE BLOCKS with lifecycle
with Timer():
    # code here
# Timer handles setup/cleanup for THIS block

USE TOGETHER: Decorator uses context manager internally
@with_timer
def my_function():
    pass
# Each function call gets its own context manager

HELPER FUNCTIONS: When logic is PART OF the operation
def process(data):
    validated = validate(data)  # Helper is part of core logic
    return result

RULE OF THUMB:
- Helper: Core logic, changes the result
- Decorator: Meta-concern, wraps every call
- Context Manager: Lifecycle management, setup/cleanup
"""