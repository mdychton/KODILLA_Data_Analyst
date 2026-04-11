

"""
1. INSERT — dodawanie danych (Projekt + Zadanie)

import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# --- DODAJEMY PROJEKT ---
cursor.execute("""
INSERT INTO projects (nazwa, start_date, end_date)
VALUES (?, ?, ?)
""", ("Aplikacja CRM", "2026-04-01", "2026-06-01"))

project_id = cursor.lastrowid  # ID właśnie dodanego projektu

# --- DODAJEMY ZADANIE PRZYPISANE DO PROJEKTU ---
cursor.execute("""
INSERT INTO tasks (project_id, nazwa, opis, status, start_date, end_date)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    project_id,
    "Login system",
    "Stworzenie logowania użytkowników",
    "in progress",
    "2026-04-02",
    "2026-04-10"
))

conn.commit()
conn.close()


-------------------------------------------------------
2. JOIN — łączenie tabel

import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    projects.nazwa,
    tasks.nazwa,
    tasks.status
FROM tasks
JOIN projects ON tasks.project_id = projects.id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()




=-------------------------------------------------------
3. RELACJA 1:N

📌 PRZYKŁAD DANYCH
projects:
id	nazwa
1	CRM App
tasks:
id	project_id	nazwa
1	1	Login
2	1	Database
3	1	UI
🧠 CO TO OZNACZA?

👉 jeden projekt ma wiele zadań

🔥 LOGIKA:
projects (1)  →  tasks (many)
🟣 4. BONUS — jak to wygląda w Twoim systemie

Twoja baza:

projects
   ↓
tasks (project_id)
🔥 CASCADE (ważne!)

Masz:

ON DELETE CASCADE

👉 jeśli usuniesz projekt:

DELETE FROM projects WHERE id = 1;

👉 AUTOMATYCZNIE znikają taski

🧠 PODSUMOWANIE
🔹 INSERT

👉 dodajesz dane

🔹 lastrowid

👉 pobierasz ID nowego projektu

🔹 JOIN

👉 łączysz tabele

🔹 1→N

👉 jeden projekt = wiele zadań

🚀 Jeśli chcesz następny poziom

Mogę Ci pokazać:

UPDATE (zmiana statusu zadania)
DELETE (usuwanie projektu + cascade w praktyce)
albo mini API w Pythonie do tej bazy (jak backend)


"""