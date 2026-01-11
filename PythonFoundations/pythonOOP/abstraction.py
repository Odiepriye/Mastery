"""
Abstraction is hiding the complex details and showing only the essential features of an object
this means making simple interfaces for complex objects
e.g. a car is an object, you dont need to know how the engine works, you just need to know how to use the car
"""
#code example
class Car:
    def __init__(self, fuel):
        self._fuel = fuel
        self._speed = 0
        self.__engine = "V8"
        self.__transmission = "Automatic"
        self.__brakes = "Brakes"
        self.__steering = "Steering"

    def accelerate(self):
        if self._fuel > 0:
            self._speed += 10
            self._fuel -= 1
        else:
            print("Not enough fuel")
        print(f"Accelerating to {self._speed} km/h")

car = Car(100)
car.accelerate()

"""
How to Implement Abstraction

1. ENCAPSULATION (Private/Protected Variables)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Hide internal state behind private variables.
   Users can't see or modify internals.
   
   Bad:
   class Car:
       self.engine = "V8"      # Users shouldn't see this
       self.fuel = 100         # Users shouldn't modify directly
   
   Good:
   class Car:
       self.__engine = "V8"    # Private - users don't see it
       self._fuel = 100       # Private - users don't modify it

2. SENSIBLE METHOD NAMING & I/O
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Public methods should be named for WHAT users want to do, not HOW.
   
   Bad:
   def __adjust_ignition_timing():        # Users don't care about this
   def __increase_fuel_injection():       # Implementation detail
   
   Good:
   def accelerate(self) -> None:          # Users understand this
   def brake(self) -> None:               # Clear intent
   def refuel(self, amount: float) -> None:  # What users want to do

3. TYPE HINTS & DOCUMENTATION
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Make it obvious what users SHOULD do and what they SHOULDN'T.
   
   def accelerate(self) -> None:
       \"\"\"Increase car speed by 10 km/h.
       
       Internally handles:
       - Fuel consumption
       - Engine management
       - Transmission shifting
       
       Users don't need to know any of this!
       \"\"\"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEY PRINCIPLE: Users Should Know WHAT, Not HOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Users know:          "I want to accelerate the car"
Users DON'T know:    "How fuel injection, spark plugs, gears work"
They call:           car.accelerate()
They don't care:     About __engine, __transmission, __fuel details
This is ABSTRACTION.

SUMMARY: The Three Tools Working Together

Encapsulation (private __variables)
    ↓ Makes internals invisible
    ↓
Sensible Public Methods (accelerate(), brake(), refuel())
    ↓ Shows what users CAN do
    ↓
Type Hints & Documentation (communicate intent)
    ↓ Explains what they SHOULD do
    ↓
Result: Simple, Safe, Clear Interface
"""