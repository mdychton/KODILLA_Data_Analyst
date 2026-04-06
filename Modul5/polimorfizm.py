"""

Jeszcze prostszy przykład
class Dog:
    def sound(self):
        print("hau")

class Cat:
    def sound(self):
        print("miau")
animals = [Dog(), Cat()]

for a in animals:
    a.sound()

👉 wynik:

hau
miau

👉 to samo wywołanie → różne zachowanie

🔹 8. Jak to zapamiętać?

👉 słowo klucz:

„jedna metoda, wiele form”

(polimorfizm = poly + morph = wiele form)

🔹 9. Twój przypadek (najważniejsze!)

✔ masz:

c.contact()

✔ różne klasy:

BaseContact
BusinessContact

✔ różne zachowanie:

prywatny telefon
służbowy telefon

👉 ✔ TO JEST POLIMORFIZM

🔥 TL;DR
ta sama metoda (contact)
różne klasy
różne działanie

👉 Python sam wybiera właściwą wersję

🔥 Jedno zdanie na rozmowę

Polimorfizm pozwala wywoływać tę samą metodę na różnych obiektach, które zachowują się w różny sposób.

"""