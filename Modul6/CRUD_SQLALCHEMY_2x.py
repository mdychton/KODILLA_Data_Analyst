🚀 🔥 CRUD ŚCIĄGAWKA (SQLAlchemy 2.x)

Załóżmy tabelę: students

from sqlalchemy import select, insert, update, delete
🟢 CREATE (INSERT) – dodawanie danych
stmt = insert(students).values(name="Jan", lastname="Kowalski")
# tworzy zapytanie INSERT → dodaje nowy rekord

with engine.begin() as conn:
    conn.execute(stmt)
    # begin() = automatyczny commit
🔵 READ (SELECT) – czytanie danych
stmt = select(students.c)
# wybiera wszystkie kolumny z tabeli students

with engine.connect() as conn:
    result = conn.execute(stmt)

    for row in result:
        print(row)
        # wypisuje każdy rekord
🟡 UPDATE – aktualizacja danych
stmt = update(students)\
    .where(students.c.id == 1)\
    .values(name="Adam")
# zmienia imię dla rekordu o id = 1

with engine.begin() as conn:
    conn.execute(stmt)
    # zapisuje zmianę
🔴 DELETE – usuwanie danych
stmt = delete(students).where(students.c.id == 1)
# usuwa rekord o id = 1

with engine.begin() as conn:
    conn.execute(stmt)
    # wykonuje usunięcie
🧠 NAJWAŻNIEJSZE ZASADY
✔ SELECT = czytanie
select()
✔ INSERT = dodawanie
insert()
✔ UPDATE = zmiana
update()
✔ DELETE = usuwanie
delete()
⚡ KLUCZOWE RÓŻNICE (BARDZO WAŻNE)
Operacja	connection
SELECT	engine.connect()
INSERT/UPDATE/DELETE	engine.begin()
💡 DLACZEGO begin()?

👉 bo automatycznie robi:

start transakcji
commit
rollback jeśli błąd
🧠 MINI FLOW (zapamiętaj)
1. import
2. stmt = ...
3. engine.begin() → execute
🚀 ULTRA SKRÓT
# CREATE
insert(students).values(...)

# READ
select(students.c)

# UPDATE
update(students).where(...).values(...)

# DELETE
delete(students).where(...)