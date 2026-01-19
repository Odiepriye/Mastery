"""
Dunder methods are special methods surrounded by double underscores: __method__
They are called automatically in response to specific operations.

They are called "magic methods" because they make objects behave like built-in types.

DUNDER METHODS ARE THE FOUNDATION OF PYTHON.


COMMON DUNDER METHODS

Object initialization:
__new__()      - Create the object instance (rarely override)
__init__()     - Initialize the object (override this)
__del__()      - Destructor (cleanup)

String representation:
__str__()      - User-friendly string (for humans)
__repr__()     - Developer-friendly representation (for debugging)

Comparison operators:
__eq__()       - Equal: ==
__ne__()       - Not equal: !=
__lt__()       - Less than: <
__le__()       - Less or equal: <=
__gt__()       - Greater than: >
__ge__()       - Greater or equal: >=

Arithmetic operators:
__add__()      - Addition: +
__sub__()      - Subtraction: -
__mul__()      - Multiplication: *
__truediv__()  - Division: /
__floordiv__() - Floor division: //
__mod__()      - Modulo: %
__pow__()      - Power: **

Container methods:
__len__()      - Length: len()
__getitem__()  - Indexing: obj[key]
__setitem__()  - Assignment: obj[key] = value
__delitem__()  - Deletion: del obj[key]
__contains__() - Membership: in

Iteration:
__iter__()     - Make object iterable
__next__()     - Get next item in iteration

Callable objects:
__call__()     - Make object callable like a function

Context managers:
__enter__()    - Enter with block
__exit__()     - Exit with block

Type coercion:
__int__()      - Convert to int
__float__()    - Convert to float
__bool__()     - Convert to bool
"""

# EXAMPLE 1: String Representation (__str__ vs __repr__)
print("=== Example 1: String Representation ===")

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """User-friendly string (print this)"""
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
    def __repr__(self):
        """Developer-friendly representation (for debugging)"""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

book = Book("1984", "George Orwell", 328)
print(str(book))    # Calls __str__: "1984 by George Orwell (328 pages)"
print(repr(book))   # Calls __repr__: "Book(title='1984', author='George Orwell', pages=328)"
print(book)         # Also calls __str__ when printed


# EXAMPLE 2: Comparison Methods (__eq__, __lt__, __gt__, etc)
print("\n=== Example 2: Comparison Operators ===")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        """Equal: =="""
        return self.grade == other.grade
    
    def __lt__(self, other):
        """Less than: <"""
        return self.grade < other.grade
    
    def __gt__(self, other):
        """Greater than: >"""
        return self.grade > other.grade
    
    def __le__(self, other):
        """Less or equal: <="""
        return self.grade <= other.grade
    
    def __ge__(self, other):
        """Greater or equal: >="""
        return self.grade >= other.grade
    
    def __ne__(self, other):
        """Not equal: !="""
        return self.grade != other.grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"

alice = Student("Alice", 95)
bob = Student("Bob", 87)
carol = Student("Carol", 95)

print(f"alice == carol: {alice == carol}")  # True (same grade)
print(f"alice != bob: {alice != bob}")      # True (different grade)
print(f"alice > bob: {alice > bob}")        # True (higher grade)
print(f"bob < alice: {bob < alice}")        # True

# Sort students by grade (uses __lt__)
students = [alice, bob, carol]
sorted_students = sorted(students)
print(f"Sorted by grade: {sorted_students}")


# EXAMPLE 3: Arithmetic Operators (__add__, __sub__, __mul__, __truediv__)
print("\n=== Example 3: Arithmetic Operators ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Addition: +"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtraction: -"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiplication: *"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Division: /"""
        return Vector(self.x / scalar, self.y / scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")     # Calls __add__
print(f"v1 - v2: {v1 - v2}")     # Calls __sub__
print(f"v1 * 2: {v1 * 2}")       # Calls __mul__
print(f"v1 / 2: {v1 / 2}")       # Calls __truediv__


# EXAMPLE 4: Container Methods (__len__, __getitem__, __setitem__, __contains__)
print("\n=== Example 4: Container Methods ===")

class SimpleList:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        """Length: len()"""
        return len(self.items)
    
    def __getitem__(self, index):
        """Indexing: obj[index]"""
        return self.items[index]
    
    def __setitem__(self, index, value):
        """Assignment: obj[index] = value"""
        self.items[index] = value
    
    def __contains__(self, item):
        """Membership: in"""
        return item in self.items
    
    def __iter__(self):
        """Iteration: for item in obj"""
        return iter(self.items)
    
    def __repr__(self):
        return f"SimpleList({self.items})"
    
    def append(self, item):
        self.items.append(item)

sl = SimpleList()
sl.append(10)
sl.append(20)
sl.append(30)

print(f"SimpleList: {sl}")
print(f"len(sl): {len(sl)}")          # Calls __len__: 3
print(f"sl[0]: {sl[0]}")              # Calls __getitem__: 10
sl[0] = 100                           # Calls __setitem__
print(f"After sl[0] = 100: {sl}")
print(f"20 in sl: {20 in sl}")         # Calls __contains__: True
print(f"999 in sl: {999 in sl}")       # Calls __contains__: False

print("Iterating (calls __iter__):")
for item in sl:
    print(f"  {item}")


# EXAMPLE 5: Callable Objects (__call__)
print("\n=== Example 5: Callable Objects ===")

class Multiplier:
    """Make an object callable like a function"""
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """Called when obj() is used"""
        return x * self.factor
    
    def __repr__(self):
        return f"Multiplier({self.factor})"

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5): {double(5)}")      # Calls __call__: 10
print(f"triple(5): {triple(5)}")      # Calls __call__: 15

# Use in map (passes callable object)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(f"Doubled: {doubled}")


# EXAMPLE 6: Type Coercion (__int__, __float__, __bool__)
print("\n=== Example 6: Type Coercion ===")

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def __int__(self):
        """Convert to int"""
        return int(self.celsius)
    
    def __float__(self):
        """Convert to float"""
        return float(self.celsius)
    
    def __bool__(self):
        """Convert to bool (truthiness)"""
        return self.celsius > 0  # Positive = True, non-positive = False
    
    def __repr__(self):
        return f"Temperature({self.celsius}°C)"

temp_hot = Temperature(25)
temp_cold = Temperature(-5)
temp_freezing = Temperature(0)

print(f"temp_hot: {temp_hot}")
print(f"int(temp_hot): {int(temp_hot)}")     # Calls __int__: 25
print(f"float(temp_hot): {float(temp_hot)}") # Calls __float__: 25.0

print(f"\nbool(temp_hot): {bool(temp_hot)}")        # True (positive)
print(f"bool(temp_cold): {bool(temp_cold)}")       # False (negative)
print(f"bool(temp_freezing): {bool(temp_freezing)}")  # False (zero)

if temp_hot:
    print(f"It's warm: {temp_hot}")

if not temp_cold:
    print(f"It's cold: {temp_cold}")


# EXAMPLE 7: Context Managers (__enter__, __exit__)
print("\n=== Example 7: Context Managers ===")

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Called when entering with block"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting with block (even if error)"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        return False

# Simulate file handling
class MockFile:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, content):
        print(f"Writing to {self.filename}: {content}")
    
    def read(self):
        return f"Content of {self.filename}"

class SimpleMockContext:
    def __init__(self, filename):
        self.filename = filename
        self.file = MockFile(filename)
    
    def __enter__(self):
        print(f"[Context] Opening {self.filename}")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[Context] Closing {self.filename}")
        return False

with SimpleMockContext("test.txt") as f:
    f.write("Hello, World!")


# EXAMPLE 8: Iterator Protocol (__iter__, __next__)
print("\n=== Example 8: Iterator Protocol ===")

class CountUp:
    """Iterable that counts from 1 to max"""
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        """Called when iteration starts: for x in obj"""
        self.current = 0
        return self
    
    def __next__(self):
        """Called on each iteration: next(obj)"""
        self.current += 1
        if self.current > self.max:
            raise StopIteration
        return self.current
    
    def __repr__(self):
        return f"CountUp(1..{self.max})"

counter = CountUp(5)
print(f"Counting: {counter}")

print("Using for loop (calls __iter__ and __next__):")
for num in counter:
    print(f"  {num}")

print("Iterating again (notice we can re-iterate because __iter__ resets):")
for num in counter:
    print(f"  {num}")


# EXAMPLE 9: How Decorators Use __call__
print("\n=== Example 9: Decorators Use __call__ ===")

class TimingDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        """Called when decorated function is invoked"""
        import time
        print(f"[Decorator] Calling {self.func.__name__}")
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[Decorator] Took {elapsed:.4f}s")
        return result

@TimingDecorator
def slow_function(n):
    import time
    time.sleep(0.1)
    return f"Done with {n}"

result = slow_function(5)  # Calls TimingDecorator.__call__
print(f"Result: {result}")


"""
UNDERSTANDING THE FLOW

When you write:           Python actually calls:
len(obj)                  obj.__len__()
str(obj)                  obj.__str__()
obj[i]                    obj.__getitem__(i)
obj[i] = value            obj.__setitem__(i, value)
obj + other               obj.__add__(other)
obj == other              obj.__eq__(other)
for item in obj:          obj.__iter__() then __next__()
obj()                     obj.__call__()
with obj:                 obj.__enter__() and __exit__()
int(obj)                  obj.__int__()
bool(obj)                 obj.__bool__()
"""

"""
WHY DUNDER METHODS MATTER

1. PROTOCOL IMPLEMENTATION: By implementing dunder methods, your objects
   "speak the language" of Python. They work with built-in functions.

2. INTEGRATION: Your custom types work seamlessly with:
   - Sorting (implements __lt__)
   - String formatting (implements __str__)
   - Collections (implements __len__, __getitem__)
   - Iteration (implements __iter__)
   - Mathematical operations (implements __add__, __mul__, etc)

3. ABSTRACTION: Users of your class don't need to learn your API.
   They use standard Python operations that feel natural.

4. COMPOSABILITY: Your objects work with Python's tools:
   - sorted() uses __lt__
   - len() uses __len__
   - for loops use __iter__
   - with statements use __enter__/__exit__

5. EVERYTHING IN PYTHON IS AN OBJECT:
   - Numbers are objects (implement __add__, __mul__, etc)
   - Strings are objects (implement __len__, __getitem__, etc)
   - Functions are objects (implement __call__)
   - Classes are objects (implement __init__, __new__)
"""

"""
DUNDER METHODS AND YOUR STAGE 2 LEARNING

Decorators: They use __call__ to make objects callable
Context Managers: They use __enter__ and __exit__
Generators: They use __iter__ and __next__

Understanding dunder methods unlocks deep Python knowledge!
"""
