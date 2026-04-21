"""
🔑 O co chodzi (Statystyki / ufunc)?

NumPy ma specjalne funkcje:
👉 ufunc (universal functions)

📌 Co robią?
działają na tablicach (ndarray)
wykonują operacje element po elemencie
korzystają z broadcastingu (czyli bez pętli)
📌 Dane wejściowe
import numpy as np

arr = np.arange(0, 101, 10)
# [  0  10  20  30  40  50  60  70  80  90 100]
📌 1. Pierwiastek (square root)
np.sqrt(arr)
🧾 Komentarz:
# np.sqrt() → oblicza pierwiastek kwadratowy z każdego elementu
# działa element po elemencie (bez pętli)
📌 Wynik:
# [ 0.          3.16  4.47  5.47  6.32  7.07  7.74  8.36  8.94  9.48 10. ]
🇬🇧 Tłumaczenie:
square root = pierwiastek kwadratowy
📌 2. Sinus
np.sin(arr)
🧾 Komentarz:
# np.sin() → liczy sinus dla każdego elementu
# UWAGA: wartości w radianach (nie stopniach!)
📌 Wynik (przykładowy):
# [ 0.         -0.544  0.913 -0.988 ... ]
🇬🇧 Tłumaczenie:
sine = sinus
📌 3. Mnożenie
np.multiply(arr, 2)
🧾 Komentarz:
# np.multiply() → mnoży elementy
# tutaj: każdy element * 2

👉 to samo co:

arr * 2
📌 Wynik:
# [  0  20  40  60  80 100 120 140 160 180 200]
🇬🇧 Tłumaczenie:
multiply = mnożyć
🔍 Dlaczego to działa?

Dzięki broadcastingowi:

arr * 2

👉 NumPy traktuje 2 jak:

[2,2,2,2,...]
🧠 Co warto zapamiętać
✔️ ufunc = funkcje elementowe
działają na całych tablicach
są szybkie (wektorowe)
nie wymagają pętli
🔥 Najczęstsze ufunc
np.sqrt()      # pierwiastek
np.sin()       # sinus
np.cos()       # cosinus
np.exp()       # e^x
np.log()       # logarytm
np.multiply()  # mnożenie
np.add()       # dodawanie
🧠 Podsumowanie (prosto)
NumPy robi operacje na całej tablicy naraz
każda wartość liczona osobno (element-wise)
broadcasting „dopasowuje” dane automatycznie
🔥 Najważniejszy pattern
np.funkcja(arr)

👉 zamiast:

for x in arr:
    ...

    
======================

⚔️ NumPy vs pętla (wydajność)
📌 Dane
import numpy as np

arr = np.arange(1_000_000)  # 1 milion elementów
🐢 1. Python (pętla)
result = []
for x in arr:
    result.append(x * 2)
🧾 Co się dzieje:
Python iteruje element po elemencie
dużo narzutu (wolne)
🚀 2. NumPy (wektorowo)
result = arr * 2
🧾 Co się dzieje:
operacja na całej tablicy naraz
wykorzystuje C pod spodem → bardzo szybkie
⏱️ Różnica czasu (typowo)
Metoda	Czas
Pętla Python	~0.2–0.5 s
NumPy	~0.002 s

👉 NumPy może być nawet 100x szybszy

🔍 Dlaczego NumPy jest szybszy?
1. Brak pętli w Pythonie
# Python
for x in arr:

vs

# NumPy
arr * 2

👉 pętla jest „ukryta” i napisana w C

2. Operacje na blokach pamięci
NumPy działa na ciągłej pamięci
CPU może to lepiej zoptymalizować
3. Broadcasting
arr * 2

👉 nie tworzy kopii [2,2,2,...]

🧠 Intuicja
Python → „idź po kolei”
NumPy → „zrób wszystko naraz”
🔥 Realny przykład (porównanie)
import time
import numpy as np

arr = np.arange(1_000_000)

# Python loop
start = time.time()
result = [x * 2 for x in arr]
print("Loop:", time.time() - start)

# NumPy
start = time.time()
result = arr * 2
print("NumPy:", time.time() - start)
🧠 Wniosek (bardzo ważny)

👉 Jeśli używasz NumPy:

❌ unikaj pętli
✅ używaj operacji wektorowych
🔥 Zasada do zapamiętania

„Jeśli piszesz pętlę w NumPy — robisz coś źle”

======================================================
CWICZENIA


Ćwiczenia
Stwórz program, który ze wskazanej macierzy wyciągnie odpowiednio najmniejszą i największą wartość dla każdego wiersza.
[[0 4 1]
[2 0 4]]
Stwórz wektor Z według następującego wzoru: np.random.uniform(0,1,10). Następnie znajdź element, który jest najbliższy wartości 0.5.
Stwórz wektor zawierający 20 losowych wartości, a następnie zamień jego największą wartość na 0.
Znajdź części całkowite tablicy, wykorzystując przynajmniej dwa różne sposoby.


✅ Zadanie 1

Najmniejsza i największa wartość w każdym wierszu

import numpy as np

arr = np.array([[0, 4, 1],
                [2, 0, 4]])

# minimum w każdym wierszu (axis=1 → wiersze)
min_vals = arr.min(axis=1)

# maksimum w każdym wierszu
max_vals = arr.max(axis=1)

print("min:", min_vals)
print("max:", max_vals)
📌 Wynik:
min: [0 0]
max: [4 4]
🧠 Wyjaśnienie:
axis=1 → operujemy po wierszach
każdy wiersz daje jedną wartość
✅ Zadanie 2

Element najbliższy 0.5

Z = np.random.uniform(0, 1, 10)

# liczymy odległość od 0.5
dist = np.abs(Z - 0.5)

# indeks najmniejszej różnicy
idx = dist.argmin()

# najbliższa wartość
closest = Z[idx]

print("Z:", Z)
print("najbliższy do 0.5:", closest)
🧠 Wyjaśnienie:
Z - 0.5 → różnica
np.abs() → wartość bezwzględna
argmin() → indeks najmniejszej wartości
✅ Zadanie 3

Zamień największą wartość na 0

Z = np.random.random(20)

# znajdź indeks największego elementu
idx = Z.argmax()

# zamień na 0
Z[idx] = 0

print(Z)
🧠 Wyjaśnienie:
argmax() → indeks największej wartości
potem normalna zmiana elementu
✅ Zadanie 4

Części całkowite – 2 sposoby

arr = np.array([5, 0.0249139 , 0.11873564, 0., 0.72321586,
                11308494, 0.29931472, 0.24439968, 0.61251754, 4])
🔹 Sposób 1: astype(int)
int_part1 = arr.astype(int)

# konwersja typu → ucina część dziesiętną
🔹 Sposób 2: np.floor()
int_part2 = np.floor(arr)

# zaokrągla w dół
🔹 (bonus) Sposób 3: np.trunc()
int_part3 = np.trunc(arr)

# ucina część dziesiętną (jak astype)
📌 Wyniki (dla dodatnich liczb):
# wszystkie dadzą podobny efekt:
[5. 0. 0. 0. 0. 11308494. 0. 0. 0. 4.]
🧠 Różnice (ważne!)
metoda	działanie
astype(int)	ucina
floor()	w dół
trunc()	ucina

👉 różnice widać przy liczbach ujemnych!

🔥 PODSUMOWANIE
min(axis=1) / max(axis=1) → po wierszach
argmin() / argmax() → indeksy
np.abs() → odległość
astype, floor, trunc → część całkowita



"""