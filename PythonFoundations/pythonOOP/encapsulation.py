"""
Encapsulation is protecting an objects data and methods based on its' scope
this means an object keeps its own data private and only lets you change it in safe, controlled ways.
e.g. 
you can press the buttons on a TV remote but you can not touch the wires inside.
e.g. 
If a car is a class, you press the gas pedal
You dont directly inject fuel into the engine
The car protects itself from misuse
"""
#code example
class Car:
    def __init__(self, fuel):
        self.fuel = fuel
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Accelerating to {self.speed} km/h")
    def brake(self):
        self.speed = max(0, self.speed - 10)
        print(f"Braking to {self.speed} km/h")

car = Car(100)
car.accelerate()
car.brake()
"""
As like other languages like java, python also has levels of protection for variables
e.g. speed is public, _speed is protected, __speed is private
- public variables can be accessed from outside the class
- protected variables can be accessed from the class and its subclasses
- private variables can only be accessed from the class
"""
#python protected variables
class Truck:
    def __init__(self):
        self.fuel = 100           # Public (anyone can access)
        self._condition = "good"  # Protected (hint: private, but not enforced by python, linters will warn you)
        self.__engine = None      # Private (name mangling, harder to access)

truck = Truck()
print(truck.fuel)        # Works
print(truck._condition)  # Works (but linters will warn you)
print(truck.__engine)    # AttributeError! (Python can't access the name)

"""
Choosing when to Use Public, Protected, Private is about INTENT and INTERFACE DESIGN, not enforcement.

PUBLIC (no underscore): 
Use for methods and attributes users of your class SHOULD use
Use for: Methods and attributes users of your class SHOULD use

Example: car.accelerate(), car.get_speed()
Philosophy: "This is the official API. Use this."
When: Part of your contract with users

Risk: Users might depend on implementation details. Harder to change later.
Solution: Document clearly, use type hints, keep API stable


PROTECTED (_underscore):
Use for: Internal implementation, but subclasses might need it

Example: _validate_speed(), _calculate_fuel_consumption()
Philosophy: "This is internal. Don't use from outside, but subclasses can."
When: Helper methods, things that might be overridden by subclasses

Risk: Requires discipline. Linter warns, but not enforced.
Solution: Code review catches violations. Document WHY it's protected.


PRIVATE (__double_underscore)
Use for: Core state that breaks the class if modified externally
Example: __engine, __battery, __transaction_log
Philosophy: "This is implementation. You don't need to know it exists."
When: State that would violate class invariants if modified

Risk: Still accessible via name mangling (_ClassName__private), but ugly.
Solution: Anyone accessing private this way is explicitly breaking contract.

Summary:
1. Start with PUBLIC for everything
2. When you realize something shouldn't be modified externally → use PROTECTED (_)
3. When you realize something shouldn't be KNOWN about externally → use PRIVATE (__)

"""
# Example:
class BankAccount:
    def __init__(self, initial_balance: float):
        self.__balance = initial_balance  # PRIVATE - core state
    
    def deposit(self, amount: float) -> None:  # PUBLIC - main API
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
    
    def _record_transaction(self, amount: float) -> None:  # PROTECTED - helper
        # Subclasses might override this to log differently
        pass
    
    def get_balance(self) -> float:  # PUBLIC - read-only access
        return self.__balance

# Users do this:
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Safe, controlled

# Users DON'T do this:
account.__balance = -1000     # NameError! Protected by Python

# Example: Bad Design
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance  # PUBLIC - tempts users to modify

# Users might do this:
account = BadBankAccount(1000)
account.balance = -1000000  # Breaks invariant! No validation!



"""
Python doesn't enforce access levels like Java/C# do.
Instead, protection comes from:

1. GOOD API DESIGN
   - Public methods do one job and do it well
   - Methods validate inputs, maintain invariants
   - Users use the API naturally

2. TYPE HINTS
   - Communicate what types methods expect/return
   - Linter enforces type safety
   - Users know what's safe

3. DOCUMENTATION
   - Explain what users should do
   - Explain what happens if they break the contract
   - Make intent crystal clear

4. TESTS
   - Verify the API works as documented
   - Show proper usage examples
   - Catch misuse

5. CODE REVIEW
   - Catch people breaking contracts
   - Question access to protected members
   - Suggest better patterns

REMEMBER: Public, Protected, Private are COMMUNICATION TOOLS, not safety walls.
Python trusts developers. Design your classes to make right usage obvious
and wrong usage obvious (so code review catches it).

"""