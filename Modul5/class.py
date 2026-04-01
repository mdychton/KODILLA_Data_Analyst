class Car:
   pass

my_car = Car()
type(my_car)




"""
Metoda – funkcja, która jest zdefiniowana w obrębie klasy. 
Konstruktor – funkcja, która służy do tworzenia nowych instancji klasy.
Atrybut – zmienna, która jest zdefiniowana na poziomie klasy.
Instancja – obiekt, który jest utworzony na podstawie klasy.
Klasa – szablon, który definiuje strukturę i zachowanie obiektów.
Obiekt – instancja klasy, która posiada swoje własne dane i zachowanie.
np. Klasa Car może mieć atrybuty takie jak marka, model, rok produkcji, a także metody takie jak start() i stop(). Instancja tej klasy, np. my_car, będzie miała swoje własne wartości dla tych atrybutów i będzie mogła wywoływać te metody. Mozwli nam to tworzenie wielu obiektów na podstawie tej samej klasy, co jest jednym z głównych celów programowania obiektowego.      
"""


"ZMIENNA SELF to konwencja w języku Python, która odnosi się do pierwszego argumentu metody w klasie. Jest to sposób na odwołanie się do instancji klasy, na której metoda jest wywoływana. Kiedy definiujemy metodę w klasie, musimy uwzględnić self jako pierwszy argument, aby mieć dostęp do atrybutów i innych metod tej instancji. Kiedy wywołujemy metodę na instancji, Python automatycznie przekazuje tę instancję jako argument self. Dzięki temu możemy manipulować danymi i zachowaniem konkretnej instancji klasy, co jest kluczowe dla programowania obiektowego."


class Car:
   def __init__(self, make, model_name, top_speed, color):
       self.make = make                 #to marka :-)
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
print(mustang)

print(mustang.make)

"""
Udało nam się zdefiniować konkretny przypadek – instancję klasy Car, przypisaną do zmiennej mustang. Opisuje ona żółtego Forda Mustanga o prędkości maksymalnej 250 km/h.

Do konkretnych pól klasy, możemy się dostać za pomocą notacji instancja.pole, tak samo będziemy się również odwoływać do metod zdefiniowanych w obrębie klasy.
"""

"""
🔹 Klasa (class)

To taki szablon / plan na obiekt.

👉 Przykład:
Klasa to „przepis na samochód”, ale to jeszcze nie jest konkretny samochód.

class Samochod:
    pass
🔹 Obiekt / Instancja

To konkretny egzemplarz klasy.

👉 Czyli:

klasa = plan domu 🏠
obiekt = konkretny dom
auto1 = Samochod()
auto2 = Samochod()

➡️ auto1 i auto2 to obiekty (instancje)

🔹 Atrybuty

To cechy obiektu (dane).

👉 Np. kolor, marka, rok

class Samochod:
    def __init__(self, marka, kolor):
        self.marka = marka
        self.kolor = kolor

➡️ marka i kolor to atrybuty

🔹 Metody

To funkcje w klasie (czyli co obiekt potrafi zrobić)

class Samochod:
    def __init__(self, marka):
        self.marka = marka

    def jedz(self):
        print("Samochód jedzie")

➡️ jedz() to metoda

🔹 self (najważniejsze!)

To odwołanie do konkretnego obiektu

👉 Czyli:
„ten konkretny egzemplarz”

class Samochod:
    def __init__(self, marka):
        self.marka = marka  # zapisujemy do tego konkretnego obiektu

    def pokaz_marke(self):
        print(self.marka)
🔹 Jak to działa razem?
auto = Samochod("Toyota")

auto.pokaz_marke()

➡️ Python zamienia to w tle na:

Samochod.pokaz_marke(auto)

➡️ czyli self = auto

🔹 Podsumowanie w 1 zdaniu:
klasa = plan
obiekt/instancja = konkretny egzemplarz
atrybut = cecha (dane)
metoda = akcja (funkcja)
self = „ten konkretny obiekt”


"""