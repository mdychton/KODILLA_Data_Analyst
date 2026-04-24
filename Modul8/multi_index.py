"""
🧠 MultiIndex w Pandas — wyjaśnienie krok po kroku
📌 Co to jest MultiIndex?
MultiIndex = indeks z więcej niż jednym poziomem

Czyli zamiast:

0
1
2

masz:

(School, Student)
🎯 Po co to robimy?

👉 żeby modelować hierarchię danych

np.:

szkoła → student
kraj → miasto
rok → miesiąc → dzień
📊 Twój przykład danych
exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3 = [67,59,79,84]

df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)

df['semester1'] = df['e1'] + df['e2'] + df['e3']

👉 mamy tabelę wyników studentów

🏗️ Tworzenie MultiIndex — 2 sposoby
✅ SPOSÓB 1: MultiIndex.from_tuples (najbardziej „czytelny”)
🔧 Kod:
schools = ['High School X','High School X','High School Y','High School Y']

# tworzymy pary (School, Student)
multi_index_list = [
    (school, student)
    for school, student in zip(schools, df.index)
]
🧠 Co tu się dzieje?
zip(schools, df.index)

👉 łączy dane w pary:

('High School X', 'Student A')
('High School X', 'Student B')
('High School Y', 'Student C')
('High School Y', 'Student D')
🔥 Tworzymy MultiIndex:
df.index = pd.MultiIndex.from_tuples(
    multi_index_list,
    names=['School','Student']
)
📌 Efekt:
School          Student
High School X   Student A
High School X   Student B
High School Y   Student C
High School Y   Student D
💡 Komentarz:
from_tuples = dajesz gotowe pary
names=[...] = nazwy poziomów indeksu
✅ SPOSÓB 2: set_index (szybszy)
df.set_index(
    [
        pd.Index(['High School X','High School X','High School Y','High School Y']),
        df.index
    ],
    inplace=True
)
🧠 Co się tu dzieje?

Tworzysz 2 poziomy:

level 1 → School (nowy Index)
level 2 → Student (stary index)
⚠️ minus tej metody:

👉 nie ma nazw indeksów

dlatego robisz:

df.index.names = ['School','Student']
🔍 Jak działa dostęp do danych
📌 1. .loc — najpierw poziom 1
df.loc['High School X']

👉 dostajesz wszystkich studentów z tej szkoły

📌 wynik:
Student A
Student B
📌 2. .iloc — pozycja w obrębie wyniku
df.loc['High School X'].iloc[1]

👉:

najpierw szkoła
potem drugi student
📌 3. .xs() — najbardziej „multiindexowy sposób”
🔹 tylko szkoła:
df.xs('High School Y')

👉 wszystkie wiersze tej szkoły

🔹 pełny dostęp (tuple):
df.xs(('High School Y','Student D'))

👉 dokładny rekord

🔹 po jednym poziomie:
df.xs('Student D', level='Student')

👉 szuka wszędzie, gdzie Student = D

🧠 KLUCZOWA INTUICJA
📌 loc vs xs
metoda	jak myśli Pandas
.loc['X']	„daj mi wszystko z poziomu X”
.xs(...)	„daj mi dane z dowolnego poziomu”
⚠️ ważna obserwacja (Twój wcześniejszy problem)

Jeśli robisz:

set_index(['School','Student','e1','e2','e3','semester1'])

👉 wtedy:

kolumny = ❌ puste
wszystko = indeks
🧠 TL;DR
MultiIndex:

👉 struktura hierarchiczna w indeksie

Tworzenie:
from_tuples → czytelne i bezpieczne
set_index → szybkie, ale łatwo przesadzić
Dostęp:
.loc → poziom 1
.iloc → pozycja
.xs → najlepsze do MultiIndex


"""