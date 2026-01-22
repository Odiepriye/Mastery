"""
TYPEDDICT: Structured Dictionaries

PROBLEM: Regular dicts are untyped
  data = {"name": "Alice", "age": 30}
  data["invalid_key"]  # No warning! KeyError at runtime

SOLUTION: TypedDict adds structure
  class Person(TypedDict):
      name: str
      age: int
  
  data: Person = {"name": "Alice", "age": 30}
  data["invalid_key"]  # Type checker warns!

BENEFITS:
  1. Type checker catches missing/wrong keys
  2. IDE autocomplete for dict access
  3. Documents expected structure
  4. Catches typos before runtime
"""

from typing import TypedDict

print("=== TYPEDDICT BASICS ===")

class PersonDict(TypedDict):
    name: str
    age: int
    email: str

person: PersonDict = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"Email: {person['email']}")

# Works with lists
people: list[PersonDict] = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
]

for person in people:
    print(f"{person['name']} ({person['age']}): {person['email']}")


print("\n=== OPTIONAL KEYS ===")

class ConfigDict(TypedDict, total=False):
    """All keys optional"""
    debug: bool
    timeout: int
    retries: int

# All valid:
config1: ConfigDict = {}
config2: ConfigDict = {"debug": True}
config3: ConfigDict = {"debug": True, "timeout": 30}

print(f"Config examples: {config1}, {config2}, {config3}")


print("\n=== REAL-WORLD: API Response ===")

class UserResponse(TypedDict):
    id: int
    username: str
    email: str
    active: bool

# Simulating API response
def get_user(user_id: int) -> UserResponse:
    return {
        "id": user_id,
        "username": "alice123",
        "email": "alice@example.com",
        "active": True
    }

user = get_user(1)
print(f"User: {user['username']} ({user['email']})")

print("\n=== WHY TYPEDDICT ===")
print("✓ Type checker catches typos: user['emial'] warns!")
print("✓ IDE autocomplete works")
print("✓ Documents dict structure")
print("✓ Catches bugs before runtime")
