import sqlite3
from sqlite3 import Error

import os
print(os.path.abspath("database.db"))   # pokazuje gdzie jest plik bazy danych

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)  #jeśli plik nie istnieje → zostanie utworzony, jeśli istnieje → zostanie otwarty
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
       return conn    # zwracamy połączenie, aby można było z niego korzystać w innych funkcjach, np. do tworzenia tabel, dodawania danych itp. Jeśli nie zwrócimy połączenia, to nie będziemy mogli z niego korzystać poza tą funkcją, a to jest kluczowe do dalszej pracy z bazą danych   
   except Error as e:   # jeśli wystąpi błąd podczas próby połączenia z bazą danych, to zostanie on przechwycony i wyświetlony, a funkcja zwróci None, co pozwala na obsługę sytuacji, gdy połączenie nie może zostać nawiązane (np. z powodu błędnej ścieżki do pliku, braku uprawnień itp.)
       print(e)

   return conn  #jeśli błąd → zwraca None (brak połączenia)

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()   #tworzy „cursor” = narzędzie do wykonywania SQL
       c.execute(sql)    # wykonuje pojedynczą komendę SQL (np. CREATE TABLE, INSERT INTO itp.) nie jak executescript, która wykonuje cały skrypt SQL (wiele komend naraz)
       conn.commit()     # zatwierdza zmiany w bazie danych, jest to ważne, ponieważ bez tego zmiany nie zostaną zapisane w bazie danych, a to jest kluczowe do utrzymania spójności danych i zapewnienia, że operacje takie jak tworzenie tabel, dodawanie danych itp. zostaną trwale zapisane w bazie danych
       print("SQL executed")    
   except Error as e:           #obsługa błędów SQL, jeśli wystąpi błąd podczas wykonywania komendy SQL (np. błędna składnia, naruszenie klucza itp.), to zostanie on przechwycony i wyświetlony, co pozwala na diagnozowanie problemów z zapytaniami SQL i zapewnia lepszą obsługę błędów w aplikacji korzystającej z bazy danych  
       print(e)

create_projects_sql = """                        --zaczyna string SQL 
   -- projects table                            komentarz SQL (nie Python!)
   CREATE TABLE IF NOT EXISTS projects (        --tworzy tabelę jeśli nie istnieje
      id integer PRIMARY KEY AUTOINCREMENT,
      name text NOT NULL,                       --name projektu (obowiązkowa)   
      start_date text,
      end_date text
   );
   """
create_tasks_sql = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    opis TEXT,
    status TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
);
"""

def insert_project(conn, project):
   """
   Create a new project into the projects table
   :param conn:
   :param project:
   :return: project id
   """
   sql = ''' INSERT INTO projects(name, start_date, end_date)
             VALUES(?,?,?) '''
   cur = conn.cursor()
   cur.execute(sql, project)  # wykonuje komendę SQL z parametrami przekazanymi w formie krotki (project), co pozwala na bezpieczne wstawianie danych do bazy danych i unikanie problemów związanych z wstrzykiwaniem SQL (SQL injection)
   conn.commit()  # zatwierdza zmiany w bazie danych, jest to ważne, ponieważ bez tego zmiany nie zostaną zapisane w bazie danych, a to jest kluczowe do utrzymania spójności danych i zapewnienia, że operacje takie jak tworzenie tabel, dodawanie danych itp. zostaną trwale zapisane w bazie danych
   return cur.lastrowid  # zwraca ID właśnie dodanego projektu, co pozwala na dalsze operacje związane z tym projektem (np. dodawanie zadań do tego projektu itp.)

def insert_task(conn, task):
    """
    Create a new task into the tasks table
    :param conn:
    :param task:
    :return: task id    
    """
    try:
        sql = ''' INSERT INTO tasks(project_id, name, opis, status, start_date, end_date)   --nazwa kolumn w tabeli tasks, które będą wypełniane danymi z krotki task, nie musi byc ID bo samo sie dodaje (AUTOINCREMENT)
              VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)  # wykonuje komendę SQL z parametrami przekazanymi w formie krotki (task), co pozwala na bezpieczne wstawianie danych do bazy danych i unikanie problemów związanych z wstrzykiwaniem SQL (SQL injection)
        conn.commit()  # zatwierdza zmiany w bazie danych, jest to ważne, ponieważ bez tego zmiany nie zostaną zapisane w bazie danych, a to jest kluczowe do utrzymania spójności danych i zapewnienia, że operacje takie jak tworzenie tabel, dodawanie danych itp. zostaną trwale zapisane w bazie danych
        return cur.lastrowid  # zwraca ID właśnie dodanego zadania, co pozwala na dalsze operacje związane z tym zadaniem (np. aktualizowanie statusu zadania itp.)
    except Error as e:
        print(e)
        return None  # jeśli wystąpi błąd podczas próby dodania zadania do bazy danych, to zostanie on przechwycony i wyświetlony, a funkcja zwróci None, co pozwala na obsługę sytuacji, gdy dodanie zadania nie powiodło się (np. z powodu naruszenia klucza obcego, błędnej składni itp.)




if __name__ == "__main__":


   db_file = "database.db"                      #nazwa pliku bazy danych, jeśli plik nie istnieje, to zostanie utworzony, a jeśli istnieje, to zostanie otwarty

   conn = create_connection(db_file)            #tworzy połączenie z bazą danych, jeśli połączenie nie może zostać nawiązane (np. z powodu błędnej ścieżki do pliku, braku uprawnień itp.), to funkcja zwróci None, co pozwala na obsługę sytuacji, gdy połączenie nie może zostać nawiązane
   if conn is not None:                         #sprawdza, czy połączenie zostało nawiązane, jeśli tak, to wykonuje dalsze operacje na bazie danych, a jeśli nie, to wyświetla komunikat o błędzie i kończy działanie programu    
       execute_sql(conn, create_projects_sql)   #tworzy tabelę projects, jeśli połączenie zostało nawiązane
       execute_sql(conn, create_tasks_sql)      #tworzy tabelę tasks, jeśli połączenie zostało nawiązane
       print("Tabele utworzone")
       
       project = ("Aplikacja CRM", "2026-04-01", "2026-06-01")  # dane projektu do wstawienia do tabeli projects
       project_id = insert_project(conn, project)  # wstawia projekt do tabeli
       print(f"Projekt dodany z ID: {project_id}")

       task = (project_id,   #klucz obcy, który łączy zadanie z projektem, dzięki temu wiemy, do którego projektu należy to zadanie
               "Zadanie 1", 
               "Zrobic backed",
                 "W toku", 
                 "2026-04-01", 
                 "2026-06-01")
       task_id = insert_task(conn, task)  # wstawia zadanie do tabeli
       print(f"Zadanie dodane z ID: {task_id}")

       conn.close()                             #zamyka połączenie z bazą (nie usuwa pliku!)


"""
róznice pomiędzy db2.py a db3.py:

NAJWAŻNIEJSZE RÓŻNICE (TEN KOD vs POPRZEDNI)
🔹 1. Tu NIE używasz executescript

✔ poprzednio:

executescript(sql)

✔ teraz:

execute_sql(conn, sql)

👉 czyli:

1 funkcja = 1 SQL
🔹 2. Modularność

👉 masz:

create_connection
execute_sql

✔ lepsza struktura (bardziej „profesjonalna”)

🔹 3. Każde SQL osobno

👉 zamiast jednego dużego bloku

🧠 PODSUMOWANIE

👉 kod robi:

pokazuje ścieżkę bazy
łączy się z bazą
tworzy tabele (projects + tasks)
zamyka połączenie



"""