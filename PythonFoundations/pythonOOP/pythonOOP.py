"""
═══════════════════════════════════════════════════════════════════
OBJECT-ORIENTED PROGRAMMING (OOP) - FOUR PILLARS
═══════════════════════════════════════════════════════════════════

The flow builds from foundation to power:

1. ENCAPSULATION (Foundation)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Protect data and methods using scope
   
   public (no underscore)     → Everyone can use
   _protected (_underscore)   → Internal, linters warn
   __private (__underscore)   → Hidden from outside
   
   Why: Safety, prevent misuse, maintain invariants

2. ABSTRACTION (Clarity)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Hide complexity, show only essential interface
   
   Users know WHAT to do, not HOW it works
   Example: car.accelerate() (not car.__adjust_fuel_injection())
   
   Implementation: Private variables + simple public methods + docs
   Why: Users understand code, maintainers can change internals

3. INHERITANCE (Reusability)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Child classes inherit from parent, reuse code
   
   class Dog(Animal):  # Inherits from Animal
       pass
   
   Dog gets all of Animal's methods + attributes
   Dog can override methods (provide own implementation)
   
   Why: DRY principle, one source of truth, maintainability

4. POLYMORPHISM (Flexibility)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Same method call, different behavior for different types
   
   dog.make_sound()   → "Woof!"
   cat.make_sound()   → "Meow!"
   bird.make_sound()  → "Tweet!"
   
   All different implementations, same method name
   
   Why: Write code once, works with all types (extensibility)

═══════════════════════════════════════════════════════════════════
HOW THEY WORK TOGETHER
═══════════════════════════════════════════════════════════════════

Encapsulation
    ↓ Creates safe interfaces
    ↓
Abstraction
    ↓ Shows simple behavior
    ↓
Inheritance
    ↓ Reuses that behavior
    ↓
Polymorphism
    ↓ Different types, same interface
    ↓
RESULT: Flexible, Extensible, Maintainable Code

Example Flow:
1. Encapsulation: Animal hides __energy, __hunger
2. Abstraction: Animal provides eat(), sleep() methods
3. Inheritance: Dog inherits eat(), sleep()
4. Polymorphism: Dog overrides make_sound() to "Woof!"

Principles:
1. safety
2. clarity
3. reusability
4. extensibility

═══════════════════════════════════════════════════════════════════
PRACTICAL EXAMPLE: Zoo System
═══════════════════════════════════════════════════════════════════

Step 1: ENCAPSULATION - Protect animal data
"""

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name: str):
        self.__name = name        # Private - protected
        self.__energy = 100       # Private - only Animal controls
    
    def make_sound(self) -> None:
        """Virtual method - subclasses override this."""
        print(f"{self.__name} makes a sound")
    
    def eat(self) -> None:
        """Public method - part of the interface."""
        self.__energy = min(100, self.__energy + 20)
        print(f"{self.__name} ate. Energy: {self.__energy}")


# Step 2: ABSTRACTION - Hide complexity, simple interface
# Step 3: INHERITANCE - Dog inherits Animal's protected interface
# Step 4: POLYMORPHISM - Different make_sound() for each type

class Dog(Animal):
    """Dog inherits from Animal, overrides make_sound."""
    
    def make_sound(self) -> None:
        print("Woof!")


class Cat(Animal):
    """Cat inherits from Animal, overrides make_sound."""
    
    def make_sound(self) -> None:
        print("Meow!")


class Bird(Animal):
    """Bird inherits from Animal, overrides make_sound."""
    
    def make_sound(self) -> None:
        print("Tweet!")


class Zoo:
    """Zoo manages animals polymorphically."""
    
    def __init__(self):
        self.animals: list[Animal] = []
    
    def add_animal(self, animal: Animal) -> None:
        """Add any Animal subclass - polymorphism!"""
        self.animals.append(animal)
    
    def feed_all(self) -> None:
        """All animals eat - works with any type!"""
        for animal in self.animals:
            animal.eat()
    
    def make_all_sounds(self) -> None:
        """All animals make sounds - different for each!"""
        for animal in self.animals:
            animal.make_sound()  # Polymorphism in action!


# Usage:
print("═══ Zoo Demo ═══")
zoo = Zoo()
zoo.add_animal(Dog("Buddy"))
zoo.add_animal(Cat("Whiskers"))
zoo.add_animal(Bird("Tweety"))

print("\nAll make sounds (polymorphism):")
zoo.make_all_sounds()

print("\nAll eat (inherited method):")
zoo.feed_all()

print("\nYou can add new animals without changing Zoo code:")

class Elephant(Animal):
    """Add new animal tomorrow - Zoo still works!"""
    
    def make_sound(self) -> None:
        print("Trumpet!")


zoo.add_animal(Elephant("Dumbo"))
zoo.make_all_sounds()  # Works with Elephant too!

"""
═══════════════════════════════════════════════════════════════════
THE MAGIC: Extensibility
═══════════════════════════════════════════════════════════════════

You wrote Zoo TODAY - it works with ANY Animal subclass (even ones
that don't exist yet)!

When someone adds Elephant TOMORROW:
- Zoo code DOESN'T CHANGE
- Elephant just needs to inherit from Animal
- Polymorphism makes it work!

This is the POWER of OOP:
Write flexible, extensible code that adapts to future changes.

═══════════════════════════════════════════════════════════════════
SENIOR PRINCIPLES SUMMARY
═══════════════════════════════════════════════════════════════════

1. Encapsulation: "This is my internal data, don't touch!"
2. Abstraction: "Use these methods, ignore implementation!"
3. Inheritance: "Reuse common code, avoid duplication!"
4. Polymorphism: "Different types, same interface!"

Together: Code that is Safe, Clear, Reusable, and Extensible
"""