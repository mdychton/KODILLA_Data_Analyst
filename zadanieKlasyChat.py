class Vehicle:
    def move(self):
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("The car is driving.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying.")
              
              
vehicles = [Car(), Boat(), Plane()]
for vehicle in vehicles:
    vehicle.move()

"""
In this code, we have a base class `Vehicle` with a method `move()`.
 We then have three subclasses: `Car`, `Boat`, and `Plane`, each overriding the `move()` method to provide specific behavior."""


#print(Car.move(vehicles[0]))  # This will call the move method of the Car class
#print(Boat.move(vehicles[1]))  # This will call the move method of the Boat class
#print(Plane.move(vehicles[2]))  # This will call the move method of the


