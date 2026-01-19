"""
TYPING MODULE: Advanced Type Hints

Python has dynamic typing (flexible but risky).
Type hints allow you to add type information without breaking flexibility.

WHY TYPING MATTERS:
1. Catch errors BEFORE running code (static analysis)
2. IDE autocomplete works better
3. Documentation: shows what types functions accept
4. Refactoring safely: type checker catches breaking changes
5. Production quality: catches subtle bugs early

TOOLS:
mypy - Static type checker
pyright - Another static type checker
IDE support - VS Code, PyCharm, etc

BASIC SYNTAX:
variable: type = value
def function(param: type) -> return_type:
    pass
"""

# BASIC TYPING (Review)
print("=== BASIC TYPING ===")

def add(x: int, y: int) -> int:
    """Simple type hints"""
    return x + y

result: int = add(5, 3)
print(f"add(5, 3) = {result}")

# Collections
numbers: list[int] = [1, 2, 3, 4, 5]
mapping: dict[str, int] = {"a": 1, "b": 2}
names: set[str] = {"Alice", "Bob"}
pair: tuple[int, str] = (1, "hello")

print(f"List of ints: {numbers}")
print(f"Dict: {mapping}")


"""
PROTOCOL: Structural Typing

Normal typing requires inheritance (nominal typing):
  class Animal: ...
  class Dog(Animal): ...
  def func(x: Animal): ...  # Only accepts Animal subclass

Protocol enables structural typing (duck typing with types):
  class Speaker(Protocol):
      def speak() -> str: ...
  class Dog:  # No inheritance!
      def speak() -> str: ...
  def func(x: Speaker): ...  # Accepts ANYTHING with speak()

KEY: If an object has the required methods, it satisfies the Protocol.
     It doesn't matter where the object comes from or what class it is.
"""

from typing import Protocol

print("\n=== PROTOCOL: Structural Typing ===")

class Drawable(Protocol):
    """Protocol: anything that can be drawn"""
    def draw(self) -> str:
        ...  # Just define the signature

class Circle:
    def draw(self) -> str:
        return "⭕"

class Square:
    def draw(self) -> str:
        return "□"

class Triangle:
    def draw(self) -> str:
        return "△"

def render(shape: Drawable) -> None:
    """Works with ANYTHING that has draw() method"""
    print(shape.draw())

# No inheritance needed! Just needs draw()
render(Circle())    # OK
render(Square())    # OK
render(Triangle())  # OK

shapes: list[Drawable] = [Circle(), Square(), Triangle()]
for shape in shapes:
    render(shape)


"""
REAL-WORLD PROTOCOL EXAMPLE: DataSource
"""

class DataSource(Protocol):
    """Any object that can fetch data"""
    def fetch(self, query: str) -> list[dict]:
        ...

class DatabaseConnection:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 1, "name": "Alice"}]

class RestAPI:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 2, "name": "Bob"}]

class CsvFile:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 3, "name": "Carol"}]

def process_data(source: DataSource, query: str) -> None:
    """Works with any data source"""
    results = source.fetch(query)
    for row in results:
        print(f"  {row}")

print("\n=== Processing from different sources ===")
print("From Database:")
process_data(DatabaseConnection(), "SELECT * FROM users")

print("From API:")
process_data(RestAPI(), "GET /users")

print("From CSV:")
process_data(CsvFile(), "users.csv")


"""
TYPEDDICT: Structured Dictionaries

Regular dict is untyped:
    data = {"name": "Alice", "age": 30}
    data["invalid_key"]  # No warning! KeyError at runtime

TypedDict adds structure:
    class Person(TypedDict):
        name: str
        age: int
    
    data: Person = {"name": "Alice", "age": 30}
    data["invalid_key"]  # Type checker warns!
"""

from typing import TypedDict

print("\n=== TYPEDDICT: Structured Dicts ===")

class PersonDict(TypedDict):
    """Defines the structure of a person dict"""
    name: str
    age: int
    email: str

# Type checker validates this
person: PersonDict = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Email: {person['email']}")

# Working with TypedDict
people: list[PersonDict] = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
]

for person in people:
    print(f"{person['name']} ({person['age']}): {person['email']}")


"""
TYPEDDICT WITH OPTIONAL KEYS
"""

class ConfigDict(TypedDict, total=False):
    """All keys are optional"""
    debug: bool
    timeout: int
    retries: int

class ConfigDictPartial(TypedDict):
    """Mix required and optional"""
    host: str          # Required
    port: int          # Required
    ssl: bool          # Optional with total=False trick

config: ConfigDict = {}  # OK with TypedDict(total=False)
config = {"debug": True}  # OK
config = {"debug": True, "timeout": 30}  # OK

print(f"\n=== TypedDict Config ===")
print(f"Config: {config}")


"""
GENERIC TYPES: Write once, use with any type

TypeVar: Variable that stands for any type
Generic[T]: Class that works with any type

Example: Container that works with int, str, etc
"""

from typing import TypeVar, Generic

print("\n=== GENERIC TYPES ===")

T = TypeVar('T')  # Generic type variable

def first(items: list[T]) -> T:
    """Returns first item, preserving type"""
    return items[0]

# Type checker knows the return type!
first_int: int = first([1, 2, 3])
first_str: str = first(["a", "b", "c"])

print(f"First of [1,2,3]: {first_int} (type: {type(first_int).__name__})")
print(f"First of ['a','b']: {first_str} (type: {type(first_str).__name__})")


"""
GENERIC CLASSES
"""

class Stack(Generic[T]):
    """Stack works with any type"""
    def __init__(self):
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T | None:
        return self._items.pop() if self._items else None
    
    def __len__(self) -> int:
        return len(self._items)

# Type-specific stacks
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"\nInt stack: {int_stack.pop()}")  # Type checker knows it's int

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(f"Str stack: {str_stack.pop()}")  # Type checker knows it's str


"""
UNION TYPES: Value can be multiple types

Old syntax: Union[int, str]
Modern syntax (3.10+): int | str
"""

from typing import Union

print("\n=== UNION TYPES ===")

# Old style
def process_old(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Number: {value}")
    else:
        print(f"Text: {value}")

# Modern style
def process(value: int | str) -> None:
    if isinstance(value, int):
        print(f"Number: {value}")
    else:
        print(f"Text: {value}")

process(42)       # OK
process("hello")  # OK
# process([1,2,3])  # Type checker warns!

print("Union with Optional:")

# Optional[T] means T | None
def find_by_id(user_id: int) -> dict | None:
    """Returns user dict or None if not found"""
    if user_id > 0:
        return {"id": user_id, "name": "User"}
    return None

user = find_by_id(1)
if user:
    print(f"Found: {user}")

not_found = find_by_id(-1)
print(f"Not found: {not_found}")


"""
LITERAL TYPES: Restrict to specific values

Useful for:
- Status enums ("pending", "approved", "rejected")
- Log levels ("DEBUG", "INFO", "ERROR")
- Modes ("read", "write", "append")
"""

from typing import Literal

print("\n=== LITERAL TYPES ===")

def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    print(f"Log level set to: {level}")

set_log_level("DEBUG")    # OK
set_log_level("INFO")     # OK
# set_log_level("INVALID")  # Type checker warns!

def approve_request(
    status: Literal["pending", "approved", "rejected"],
    reason: str = ""
) -> None:
    print(f"Status: {status}, Reason: {reason}")

approve_request("pending")
approve_request("approved")
approve_request("rejected", "Insufficient funds")


"""
CALLABLE TYPES: Type hints for functions

Callable[[input_types], return_type]
"""

from typing import Callable

print("\n=== CALLABLE TYPES ===")

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    """Apply operation to two integers"""
    return op(x, y)

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

result1 = apply_operation(5, 3, add)
result2 = apply_operation(5, 3, multiply)

print(f"5 + 3 = {result1}")
print(f"5 * 3 = {result2}")

# With lambda
result3 = apply_operation(5, 3, lambda a, b: a ** b)
print(f"5 ** 3 = {result3}")


"""
TYPE ALIASES: Name complex types

Instead of:
    config_dict: dict[str, int | bool | str]

Use:
    Config = dict[str, int | bool | str]
    config_dict: Config
"""

from typing import TypeAlias

print("\n=== TYPE ALIASES ===")

# Simple alias
StringList: TypeAlias = list[str]
StringDict: TypeAlias = dict[str, str]

words: StringList = ["hello", "world", "python"]
mapping: StringDict = {"en": "hello", "es": "hola"}

print(f"Words: {words}")
print(f"Mapping: {mapping}")

# Complex alias
UserId: TypeAlias = int
UserData: TypeAlias = dict[str, str | int | bool]

users: dict[UserId, UserData] = {
    1: {"name": "Alice", "age": 30, "active": True},
    2: {"name": "Bob", "age": 25, "active": False},
}

for user_id, user_data in users.items():
    print(f"User {user_id}: {user_data}")


"""
TYPE CHECKING WITH MYPY

mypy is a static type checker for Python.

Installation:
    pip install mypy

Usage:
    mypy file.py              # Check file
    mypy --strict file.py     # Strict mode (recommended)
    mypy .                    # Check entire project
    mypy --ignore-missing-imports file.py  # Ignore 3rd party libs

Output:
    file.py:5: error: Argument 1 to "add" has incompatible type "str"; expected "int"

Mypy catches:
- Wrong argument types
- Missing return types
- Attribute errors
- Type inconsistencies
- And much more!
"""

print("\n=== MYPY: Static Type Checking ===")
print("See examples/mypy_examples.py for detailed mypy examples")


"""
BEST PRACTICES FOR TYPING

1. ALWAYS TYPE FUNCTION SIGNATURES
   def func(x: int, y: int) -> int:
       return x + y

2. USE PROTOCOL FOR FLEXIBILITY
   class MyProtocol(Protocol):
       def method(self) -> None: ...

3. USE TYPEDDICT FOR DICTS WITH STRUCTURE
   class Config(TypedDict):
       name: str
       value: int

4. USE GENERIC TYPES FOR REUSABLE CODE
   T = TypeVar('T')
   def first(items: list[T]) -> T:
       return items[0]

5. USE UNION/OPTIONAL FOR MULTIPLE TYPES
   def func(x: int | None) -> str | None:
       ...

6. USE LITERAL FOR CONSTRAINED VALUES
   def set_mode(mode: Literal["read", "write"]):
       ...

7. RUN MYPY REGULARLY
   mypy --strict .

8. START WITH GRADUAL TYPING
   - Add types incrementally
   - Use --ignore-missing-imports for 3rd party libs
   - Focus on public APIs first

9. USE TYPE ALIASES FOR COMPLEX TYPES
   UserId: TypeAlias = int
   
10. LEVERAGE IDE SUPPORT
    - PyCharm, VS Code understand types
    - Get autocomplete and inline errors
"""

"""
TYPING IN YOUR MASTERY PROJECT 2

For your Data Processing Service:

from typing import Protocol, TypedDict, TypeVar, Generic

class DataSource(Protocol):
    def fetch(self, query: str) -> list[dict]:
        ...

class ProcessorConfig(TypedDict):
    debug: bool
    timeout: int
    retries: int

T = TypeVar('T')

class Pipeline(Generic[T]):
    def process(self, data: T) -> T:
        ...

Then use:
    pipeline: Pipeline[str] = Pipeline()
    config: ProcessorConfig = {"debug": True, "timeout": 30, "retries": 3}
    source: DataSource = DatabaseConnection()
"""

print("\n=== TYPING SUMMARY ===")
print("✓ Basic types (int, str, list, dict, etc)")
print("✓ Protocol (structural typing)")
print("✓ TypedDict (structured dictionaries)")
print("✓ Generic types (T, Generic[T])")
print("✓ Union types (int | str)")
print("✓ Literal types (restricted values)")
print("✓ Callable types (function signatures)")
print("✓ Type aliases")
print("✓ mypy static checking")
