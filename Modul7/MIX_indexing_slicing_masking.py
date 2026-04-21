"""
🔑 IDEA: mieszanie technik

Możesz łączyć:

indexing → wybór po indeksach
slicing → zakresy
masking → warunki logiczne

👉 i robić bardzo precyzyjne filtrowanie

📌 1. Tworzymy macierz
import numpy as np

arr = np.arange(20).reshape(4, 5)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]
📌 2. Fancy indexing + slicing
arr[[3, 0, 1], :3]
🔍 Co to robi?
# [3,0,1] → wybiera wiersze w tej kolejności
# :3      → bierze pierwsze 3 kolumny
📌 Wynik:
# [[15 16 17]
#  [ 0  1  2]
#  [ 5  6  7]]

👉 WAŻNE:
To jest kopia, bo użyliśmy fancy indexing ([3,0,1])

📌 3. Masking + slicing
arr[arr.sum(axis=1) > 10, 2:]
🔍 Krok po kroku:
arr.sum(axis=1)
# suma każdego wiersza
# [10, 35, 60, 85]
arr.sum(axis=1) > 10
# [False, True, True, True]

👉 filtrujemy wiersze:

# bierzemy tylko wiersze 1,2,3

👉 potem slicing kolumn:

2:  # od kolumny index 2 do końca
📌 Wynik:
# [[ 7  8  9]
#  [12 13 14]
#  [17 18 19]]
🧠 Kluczowa zasada
arr[warunek_na_wiersze, zakres_kolumn]
=========================
✅ ĆWICZENIA
=========================
✅ Zadanie 1

Treść:
Weź wiersz o indeksie 2, ale tylko kolumny, których suma > 30

🔍 Krok 1 – suma kolumn:
arr.sum(axis=0)
# [30, 34, 38, 42, 46]
🔍 Krok 2 – maska:
arr.sum(axis=0) > 30
# [False, True, True, True, True]
✅ Rozwiązanie:
result = arr[2, arr.sum(axis=0) > 30]
print(result)
📌 Wynik:
[11 12 13 14]
✅ Zadanie 2
a = np.array([97,101,105,111,117,125])
b = np.array(['a','e','i','o','u','y'])
🔍 Warunek:
a > 100
a < 110
(a > 100) & (a < 110)
# [False, True, True, False, False, False]
✅ Rozwiązanie:
result = b[(a > 100) & (a < 110)]
print(result)
📌 Wynik:
['e' 'i']

👉 filtrujemy b na podstawie a

✅ Zadanie 3
arr2 = np.array([[0,4,1],
                 [2,0,4]])
🔍 najmniejsze w wierszach:
arr2.min(axis=1)
# [0, 0]
🔍 największe w wierszach:
arr2.max(axis=1)
# [4, 4]
✅ Rozwiązanie:
min_vals = arr2.min(axis=1)
max_vals = arr2.max(axis=1)

print(min_vals)
print(max_vals)
🧠 PODSUMOWANIE (mega ważne)
axis=0 → kolumny
axis=1 → wiersze
fancy indexing → kopia
slicing → widok
maskowanie działa jak filtr
🔥 Najważniejszy pattern:
arr[warunek, kolumny]
arr[wiersze, warunek]


"""