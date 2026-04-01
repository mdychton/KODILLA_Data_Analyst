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


mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)

car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car  #po co to jest ?

print(mustang)
print(car)


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


