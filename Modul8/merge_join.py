"""
🔹 1. merge() — jak SQL JOIN

👉 To jest najważniejsza funkcja (używaj jej najczęściej)

📌 Dane wejściowe
import pandas as pd

left = pd.DataFrame({
    'A': ['A0','A1','A2','A3'],
    'key': ['key0','key1','key2','key3']
})

right = pd.DataFrame({
    'B': ['B0','B1','B2','B3'],
    'key': ['key0','key1','key2','key3']
})
🔹 INNER JOIN (część wspólna)
pd.merge(left, right, on='key', how='inner')
# bierze tylko te key, które są w obu tabelach

📊 wynik:

A   key   B
A0  key0  B0
A1  key1  B1
...
🔹 LEFT JOIN
pd.merge(left, right, on='key', how='left')
# bierze wszystko z left + dopasowanie z right
🔹 RIGHT JOIN
pd.merge(left, right, on='key', how='right')
# bierze wszystko z right
🔹 OUTER JOIN
pd.merge(left, right, on='key', how='outer')
# wszystko z obu tabel
🔥 Konflikt kolumn
left = pd.DataFrame({'A': [1], 'key': ['k']})
right = pd.DataFrame({'A': [2], 'key': ['k']})

pd.merge(left, right, on='key')

➡️ wynik:

A_x   key   A_y
1     k     2

✔️ pandas automatycznie dodaje _x i _y

🔹 Wybór kolumn ([[ ]])
pd.merge(left, right[['key', 'B']], on='key')
# bierzemy tylko 'key' i 'B' z prawej tabeli
🔹 2. [] vs [[]] (MEGA WAŻNE)
df['A']
# → Series (jedna kolumna)

df[['A']]
# → DataFrame (nadal tabela)

df[['A', 'B']]
# → DataFrame z 2 kolumnami

📌 zapamiętaj:

[] → jedna kolumna
[[]] → lista kolumn
🔹 3. join() — działa po indeksie

👉 bardziej „techniczna” funkcja

📌 przykład
left = pd.DataFrame({
    'A': ['A0','A1'],
    'key': ['k0','k1']
})

right = pd.DataFrame({
    'B': ['B0','B1']
}, index=['k0','k1'])
🔹 join
left.join(right, on='key')
# left.key → right.index
⚠️ ważne

👉 right MUSI mieć klucz jako indeks

🔹 Twój przypadek
left.join(right.set_index('key'), on='key')

✔️ działa

❌ błąd który miałeś
ValueError: columns overlap but no suffix specified

👉 bo masz:

A B C D w obu tabelach
🔧 fix
left.join(
    right.set_index('key'),
    on='key',
    lsuffix='_left',
    rsuffix='_right'
)
🔹 4. Różnica MERGE vs JOIN (najprościej)
cecha	merge ✅	join 🔧
po kolumnach	✔️	⚠️ (tylko jedna strona)
po indeksie	✔️	✔️
SQL-like	✔️	❌
łatwość	👍	😐
🔹 5. Bardzo ważny trick (który użyłeś)
left.merge(right[['key']], on='key')

👉 to NIE dodaje kolumn
👉 to filtruje

✔️ efekt:

= inner join tylko po key
= zostają dopasowane rekordy
🔥 TL;DR

👉 używaj:

merge()

👉 join() tylko gdy:

pracujesz na indeksach
wiesz co robisz


🧠 MERGE vs JOIN — obraz w głowie
🔹 Wyobraź sobie dane
LEFT                RIGHT
-----               -----
key  A              key  B
k0   A0             k0   B0
k1   A1             k1   B1
k2   A2             kX   B2
🔷 MERGE (SQL style)
left.merge(right, on='key', how='inner')

📊 wynik:

key  A   B
k0   A0  B0
k1   A1  B1

👉 tylko wspólne wartości

🔹 wszystkie typy JOIN w merge
INNER
k0, k1
LEFT
left.merge(right, on='key', how='left')
key  A   B
k0   A0  B0
k1   A1  B1
k2   A2  NaN
RIGHT
key  A   B
k0   A0  B0
k1   A1  B1
kX   NaN B2
OUTER
key  A    B
k0   A0   B0
k1   A1   B1
k2   A2   NaN
kX   NaN  B2
🔷 JOIN (index-based)

👉 teraz zmieniamy RIGHT:

right = right.set_index('key')
       B
key
k0     B0
k1     B1
kX     B2
JOIN
left.join(right, on='key')

📊 wynik (LEFT JOIN domyślnie):

key  A   B
k0   A0  B0
k1   A1  B1
k2   A2  NaN
🔥 KLUCZOWA RÓŻNICA
MERGE
kolumna ↔ kolumna
JOIN
kolumna ↔ indeks
🔷 [] vs [[]] (wizualnie)
df = pd.DataFrame({
    'A': [1,2],
    'B': [3,4]
})
🔹 jedna kolumna
df['A']

➡️

1
2

👉 Series

🔹 jedna kolumna jako DataFrame
df[['A']]

➡️

A
1
2

👉 nadal tabela

🔹 dwie kolumny
df[['A','B']]

➡️

A  B
1  3
2  4
🔥 PRO TIP (bardzo ważny)
left.merge(right[['key']], on='key')

👉 działa jak:

FILTER (INNER JOIN)

✔️ usuwa niedopasowane rekordy
❌ nie dodaje nowych kolumn

🚀 TL;DR (zapamiętaj to)

👉 90% przypadków:

merge()

👉 join() tylko gdy:

pracujesz na indeksie

👉 [['A','B']] = wybór wielu kolumn


============ZADANIA-=================

🧪 Zadanie 1 — podstawowy merge
📌 Dane
import pandas as pd

left = pd.DataFrame({
    'user_id': [1, 2, 3],
    'name': ['Adam', 'Ewa', 'Jan']
})

right = pd.DataFrame({
    'user_id': [1, 2, 4],
    'score': [100, 200, 300]
})
❓ Pytanie

Połącz tak, żeby:

były wszystkie osoby z left
dodać score jeśli istnieje
✅ Rozwiązanie
left.merge(right, on='user_id', how='left')
🧠 Co się dzieje
user_id  name  score
1        Adam  100
2        Ewa   200
3        Jan   NaN

✔️ 3 nie ma w right → NaN

🧪 Zadanie 2 — filtr (bardzo częste)
📌 Dane
orders = pd.DataFrame({
    'order_id': [1,2,3,4],
    'user_id': [10,20,30,40]
})

active_users = pd.DataFrame({
    'user_id': [10,30]
})
❓ Pytanie

Zostaw tylko zamówienia aktywnych użytkowników

✅ Rozwiązanie
orders.merge(active_users[['user_id']], on='user_id')
🧠 Wynik
order_id  user_id
1         10
3         30
🔥 Co tu jest ważne

👉 to jest:

INNER JOIN = filtr

👉 [['user_id']] → unikamy zbędnych kolumn

🧪 Zadanie 3 — join + indeks
📌 Dane
left = pd.DataFrame({
    'product': ['A','B','C'],
    'category_id': [1,2,3]
})

right = pd.DataFrame({
    'category_name': ['food','tech','clothes']
}, index=[1,2,3])
❓ Pytanie

Dodaj category_name do left używając join

✅ Rozwiązanie
left.join(right, on='category_id')
🧠 Wynik
product  category_id  category_name
A        1            food
B        2            tech
C        3            clothes
🔥 Co tu się dzieje
left.category_id → right.index
🧪 BONUS (częsty błąd)
❌
left.join(right, on='category_id')

👉 jeśli right NIE ma indeksu ustawionego → ❌

✅ fix
right = right.set_index('category_id')
🚀 MINI CHECKLISTA (interview)

👉 Chcesz dodać kolumny →

merge()

👉 Chcesz filtrować →

merge(...[['key']])

👉 Masz indeks →

join()


"""