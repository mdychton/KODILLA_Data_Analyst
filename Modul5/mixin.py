#klasa mixin to klasa, która jest przeznaczona do bycia dziedziczoną przez inne klasy, ale sama w sobie nie jest przeznaczona do tworzenia instancji. Klasy mixin są używane do dodawania dodatkowych funkcjonalności do innych klas bez konieczności tworzenia hierarchii dziedziczenia.
class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

        self._current_speed = 0

    def __str__(self):                      #bez tego bedzie taki output <__main__.Truck object at 0x000001EE86626A50>
        return f"{self.color} {self.make} {self.model_name}"
    
    def accelerate(self, step=10):
       self.current_speed += step

    def decelerate(self, step=10):
       self.current_speed -= step

    @property       
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
            

class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
        super().__init__(*args, **kwargs)  #funkcja super() służy do odwołania się do klasy, po której odziedziczyliśmy. Dzięki niej możemy wywołać konstruktor klasy Car, przekazując mu wszystkie argumenty, których potrzebuje do poprawnego zainicjalizowania obiektu. W ten sposób unikamy konieczności ręcznego przepisywania kodu z konstruktora klasy Car do konstruktora klasy Truck.  
        self.max_load = max_load            #Pamiętaj, że funkcji super() możesz użyć w dowolnej metodzie w klasie-dziecku.



class DieselEngine:
   def tank(self, how_many=100):
       print(f"Adding {how_many} liters of Diesel")

class PetrolEngine:
   def tank(self, how_many=20):
       print(f"Adding {how_many} liters of Petrol")

class Truck(Car, DieselEngine):

   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class SportCar(Car, PetrolEngine):
   pass


truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
porsche = SportCar(make="Porsche", model_name="911", color="Red", top_speed=250)
truck.tank()
porsche.tank()

