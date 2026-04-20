import numpy as np

"""
🔪 Slicing w Pythonie (i NumPy)

Slicing to sposób na wycinanie fragmentów tablicy w NumPy (i listach Pythona).

Ogólny zapis wygląda tak:

tablica[start:stop:step]
📌 Twój przykład
my_arr[5:15:5]

Rozbijmy to:

🔹 5 → start

👉 zaczynamy od indeksu 5 (włącznie)

🔹 15 → stop

👉 kończymy przed indeksem 15 (czyli 15 NIE jest w wyniku)

🔹 5 → step (krok)

👉 bierzemy co 5-ty element

🧠 Co to oznacza w praktyce?

Wyobraź sobie:

indeksy:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ...

Slicing:

my_arr[5:15:5]

Czyli:

start → 5
stop → 15 (nie włącznie)
step → co 5 elementów

👉 wybieramy więc:

index 5
index 10
📊 Wynik logiczny:
[my_arr[5], my_arr[10]]
⚡ Jak zapamiętać
🧩 format:
[start : stop : step]
🧠 znaczenie:
start → gdzie zaczynam
stop → gdzie kończę (bez tej wartości)
step → co ile przeskakuję
🔥 Przykłady dla utrwalenia
my_arr[2:10:2]   # co drugi element od 2 do 9
my_arr[:5]       # od początku do 4
my_arr[5:]       # od 5 do końca
my_arr[::2]      # co drugi element w całej tablicy
💡 Najważniejsze

👉 slicing NIE zmienia danych
👉 tylko wybiera fragment
👉 działa bardzo szybko (bez kopiowania logiki pętli)


📌 Slicing i indexing w NumPy (prosto)
import numpy as np   # import biblioteki NumPy
🔹 1. Tworzenie tablicy
my_arr = np.arange(21)   # tworzy liczby od 0 do 20

👉 wynik:
[0, 1, 2, 3, ..., 20]

🔹 2. Indexing (pojedynczy element)
my_arr[10]   # bierze element o indeksie 10

👉 zwraca jedną liczbę

🔹 3. Slicing (wycinanie fragmentu)
my_arr[5:15]   # elementy od 5 do 14 (15 nie wchodzi)

👉 wycina fragment tablicy

🔹 4. Slicing z krokiem (step)
my_arr[5:15:5]   # od 5 do 14 co 5 elementów

👉 działa tak:

start = 5
stop = 15
step = 5

👉 wynik: [5, 10]

📌 5. Tablica 2D
two_dim = np.array([
    [0,10,20],
    [5,15,25],
    [100,200,300]
])   # tworzy macierz 3x3
🔹 6. Indexing w 2D
two_dim[0]   # pierwszy wiersz
two_dim[1][0]   # element z 2. wiersza i 1. kolumny
🔹 7. Slicing w 2D (ważne!)
two_dim[1:3, :2]

👉 tłumaczenie:

[wiersze, kolumny]
1:3 → bierz wiersze 1 i 2
:2 → bierz kolumny 0 i 1

👉 czyli:

najpierw wybierasz WIERSZE
potem KOLUMNY
📌 8. Fancy indexing (bardziej zaawansowane)
my_arr = np.arange(25).reshape(5,5)   # macierz 5x5
🔹 wybór pojedynczych wierszy
my_arr[[0,1]]   # bierze wiersz 0 i 1
🔹 „korespondencyjne” wybieranie (ważne!)
my_arr[[0,1],[0,4]]

👉 oznacza:

(0,0)
(1,4)

👉 czyli pary indeksów

📌 9. Indeksy jako tablica
vals = np.array([100,5,0])   # baza wartości
select = np.random.randint(0,3,size=(4,3))   # losowe indeksy
🔹 użycie tablicy jako indeksów
vals[select]

👉 każdy numer w select wybiera wartość z vals

🧠 Najprostsze zasady
x[i] → jeden element
x[a:b] → fragment
x[a:b:c] → fragment co c
x[:, :] → 2D (wiersze, kolumny)
x[[...]] → fancy indexing (wybór listą)
🚀 Najważniejsze w 1 zdaniu

👉 slicing = wycinanie fragmentów
👉 indexing = wybieranie konkretnych elementów
👉 fancy indexing = wybieranie „po listach indeksów”

🧠 8. Fancy indexing – co to naprawdę znaczy?

Fancy indexing = indeksowanie listą / tablicą indeksów, a nie pojedynczą liczbą albo zakresem.

🔹 1. Macierz 5x5
my_arr = np.arange(25).reshape(5,5)

👉 tworzy:

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
🔹 2. Wybór wierszy
my_arr[[0,1]]
🧠 co to znaczy?

👉 podajesz listę: [0,1]

czyli:

weź wiersz 0
weź wiersz 1
📌 wynik:
[[0 1 2 3 4]
 [5 6 7 8 9]]
🔥 WAŻNE

To NIE jest slicing (0:2), tylko:

👉 „daj mi dokładnie te wiersze”

🔥 3. „Korespondencyjne” wybieranie (najważniejsze)
my_arr[[0,1],[0,4]]

To jest najtrudniejsze — ale działa bardzo logicznie.

🧠 Jak to czytać?

Masz DWIE listy:

[0, 1]   → wiersze
[0, 4]   → kolumny

👉 NumPy łączy je parami:

wiersz	kolumna	element
0	0	0
1	4	9
📌 wynik:
[0, 9]
🧠 KLUCZOWA ZASADA

👉 NIE wybierasz:

całych wierszy
całych kolumn

👉 tylko konkretne punkty:

(0,0) → 0
(1,4) → 9
📌 9. Indeksy jako tablica (bardzo ważne)
vals = np.array([100,5,0])

👉 mamy „słownik” wartości:

index:  0   1   2
value: 100  5   0
🔹 losowe indeksy
select = np.random.randint(0,3,size=(4,3))

👉 np. może wyglądać tak:

[[0 2 1]
 [1 1 0]
 [2 0 2]
 [1 2 0]]
🔥 10. Najważniejsze: indeksowanie tablicą
vals[select]
🧠 co się dzieje?

Każda liczba w select to:

👉 indeks do vals

📌 przykład:

vals = [100, 5, 0]

i:

select:
[[0 2]
 [1 0]]
🔄 zamiana:
0 → 100
2 → 0
1 → 5
0 → 100
📌 wynik:
[[100   0]
 [  5 100]]
🚀 Najprostsze podsumowanie
🔹 slicing

👉 wybierasz zakres

🔹 indexing

👉 wybierasz pojedyncze elementy

🔹 fancy indexing

👉 wybierasz „listą indeksów”

🔹 advanced (pary)

👉 (wiersz, kolumna) jako punkty w macierzy

💡 Najważniejsze zdanie

👉 Fancy indexing = NumPy traktuje listy indeksów jako „instrukcję wyboru konkretnych elementów”, a nie zakres.

"""