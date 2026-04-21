"""
📊 Agregowanie danych w NumPy
🔑 Co to jest agregacja?

👉 Agregacja = podsumowanie danych

Czyli np.:

suma
średnia
minimum
maksimum
📌 1. Podstawowe funkcje agregujące
import numpy as np

arr = np.arange(0, 101, 10)

👉 tablica:

[0 10 20 30 40 50 60 70 80 90 100]
➕ suma
arr.sum()
# suma wszystkich elementów
📊 średnia
arr.mean()
# average (średnia arytmetyczna)
🔽 minimum
arr.min()
# najmniejsza wartość
🔼 maksimum
arr.max()
# największa wartość
📌 2. Agregacja w macierzach (axis)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
🔽 minimum po kolumnach
arr_2d.min(axis=0)

👉 wynik:

[1 2 3]

📌 tłumaczenie:

axis=0 → kolumny
🔽 minimum po wierszach
arr_2d.min(axis=1)

👉 wynik:

[1 4 7]

📌 tłumaczenie:

axis=1 → wiersze
📌 3. Inne statystyki
np.median(arr_2d)  # mediana
np.var(arr_2d)     # wariancja
np.std(arr_2d)     # odchylenie standardowe
🧠 Tłumaczenia:
median = mediana (wartość środkowa)
variance = wariancja (rozrzut danych)
standard deviation = odchylenie standardowe
⚠️ 4. Dzielenie tablicy przez siebie
arr = np.arange(0, 101, 10)

arr / arr
📌 Co się dzieje?

Tablica:

[0 10 20 30 ... 100]

Operacja:

0 / 0  → ❌ (normalnie błąd w Pythonie)
🚨 Wynik NumPy:
nan  1.  1.  1. ... 1.
🔍 Co to jest nan?

👉 NaN = Not a Number
= brak wartości / nieokreślony wynik

⚠️ NumPy vs Python
Python	NumPy
błąd (ZeroDivisionError)	nan + warning
🔕 5. Wyłączanie ostrzeżeń
defaults = np.seterr(all='ignore')

👉 wyłącza warningi (np. dzielenie przez 0)

🔙 6. Przywrócenie ustawień
_ = np.seterr(**defaults)
🧠 PODSUMOWANIE
📊 Agregacja:
.sum() → suma
.mean() → średnia
.min() → minimum
.max() → maksimum
📏 axis:
axis=0 → kolumny
axis=1 → wiersze
⚠️ NumPy specjalne zachowania:
0/0 → nan (nie błąd)
warning zamiast crasha
🔥 Najważniejsza idea

👉 NumPy NIE przerywa obliczeń
👉 tylko oznacza problem jako nan

"""