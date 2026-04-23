"""
🔹 1. Co robi rename()

👉 rename() służy do:

zmiany nazw kolumn
zmiany nazw indeksów (wierszy)

💡 Najważniejsze:

nie musisz zmieniać wszystkiego — tylko to, co chcesz

📊 Przykładowy DataFrame
import pandas as pd

df = pd.DataFrame({
    'e1': [80, 85, 90],
    'e2': [75, 88, 92],
    'e3': [70, 83, 95]
}, index=['Student A', 'Studnet B', 'Studnet C'])
🔹 2. Zmiana nazw KOLUMN
df.rename(columns={
    'e1': 'exam1',
    'e2': 'exam2',
    'e3': 'exam3'
})
💡 komentarz:
# zmieniamy tylko nazwy kolumn
# stare nazwy -> nowe nazwy
# reszta kolumn zostaje bez zmian
🔥 efekt:
        exam1  exam2  exam3
Student A  80     75     70
...
⚠️ WAŻNE
df.rename(...)

👉 NIE zmienia oryginalnego DataFrame

Musisz zrobić:

df = df.rename(columns={'e1': 'exam1'})

albo:

df.rename(columns={'e1': 'exam1'}, inplace=True)
🔹 3. Zmiana nazw WIERSZY (indeksu)
df.rename(index={
    'Studnet B': 'Student B'
})
💡 komentarz:
# poprawiamy literówkę w indeksie
# tylko jeden wiersz jest zmieniany
🔥 efekt:
Student B zamiast "Studnet B"
🔹 4. Zmiana wszystkich nazw funkcją

👉 to jest mocniejsze 🔥

df.rename(str.upper, axis='columns')
💡 komentarz:
# str.upper -> zamienia tekst na wielkie litery
# axis='columns' -> działa na kolumnach
🔥 efekt:
E1  E2  E3
🔹 5. To samo dla wierszy
df.rename(str.upper, axis='index')
💡 komentarz:
# zamienia indeksy (nazwy wierszy) na wielkie litery
🔥 6. axis — co to znaczy?
axis	co oznacza
'columns' / 1	kolumny
'index' / 0	wiersze
🧠 INTUICJA
columns → nazwy “u góry tabeli”
index → nazwy “po lewej stronie”
🔥 7. Najważniejsze porównanie
metoda	co robi
rename()	zmienia wybrane nazwy
set_index()	zamienia kolumnę w indeks
df.columns = [...]	nadpisuje wszystkie kolumny
df.index = [...]	nadpisuje wszystkie wiersze
💡 Kiedy używać rename()?

👉 gdy:

masz literówkę
zmieniasz nazwy kolumn na bardziej czytelne
nie chcesz ruszać całej struktury
🔥 PRO TIP (praktyka)

Najczęściej w pracy robisz:

df.rename(columns={
    'old_name': 'new_name'
})

albo:

df.rename(str.lower, axis=1)
🧠 PROSTA INTUICJA

👉 rename() = “popraw etykiety bez ruszania danych”
👉 set_index() = “zmień strukturę tabeli”

"""