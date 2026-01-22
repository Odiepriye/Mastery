"""
TYPING MODULE: Advanced Type Hints

WHY: Catch errors before running, IDE support, documentation
HOW: Add type annotations to variables, functions, and classes
TOOL: mypy --strict (static type checker)

BASIC TYPES (Review):
  x: int = 5
  name: str = "Alice"
  items: list[int] = [1, 2, 3]
  mapping: dict[str, int] = {"a": 1}
  def func(x: int, y: int) -> int: return x + y
"""
# Simple function typing
def add(x: int, y: int) -> int:
    return x + y

result: int = add(5, 3)
print(f"add(5, 3) = {result}")

# Collections
numbers: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1, "b": 2}
print(f"Numbers: {numbers}, Mapping: {mapping}")


"""
ADVANCED CONCEPTS - See separate files:

1. PROTOCOL (protocoltyping.py)
   - Structural typing (duck typing with types)
   - Don't require inheritance
   - If it has the methods, it satisfies the Protocol
   - BEST for: Multiple unrelated classes doing same thing

2. TYPEDDICT (typedDict.py)
   - Add structure to dictionaries
   - Type checker catches missing/wrong keys
   - IDE gets autocomplete for dict access
   - BEST for: APIs returning structured data

3. GENERIC TYPES
   - TypeVar('T') - variable that represents any type
   - Generic[T] - class that works with any type
   - BEST for: Reusable containers, functions
"""

print("\n=== GENERIC TYPES ===")

from typing import TypeVar, Generic

T = TypeVar('T')

def first(items: list[T]) -> T:
    """Works with any list type"""
    return items[0]

num = first([1, 2, 3])      # Type checker knows: int
text = first(["a", "b"])    # Type checker knows: str
print(f"First number: {num}, First text: {text}")


"""
UNION TYPES:
  Old: Union[int, str]
  Modern (3.10+): int | str
  
  Optional[T] means T | None
"""

print("\n=== UNION & OPTIONAL ===")

def process(value: int | str) -> None:
    if isinstance(value, int):
        print(f"Number: {value}")
    else:
        print(f"Text: {value}")

process(42)
process("hello")

def find_user(user_id: int) -> dict | None:
    """Returns dict or None"""
    return {"id": user_id} if user_id > 0 else None

user = find_user(1)
print(f"User found: {user is not None}")


"""
LITERAL TYPES:
  Restrict value to specific options
  
  Literal["DEBUG", "INFO", "ERROR"]
"""

print("\n=== LITERAL TYPES ===")

from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"Mode: {mode}")

set_mode("read")
# set_mode("invalid")  # Type checker warns!


"""
CALLABLE TYPES:
  Functions as parameters
  
  Callable[[input_types], return_type]
"""

print("\n=== CALLABLE TYPES ===")

from typing import Callable

def apply_op(x: int, y: int, op: Callable[[int, int], int]) -> int:
    """Take two ints and a function that takes two ints"""
    return op(x, y)

result = apply_op(5, 3, lambda a, b: a + b)
print(f"5 + 3 = {result}")


"""
TYPE ALIASES:
  Name complex types for readability
  
  UserId: TypeAlias = int
  Config: TypeAlias = dict[str, str | int | bool]
"""

print("\n=== TYPE ALIASES ===")

from typing import TypeAlias

UserId: TypeAlias = int
Username: TypeAlias = str
UserRecord: TypeAlias = dict[str, str | int]

users: dict[UserId, UserRecord] = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
}
print(f"Users: {users}")


"""
MYPY - STATIC TYPE CHECKING

Install: pip install mypy
Run: mypy file.py
Strict: mypy --strict file.py

Catches:
  - Wrong argument types
  - Missing return types
  - Attribute errors
  - Type inconsistencies
  
Output example:
  file.py:5: error: Argument 1 to "add" has incompatible type "str"; expected "int"
"""

print("\n=== MYPY CHECKING ===")
print("Run: mypy --strict yourfile.py")
print("Catches type errors BEFORE runtime")


"""
BEST PRACTICES

✓ Always type function signatures
✓ Use Protocol for flexible interfaces
✓ Use TypedDict for structured dicts
✓ Use Generic[T] for reusable code
✓ Use Literal for constrained values
✓ Run mypy --strict on your code
✓ Add types incrementally (gradual typing)
✓ Leverage IDE support (autocomplete, errors)

DON'T:
✗ Assume types are enforced at runtime (they're not!)
✗ Make type hints if it makes code unreadable
✗ Try to type everything at once
"""

print("\n=== SUMMARY ===")
print("✓ Catch errors with static type checking")
print("✓ Better IDE support and autocomplete")
print("✓ Self-documenting code")
print("✓ Safe refactoring")
