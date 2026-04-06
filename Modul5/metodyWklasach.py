class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

    # <-- __str__ MUSI BYĆ TU, z tym samym wcięciem co __init__
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
    
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
    
    def __eq__(self, other):
        return all(
        (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
        )
    )

    def __gt__(self, other):
        return self.top_speed > other.top_speed


"""
    def __eq__(self, other):
        return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
    )
"""


mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car  #po co to jest ?

print(mustang)
print(car)

"""
__eq__, __gt__, __ge__, __lt__, __le__ 
"""
car_one = Car(make="Fiat", model_name="Mustang", top_speed=550, color="Red")                       #do tego odnosi sie def eg - ale to porównuje tylko 2 wartosci jesli jest wiecej jak tu to najpierw porownuje 1-2 a pozniej 2-3 itd . Chyba ze uzyje sie wbudowanej funcji all
car_two = Car(make="Fiat", model_name="Mustang", top_speed=350, color="Red")
car_three = Car(make="Fiat", model_name="Mustang", top_speed=350, color="Red")
car_one == car_two
car_one > car_two               # czyli najpierw musze miec zdefiniowana gt a pozniej taki zapis umozliwi porowainie
print(car_one==car_two==car_three)
print(car_one > car_two)

car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: car.top_speed)
print()
by_make = sorted(cars, key=lambda car: car.make)

print(cars)
# eg z all

#Python ma wbudowaną funkcję all(), która zwraca True, jeśli wszystkie wartości do niej przekazane również są prawdziwe. W przeciwnym przypadku zwróci False.





"""
Zwróć uwagę, że metoda all() przyjmuje zmienną, po której można iterować, czyli np. krotkę lub listę.

Podobną funkcją jest any(). Ona z kolei zwróci True, jeśli którykolwiek z przekazanych argumentów będzie prawdą.

Wspomniane funkcje są bardzo praktyczne w momentach, kiedy potrzebujesz sprawdzić jednocześnie wiele warunków logicznych.
"""
#print(mustang)
#print(mustang.make)

#  print(dir(Car)) metody w klasie Car


#__str__ Jest to metoda, która odpowiada za wygląd obiektu klasy, gdy przedstawimy go jako string, na przykład przy przekazaniu go do funkcji print()


"""<__main__.Car object at 0x10792ff28>
Pewnie zastanawiasz się, skąd w ogóle ten dziwny “numer” - 0x10792ff28? 
Oznacza on dokładny adres w pamięci, pod którym znajduje się obiekt. 
Jednak taka informacja niewiele mówi o tym, czym jest obiekt, który wydrukowaliśmy na konsoli.
"""

#__repr__

"""
Ta metoda odpowiada za to, jak obiekt jest przedstawiony w interpreterze.
Z założenia, wynik __str__ powinien być czytelny i przeznaczony dla końcowego użytkownika programu lub skryptu.
Natomiast wynik __repr__ jest adresowany głównie do programistów i wyszukiwania problemów w kodzie (debugowania).
Przykładowo, dla użytkownika najważniejszą informacją o instancji klasy Car może być zawartość pola name. 
Jednak, gdy programista natrafia na problem i chciałby się dowiedzieć od razu, czym jest dany obiekt, może chcieć odczytać wartości wszystkich pól jednocześnie – samo pole make nie powie mu wiele.
"""


"""
Operator	Funkcja	Znaczenie
>	__gt__(self, other)	ang. greater than – większy niż
>=	__ge__(self, other)	ang. greater or equal – większy lub równy
<	__lt__(self, other)	ang. less than – mniejszy niż
<=	__le__(self, other)	ang. less or equal – mniejszy lub równy
==	__eq__(self, other)	ang. equal – równy

"""