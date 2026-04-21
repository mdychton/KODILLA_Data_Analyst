"""
O co chodzi w maskowaniu (masking)?

Maskowanie = filtrowanie danych na podstawie warunku

👉 zamiast pętli robisz:

arr[warunek]
📌 1. Tworzenie tablicy
import numpy as np

arr = np.arange(0, 50, 5)  
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
📌 2. Tworzenie maski (warunku)
arr > 15

👉 wynik:

[False False False False True True True True True True]
🔍 Co się dzieje?
NumPy sprawdza KAŻDY element (bez pętli!)
to dzięki broadcastingowi
📌 3. Filtrowanie danych
arr[arr > 15]

👉 wynik:

[20 25 30 35 40 45]
🧠 Zasada:
True → bierz
False → pomiń
📌 4. Łączenie warunków (AND)
arr[(arr > 15) & (arr != 40)]

👉 wynik:

[20 25 30 35 45]
🔑 ważne:
& = AND (i)
nawiasy są obowiązkowe!
📌 5. OR (lub)
arr[(arr < 10) | (arr >= 20)]

👉 wynik:

[ 0  5 20 25 30 35 40 45]
🔑 operator:
| = OR
📌 6. Inne operatory
^   # XOR (tylko jeden warunek True)
~   # NOT (odwraca True/False)
📌 7. Alternatywa (funkcje NumPy)
np.logical_or(arr < 10, arr >= 20)

👉 to samo co:

(arr < 10) | (arr >= 20)
📌 8. Indeksy zamiast wartości
np.where(arr <= 43)

👉 wynik:

(array([0, 1, 2, 3, 4, 5, 6, 7, 8]),)

👉 czyli: gdzie spełniony warunek (indeksy)

🧠 PODSUMOWANIE (najważniejsze)
arr > 10 → tworzy maskę (True/False)
arr[mask] → filtruje dane
&, |, ^, ~ → łączenie warunków
np.where() → zwraca indeksy


==============================================
cwiczenia


Ćwiczenia
Wyfiltruj z arr tylko te wartości, które są mniejsze od 10 lub większe bądź równe 20, ale jednocześnie różne od liczby 40. (gdzie arr = np.arange(0,50,5)).
Wykorzystując operator XOR, stwórz macierz o kształcie (4,4), której elementy po głównej przekątnej mają wartość logiczną False, a pozostałe wartość True.

✅ Zadanie 1
📌 Dane:
import numpy as np

arr = np.arange(0, 50, 5)
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
📌 Warunki:
< 10
LUB ≥ 20
ALE ≠ 40
✅ Rozwiązanie:
result = arr[((arr < 10) | (arr >= 20)) & (arr != 40)]
print(result)
📌 Wynik:
[ 0  5 20 25 30 35 45]
✅ Zadanie 2 (XOR + macierz)
📌 Cel:
przekątna → False
reszta → True
✅ Rozwiązanie:
m = np.ones((4, 4), dtype=bool)   # wszystko True
diag = np.eye(4, dtype=bool)      # przekątna True

result = m ^ diag                 # XOR
print(result)
📌 Wynik:
[[False  True  True  True]
 [ True False  True  True]
 [ True  True False  True]
 [ True  True  True False]]
🧠 Dlaczego XOR działa?
True ^ True = False → przekątna
True ^ False = True → poza przekątną


"""