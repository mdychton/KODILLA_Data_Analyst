"""
🔥 1. Co to jest broadcasting (najprościej)

👉 Broadcasting = NumPy „dopasowuje” tablice, żeby dało się zrobić działanie element-po-elemencie

Czyli zamiast pisać pętle:

for i:
    a[i] + 10

NumPy robi:

👉 „OK, ja sobie sam rozciągnę 10 do rozmiaru tablicy”

🧠 2. „Rozciąganie” NIE oznacza kopiowania

To klucz:

👉 NumPy NIE tworzy nowych tablic
👉 tylko udaje, że 10 ma rozmiar [10,10,10]

📊 3. Przykład 1
arr = np.array([1,2,3])
arr + 10

👉 NumPy myśli:

10 → [10, 10, 10] (wirtualnie)

wynik:

[11, 12, 13]
🔥 4. Przykład 2 (2 tablice)
a = [1,2,3]
b = [10,20,30]

👉 działanie:

[1+10, 2+20, 3+30]

wynik:

[11, 22, 33]
📐 5. Najważniejsze: shape (kształt)

NumPy NIE patrzy na liczby, tylko na wymiary

Przykład:
a.shape = (3,1)
b.shape = (3,)
Co to znaczy?
a =
[[1]
 [2]
 [3]]
b = [10, 20, 30]
🔥 6. Co robi NumPy?

👉 dopasowuje brakujące wymiary:

a: (3,1)
b: (1,3)

👉 i „rozciąga”:

(3,3)
📊 7. Wynik
[[11 21 31]
 [12 22 32]
 [13 23 33]]
🧠 8. Jak to sobie wyobrazić?

👉 jak tabela:

      10  20  30
1
2
3

i każda liczba się „krzyżuje”

📏 9. Zasada broadcastingu (najważniejsza)

Porównujemy wymiary od końca:

✔ działa jeśli:

są równe
albo jeden = 1
Przykład OK:
(3,1)
(1,3)
→ (3,3)
❌ Przykład NIE działa:
(3,2)
(3,3)

👉 bo 2 ≠ 3 i ≠ 1

🔥 10. Masking = broadcasting w praktyce
arr > 10

NumPy robi:

[0,5,10,15,20] > 10

czyli:

[False, False, False, True, True]

👉 porównuje każdy element bez pętli

📐 11. Reshape — po co?

👉 reshape = zmiana „kształtu danych”

przykład:
a = [1,2,3]
a.reshape(3,1)

wynik:

[[1]
 [2]
 [3]]
🧠 12. newaxis (to samo co reshape)
a[:, np.newaxis]

👉 zamienia:

(3,)

na:

(3,1)
🔥 13. Najważniejsza intuicja

👉 broadcasting = „NumPy udaje, że tablice mają ten sam rozmiar”

👉 reshape = „Ty zmieniasz kształt tablicy”

💥 14. Najprostsze zdanie (do zapamiętania)

👉 Broadcasting = automatyczne dopasowanie wymiarów do działań matematycznych

🚀 TL;DR
broadcasting = „rozciąganie w tle”
reshape = „zmieniam strukturę”
NumPy działa bez pętli
wszystko opiera się o shape

"""