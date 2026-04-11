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
        cursor = conn.cursor()          # tworzy kursor (narzędzie do wykonywania SQL)
        cursor.executescript(sql)       # wykonuje CAŁY skrypt SQL (wiele komend naraz)
        print("Tabele utworzone")
    except Error as e:                  # jesli wystąpi błąd, to go wyświetlamy
        print(e)

def create_connection(db_file):            #funkcja tworząca połączenie z bazą danych
    conn = None                             # na początku nie mamy połączenia, więc ustawiamy na None
    try:                                     # próbujemy połączyć się z bazą danych
        conn = sqlite3.connect(db_file)        #jesli database.db nie istnieje, to zostanie utworzony automatycznie, a jesli istnieje, to zostanie otwarty
        print(f"Connected to {db_file}")

        create_tables(conn)             # po nawiązaniu połączenia, tworzymy tabele w bazie danych

    except Error as e:                  # jesli wystąpi błąd, to go wyświetlamy
        print(e)
    finally:                            # na koniec, niezależnie od tego, czy wystąpił błąd, czy nie, zamykamy połączenie z bazą danych, ta sekwencja jest ważna, aby zwolnić zasoby i uniknąć problemów z blokowaniem bazy danych i wykona sie zawsze, nawet jeśli wystąpi błąd podczas tworzenia tabel    
        if conn:
            conn.close()                # zamyka połączenie z bazą danych, to NIE usuwa pliku — tylko zamyka dostęp do bazy danych, ale plik nadal istnieje na dysku

if __name__ == '__main__':              #ten blok uruchamia się tylko gdy plik jest odpalany bezpośrednio,nie uruchomi się przy imporcie
    create_connection("database.db")    # tworzy połączenie z bazą danych i tworzy tabele, jeśli baza danych nie istnieje, to zostanie utworzona automatycznie, a jeśli istnieje, to zostanie otwarta i tabele zostaną utworzone (jeśli jeszcze nie istnieją)   



    """
    DODATKOWE INFORMACJE:

    GDZIE POWSTAJE database.db?

👉 tutaj:

sqlite3.connect("database.db")

📌 lokalizacja zależy od:
👉 folderu, z którego uruchamiasz skrypt

Dlatego masz:

print(os.path.abspath("database.db"))

➡️ żeby to sprawdzić dokładnie

💥 KIEDY BAZA PRZESTAJE ISTNIEĆ?

👉 TYLKO gdy:

❌ usuniesz plik ręcznie:
rm database.db
❌ albo w Pythonie:
import os
os.remove("database.db")
❗ WAŻNE
conn.close()

➡️ NIE usuwa bazy
➡️ tylko zamyka połączenie

🔴 CO MUSI BYĆ W KONKRETNYM MIEJSCU
1. importy — NA GÓRZE

👉 zawsze na początku pliku

2. funkcje (def ...) — PRZED użyciem
create_tables(conn)

👉 funkcja musi być zdefiniowana wcześniej

3. if __name__ == '__main__':

👉 na dole pliku
👉 to „entry point” programu

4. kolejność logiczna:
połączenie (connect)
tworzenie tabel
zamknięcie

👉 jeśli zamkniesz wcześniej → nie zadziała

🧠 PODSUMOWANIE

👉 connect() → tworzy plik bazy
👉 executescript() → tworzy tabele
👉 conn.close() → tylko zamyka połączenie
👉 baza istnieje dopóki plik .db istnieje na dysku



📌 kolejność jest zawsze taka:
1. connect()  → otwierasz bazę
2. cursor()   → tworzysz „pilot do bazy”
3. execute()  → wykonujesz SQL

conn = „brama do bazy”

Bez niej:

❌ nie ma dostępu do pliku
❌ nie można wykonać SQL
❌ nie można stworzyć tabel
    

Wyobraź sobie:

🏦 baza danych = bank
database.db = budynek banku
conn = wejście + dostęp
cursor = pracownik banku
execute() = wykonywanie operacji

najważniejsze zdanie do zapamiętania

👉 Nie wykonujesz SQL w Pythonie
👉 tylko w bazie danych, przez połączenie (conn)


    """