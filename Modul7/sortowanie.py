"""
🔑 SORTOWANIE W NUMPY
📌 1. Losowa tablica
import numpy as np

arr = np.random.randint(1, 40, 10)
# 10 losowych liczb z zakresu 1–39
📌 2. sort() vs sort()
🔹 funkcja np.sort() (kopiuje dane)
np.sort(arr)
🧠 co robi:
zwraca posortowaną kopię
NIE zmienia oryginalnej tablicy
📌 przykład:
print(arr)          # oryginał
print(np.sort(arr)) # posortowana kopia
print(arr)          # nadal bez zmian
🔹 zapis do zmiennej
arr = np.sort(arr)

👉 teraz nadpisujesz dane

📌 3. sortowanie malejące
arr = np.sort(arr)[::-1]
🧠 co to robi:
np.sort() → rosnąco
[::-1] → odwrócenie kolejności
📌 4. metoda .sort() (zmienia oryginał)
arr.sort()
🧠 różnica:
działa „w miejscu”
zmienia oryginalną tablicę
📊 porównanie:
metoda	kopia?	zmienia arr?
np.sort()	tak	nie
arr.sort()	nie	tak
📌 5. sortowanie macierzy (axis)
arr2d = np.array([np.arange(1,6),
                  np.arange(6,1,-1)]).reshape(5,2)
🔹 sortowanie wierszy (domyślnie)
np.sort(arr2d)

👉 sortuje KAŻDY wiersz osobno

🔹 sortowanie kolumn
np.sort(arr2d, axis=0)
🧠 co robi:
axis=0 → kolumny
sortuje pionowo
📌 6. Structured Array (strukturalne tablice)
🔹 definicja typu danych
dt = np.dtype([('student','S10'),
               ('exam1', int),
               ('exam2', int)])
🧠 tłumaczenie:
student → tekst (10 znaków)
exam1 → liczba
exam2 → liczba
🔹 dane
a = np.array([
    ("Student A", 89, 74),
    ("Student B", 85, 56),
    ("Student C", 93, 44),
    ("Student D", 83, 92)
], dtype=dt)
📌 7. sortowanie po polach
🔹 po exam1
np.sort(a, order='exam1')

👉 sortuje według pierwszego egzaminu

🔹 po exam2
np.sort(a, order='exam2')

👉 sortuje według drugiego egzaminu

📌 8. najlepszy student (max exam2)
np.sort(a, order='exam2')[-1][0]
🧠 co to znaczy:
[-1] → ostatni (największy wynik)
[0] → nazwa studenta
📌 9. argsort (bardzo ważne!)
np.argsort(arr)
🔍 co zwraca?

👉 NIE wartości
👉 tylko indeksy po sortowaniu

📊 przykład:
arr = [50, 10, 30]

np.argsort(arr)

👉 wynik:

[1, 2, 0]
🧠 interpretacja:
10 (index 1)
30 (index 2)
50 (index 0)
🔥 DLACZEGO argsort jest ważny?

Bo możesz:

arr[np.argsort(arr)]

👉 i dostajesz sortowanie (manualnie kontrolowane)

🧠 PODSUMOWANIE
📌 sortowanie:
np.sort() → kopia
.sort() → zmienia oryginał
📌 odwracanie:
[::-1]
📌 macierze:
axis=0 → kolumny
axis=1 → wiersze
📌 structured arrays:
sortowanie po nazwanych polach
📌 argsort:
zwraca indeksy sortowania
używane w fancy indexing
🔥 Najważniejszy wzór:
arr[np.argsort(arr)]


"""