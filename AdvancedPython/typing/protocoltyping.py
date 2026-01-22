"""
PROTOCOL: Structural Typing

NOMINAL TYPING (Inheritance):
  "You must be a subclass of X"
  class Animal: ...
  class Dog(Animal): ...
  def func(x: Animal): ...  # Only accepts Animal subclass

STRUCTURAL TYPING (Protocol):
  "You just need these methods"
  class Speaker(Protocol):
      def speak() -> str: ...
  class Dog:  # No inheritance!
      def speak() -> str: ...
  def func(x: Speaker): ...  # Accepts ANYTHING with speak()

KEY: If object has the required methods, it satisfies the Protocol.
     Loose coupling, maximum flexibility, Pythonic!
"""

from typing import Protocol

print("=== PROTOCOL BASICS ===")

# Simple Protocol example
class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "⭕"

class Square:
    def draw(self) -> str:
        return "□"

def render(shape: Drawable) -> None:
    print(shape.draw())

render(Circle())   # Works - has draw()
render(Square())   # Works - has draw()

print("\n=== REAL-WORLD: DataFetcher Protocol ===")

# Any data source that can fetch data
class DataFetcher(Protocol):
    def fetch(self, query: str) -> list[dict]:
        ...

# Three completely different implementations
class DatabaseConnection:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 1, "name": "Alice"}]

class RestAPI:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 2, "name": "Bob"}]

class CsvFile:
    def fetch(self, query: str) -> list[dict]:
        return [{"id": 3, "name": "Carol"}]

# One function works with all three!
def process_data(source: DataFetcher, query: str) -> None:
    results = source.fetch(query)
    for row in results:
        print(f"  {row}")

print("From Database:")
process_data(DatabaseConnection(), "SELECT * FROM users")

print("From API:")
process_data(RestAPI(), "GET /users")

print("From CSV:")
process_data(CsvFile(), "users.csv")

print("\n=== WHY PROTOCOL > INHERITANCE ===")
print("Without Protocol: Must force all to inherit from DataFetcher")
print("With Protocol: Just implement fetch(), no inheritance needed")
print("Result: Loose coupling, maximum flexibility")
