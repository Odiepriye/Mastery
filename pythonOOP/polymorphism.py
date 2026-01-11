"""
The ability to call the same method on different objects and get different behavior.
this means that the same method can be used for different classes, write code that can work with different classes.
e.g. a dog is an animal, so a dog can be called an animal
e.g. a cat is an animal, so a cat can be called an animal
"""
#code example
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} is speaking")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Bird(Animal):
    pass
dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")
#bad/not DRY code
dog.speak()
cat.speak()
bird.speak()
#good/DRY code
animals = [dog, cat, bird]
for animal in animals:
    animal.speak()