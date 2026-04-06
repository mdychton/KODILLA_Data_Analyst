"""
W Pythonie dostępne są dwie funkcje wbudowane, które zostały zaprojektowane specjalnie po to, by wspomagać dziedziczenie obiektów: isinstance() oraz issubclass().

Pozwalają one rozpoznać czy obiekt, na którym działamy, jest instancją danej klasy, lub czy dwie klasy są ze sobą związane poprzez mechanizm dziedziczenia

"""

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



truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
truck.accelerate()
print(truck.current_speed)
print(truck)

print(isinstance(truck, Truck))  # sprawdza czy obiekt truck jest instancją klasy Truck
print(isinstance(truck, Car))    # sprawdza czy obiekt truck jest instancją klasy Car
print(issubclass(Truck, Car))    # sprawdza czy klasa Truck jest podklasą klasy Car
print(issubclass(Car, Truck))    # sprawdza czy klasa Car jest podklasą klasy Truck
print(isinstance(car, Car) ) # sprawdza czy obiekt car jest instancją klasy Car
print(isinstance(car, Truck)) # sprawdza czy obiekt car jest instancją klasy Truck