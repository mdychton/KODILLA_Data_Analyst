"""
🔹 Główna różnica
.loc → działa na etykietach (nazwach)
.iloc → działa na pozycjach (numerach)
🔸 Przykład
import pandas as pd

df = pd.DataFrame({
    'e1': [80, 85, 90],
    'e2': [75, 88, 92]
}, index=['Student A', 'Student B', 'Student C'])
🔹 .loc → po nazwie
df.loc['Student B']

➡️ zwróci wiersz dla Student B

df.loc['Student B', 'e1']

➡️ konkretną wartość

🔹 .iloc → po numerze
df.iloc[1]

➡️ drugi wiersz (bo liczymy od 0)

df.iloc[1, 0]

➡️ wiersz 1, kolumna 0

🔥 Najważniejsze różnice
1. Nazwy vs liczby
df.loc['Student B']   # OK
df.iloc['Student B']  # ❌ błąd
df.iloc[1]            # OK
df.loc[1]             # ❌ (chyba że masz indeks = 1)
2. Zakresy (to często myli!)
df.loc['Student A':'Student B']

➡️ włącznie z końcem (A i B)

df.iloc[0:2]

➡️ bez końca (czyli 0 i 1)

3. Dodawanie danych
df.loc['Student D'] = [70, 80]

➡️ ✅ działa (dodaje nowy wiersz)

df.iloc[3] = [70, 80]

➡️ ❌ błąd (bo .iloc nie dodaje nowych)

🔹 Szybkie porównanie
operacja	loc	iloc
wybór po nazwie	✅	❌
wybór po pozycji	❌	✅
dodawanie wierszy	✅	❌
zakres (range)	inclusive	exclusive
💡 Intuicja (najważniejsze)
używaj .loc, gdy myślisz: "Student B, kolumna e1"
używaj .iloc, gdy myślisz: "drugi wiersz, pierwsza kolumna"
🔥 Tip z życia (bardzo ważny)

Jeśli masz indeks tekstowy (jak u Ciebie: Student A):
👉 używaj .loc prawie zawsze


🔹 Wyobraź sobie tabelę
import pandas as pd

df = pd.DataFrame({
    'e1': [80, 85, 90],
    'e2': [75, 88, 92]
}, index=['Student A', 'Student B', 'Student C'])

Wygląda tak:

            e1   e2
Student A   80   75
Student B   85   88
Student C   90   92
🔥 KLUCZOWA RÓŻNICA

👉 .loc = używasz nazw (etykiet)
👉 .iloc = używasz numerów (pozycji)

🧠 1. .loc — jak Excel (po nazwie)

Myślisz:

„Chcę Student B i kolumnę e1”

df.loc['Student B', 'e1']

➡️ wynik: 85

🔹 więcej przykładów

👉 cały wiersz:

df.loc['Student B']

👉 jedna kolumna:

df.loc[:, 'e1']

👉 zakres:

df.loc['Student A':'Student B']

➡️ dostajesz A i B (koniec wliczony!)

🧠 2. .iloc — jak lista (po numerze)

Numerujemy:

            e1   e2
0 (A)       80   75
1 (B)       85   88
2 (C)       90   92

👉 drugi wiersz:

df.iloc[1]

👉 konkretna wartość:

df.iloc[1, 0]

➡️ 85

👉 zakres:

df.iloc[0:2]

➡️ bierze:

0
1
❌ nie bierze 2
⚠️ NAJWIĘKSZA PUŁAPKA
🔹 .loc vs .iloc range
df.loc['Student A':'Student B']

➡️ A i B

df.iloc[0:2]

➡️ też A i B… ale tylko dlatego, że 2 jest wyłączone

🔥 NAJWAŻNIEJSZE PRZYKŁADY
❌ To NIE działa
df.loc[1]

➡️ bo nie masz indeksu 1

df.iloc['Student B']

➡️ bo to nie liczba

✅ To działa
df.loc['Student B']   # po nazwie
df.iloc[1]            # po pozycji
🔥 DODAWANIE (mega ważne)
.loc potrafi dodać:
df.loc['Student D'] = [70, 60]
.iloc NIE:
df.iloc[3] = [70, 60]

➡️ ❌ błąd

💡 PROSTE PORÓWNANIE
Myślenie	użyj
"Student B"	.loc
"drugi wiersz"	.iloc
"kolumna e1"	.loc
"pierwsza kolumna"	.iloc
🧠 INTUICJA (najważniejsze)

👉 .loc = czytasz tabelę jak człowiek
👉 .iloc = czytasz tabelę jak Python (liczby)






"""