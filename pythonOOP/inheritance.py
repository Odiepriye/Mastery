"""
Inheritance is a way to create a new class from an existing class
this means that the new class inherits all the properties and methods of the existing class
the new class inherits all the properties and methods of the existing class
the new class can add new properties and methods or override the existing ones
e.g. a car is a vehicle, so a car inherits from the vehicle class
the car class can add new properties and methods or override the existing ones
"""
#Inheritance example
class Vehicle:
    def __init__(self, fuel):
        self._fuel = fuel
        self._speed = 0
        self.__engine = "V8"
        self.__transmission = "Automatic"
        self.__brakes = "Brakes"
        self.__steering = "Steering"

    def accelerate(self):
        self._speed += 10
        self._fuel -= 1
        print(f"Accelerating to {self._speed} km/h")

class Car(Vehicle):
    def stop(self):
        self._speed = 0
        print(f"Stopping at {self._speed} km/h")

car = Car(100)
car.accelerate()
car.stop()

# Multi-level Inheritance
class Animal:
    def __init__(self):
        self.__born = True
    def get_born(self):
        return self.__born

class Mammal(Animal):  # Mammal inherits from Animal
    def __init__(self):
        super().__init__() #without this, the Animal class will not be initialized
        self.__hair = True
    def get_hair(self):
        return self.__hair

class Dog(Mammal):  # Dog inherits from Mammal (which inherits from Animal)
    pass

dog = Dog()
print(dog.get_born())
print(dog.get_hair())

# Multiple Inheritance
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):  # Inherits from both!
    pass

duck = Duck()
duck.fly()     # From Flyer
duck.swim()    # From Swimmer