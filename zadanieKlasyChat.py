class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")


class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving.")


class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing.")


class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying.")
   
vehicles = [Car("Toyota"), 
            Boat("Sailboat"), 
            Plane("Airplane")]

for vehicle in vehicles:
    vehicle.move()

"""
In this code, we have a base class `Vehicle` with a method `move()`.
 We then have three subclasses: `Car`, `Boat`, and `Plane`, each overriding the `move()` method to provide specific behavior."""


#print(Car.move(vehicles[0]))  # This will call the move method of the Car class
#print(Boat.move(vehicles[1]))  # This will call the move method of the Boat class
#print(Plane.move(vehicles[2]))  # This will call the move method of the


