# Parent class: Animal
class Animal:
    def move(self):
        pass  # We will override this method in subclasses

# Subclass: Car
class Car(Animal):
    def move(self):
        print("Driving ")

# Subclass: Plane
class Plane(Animal):
    def move(self):
        print("Flying ")

# Creating instances of Car and Plane
car = Car()
plane = Plane()

# Calling the move method (demonstrating polymorphism)
car.move()   # Output: Driving 
plane.move()  # Output: Flying 
