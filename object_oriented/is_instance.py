# Exercise 4 - Instance and Subclass
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(Dog, Animal))  # False (classes are not instances)
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
#print(issubclass(dog, Animal))  # Error (must be a class)