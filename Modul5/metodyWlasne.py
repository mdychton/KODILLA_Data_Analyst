class Car:

   def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

       # Variables
       self.current_speed = 0
    
    

   def accelerate(self, step=10):
       self.current_speed += step

   def decelerate(self, step=10):
       self.current_speed -= step

   def set_current_speed(self, value):
        if value <= self.top_speed:
            self.current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")


car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car.current_speed
car.accelerate(50)
car.decelerate(20)
print(car.current_speed)