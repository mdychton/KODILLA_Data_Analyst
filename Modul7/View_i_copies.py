"""

🔑 Kluczowa idea
Basic indexing (slicing) → zwraca widok (view) → zmiany wpływają na oryginał
Fancy indexing → zwraca kopię (copy) → zmiany NIE wpływają na oryginał
📌 Najważniejsze komendy
1. Tworzenie tablicy
arr = np.arange(10)

👉 Tworzy tablicę od 0 do 9

2. Slicing (widok – view)
slice_of_arr = arr[:5]

👉 Pobiera pierwsze 5 elementów (widok, nie kopia)

slice_of_arr[:] = 100

👉 Zmienia wartości → zmienia też oryginalne arr

3. Fancy indexing (kopia)
fancy_index_arr = arr[np.arange(5)]

👉 Tworzy kopię pierwszych 5 elementów

fancy_index_arr[:] = 100

👉 Zmienia tylko kopię (oryginał bez zmian)

4. Sprawdzanie: view czy copy
slice_of_arr.base is None

👉 False → to widok

fancy_index_arr.base is None

👉 True → to kopia

slice_of_arr.base is arr

👉 True → widok pochodzi z arr

5. Wymuszenie kopii
slice_of_arr = arr[:5].copy()

👉 Tworzy niezależną kopię, bez wpływu na oryginał

6. Operacje na macierzy
macierz = np.arange(9).reshape(3, 3)

👉 Tworzy macierz 3x3

macierz[-1, -1] = 999

👉 Zmienia ostatni element

macierz[1:, 1:] = 0

👉 Zmienia prawy dolny fragment macierzy na 0

7. Zadanie (niezerowe indeksy)
np.nonzero(array)

👉 Zwraca indeksy elementów ≠ 0

Przykład:

np.nonzero(np.array([1,2,0,0,4,0]))

➡️ wynik: (array([0, 1, 4]),)

🧠 Najważniejsze do zapamiętania
[:] → zazwyczaj widok
fancy indexing ([lista_indeksów]) → kopia
.copy() → zawsze bezpieczna kopia
.base → sprawdzenie źródła danych



"""