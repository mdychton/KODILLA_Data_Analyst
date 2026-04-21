"""
Najprostszy przykład
import numpy as np

arr = np.array([1, 2, 3])
arr + 10

👉 wynik:

[11 12 13]
🔍 Co się stało?

NumPy traktuje 10 jak:

[10, 10, 10]

👉 ale nie tworzy tej tablicy fizycznie (oszczędność pamięci)

📌 Broadcasting z dwiema tablicami
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b

👉 wynik:

[11 22 33]
📌 Broadcasting z różnymi wymiarami
a = np.array([[1],
              [2],
              [3]])   # shape (3,1)

b = np.array([10, 20, 30])  # shape (3,)
a + b

👉 wynik:

[[11 21 31]
 [12 22 32]
 [13 23 33]]
🔍 Jak to działa „pod spodem”?

NumPy „rozciąga” mniejsze wymiary:

a: (3,1)  → kolumna
b: (1,3)  → wiersz (automatycznie)

=> wynik: (3,3)
📏 Zasady broadcastingu (kluczowe)

Porównujemy wymiary od końca:

✔️ Warunki zgodności:
Są równe
Jeden z nich = 1
✅ Przykład OK:
(3,1)
(1,3)

👉 wynik:

(3,3)
❌ Przykład błędu:
(3,2)
(3,3)

👉 nie działa (bo 2 ≠ 3 i ≠ 1)

📌 Broadcasting w praktyce (masking)
arr = np.array([0, 5, 10, 15, 20])
arr > 10

👉 wynik:

[False False False True True]

👉 NumPy porównuje KAŻDY element do 10 (bez pętli)

📌 Broadcasting w macierzach
arr = np.array([[1,2,3],
                [4,5,6]])

arr + np.array([10,20,30])

👉 wynik:

[[11 22 33]
 [14 25 36]]

👉 wektor został „rozciągnięty” na każdy wiersz

🧠 Intuicja (bardzo ważne)

Broadcasting =
👉 „dopasuj kształty tak, żeby dało się zrobić operację element po elemencie”

🔥 Typowe zastosowania
dodawanie stałej do tablicy
normalizacja danych
operacje na macierzach
masking (np. arr > 10)
⚠️ Najczęstsze błędy

❌ brak zgodności wymiarów
❌ zapominanie o reshape()

📌 Przydatne narzędzia
a.reshape(3,1)   # zmiana kształtu
a[:, np.newaxis] # dodanie wymiaru
🧠 Podsumowanie
broadcasting usuwa potrzebę pętli
działa „wirtualnie” (bez kopiowania danych)
wymaga zgodności wymiarów
jest podstawą maskowania i operacji NumPy

"""