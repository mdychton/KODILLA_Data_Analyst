import sqlite3
from sqlite3 import Error

import os
print(os.path.abspath("database.db"))   # pokazuje gdzie jest plik bazy danych

def create_tables(conn):
    sql = """                   -- twrorzymy dwie tabele: Projekt i Zadanie, z relacją 1 do wielu (jeden projekt może mieć wiele zadań) TO NIE JEST KOMENATRZ, TO JEST KOD SQL
    PRAGMA foreign_keys = ON;       --To jest ważne, aby włączyć obsługę kluczy obcych w SQLite, ponieważ domyślnie jest ona wyłączona. Dzięki temu możemy zapewnić integralność danych między tabelami Projekt i Zadanie.

    CREATE TABLE IF NOT EXISTS Projekt (
        id INTEGER PRIMARY KEY AUTOINCREMENT,             --komentarze w SQL są oznaczane dwoma myślnikami -- AUTOINCREMENT oznacza, że id będzie automatycznie zwiększane o 1 dla każdego nowego rekordu     
        nazwa TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT
    );

    CREATE TABLE IF NOT EXISTS Zadanie (
        id INTEGER PRIMARY KEY,
        project_id INTEGER,
        nazwa TEXT NOT NULL,
        opis TEXT,
        status TEXT,
        start_date TEXT,
        end_date TEXT,
        FOREIGN KEY (project_id) REFERENCES Projekt(id) ON DELETE CASCADE -- ON DELETE CASCADE oznacza, że jeśli usuniemy projekt, to wszystkie zadania związane z tym projektem również zostaną usunięte
    );
    """
    try:
        cursor = conn.cursor()
        cursor.executescript(sql)
        print("Tabele utworzone")
    except Error as e:
        print(e)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")

        create_tables(conn)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_connection("database.db")