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
       #conn.commit()     # zatwierdza zmiany w bazie danych, jest to ważne, ponieważ bez tego zmiany nie zostaną zapisane w bazie danych, a to jest kluczowe do utrzymania spójności danych i zapewnienia, że operacje takie jak tworzenie tabel, dodawanie danych itp. zostaną trwale zapisane w bazie danych
       #print("SQL executed")    
   except Error as e:           #obsługa błędów SQL, jeśli wystąpi błąd podczas wykonywania komendy SQL (np. błędna składnia, naruszenie klucza itp.), to zostanie on przechwycony i wyświetlony, co pozwala na diagnozowanie problemów z zapytaniami SQL i zapewnia lepszą obsługę błędów w aplikacji korzystającej z bazy danych  
       print(e)

if __name__ == "__main__":

   create_projects_sql = """                        #zaczyna string SQL
   -- projects table                            komentarz SQL (nie Python!)
   CREATE TABLE IF NOT EXISTS projects (        --tworzy tabelę jeśli nie istnieje
      id integer PRIMARY KEY AUTOINCREMENT,
      nazwa text NOT NULL,                       --nazwa projektu (obowiązkowa)   
      start_date text,
      end_date text
   );
   """

   create_tasks_sql = """
   -- zadanie table
   CREATE TABLE IF NOT EXISTS tasks (
      id integer PRIMARY KEY,
      project_id integer NOT NULL,              --łączy zadanie z projektem
      nazwa VARCHAR(250) NOT NULL,
      opis TEXT,
      status VARCHAR(15) NOT NULL,
      start_date text NOT NULL,
      end_date text NOT NULL,
      FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE           --RELACJA task należy do project, ON DELETE CASCADE oznacza, że jeśli usuniemy projekt, to wszystkie zadania związane z tym projektem również zostaną usunięte
   );
   """

   db_file = "database.db"                      #nazwa pliku bazy danych, jeśli plik nie istnieje, to zostanie utworzony, a jeśli istnieje, to zostanie otwarty

   conn = create_connection(db_file)            #tworzy połączenie z bazą danych, jeśli połączenie nie może zostać nawiązane (np. z powodu błędnej ścieżki do pliku, braku uprawnień itp.), to funkcja zwróci None, co pozwala na obsługę sytuacji, gdy połączenie nie może zostać nawiązane
   if conn is not None:                         #sprawdza, czy połączenie zostało nawiązane, jeśli tak, to wykonuje dalsze operacje na bazie danych, a jeśli nie, to wyświetla komunikat o błędzie i kończy działanie programu    
       execute_sql(conn, create_projects_sql)   #tworzy tabelę projects, jeśli połączenie zostało nawiązane
       execute_sql(conn, create_tasks_sql)      #tworzy tabelę tasks, jeśli połączenie zostało nawiązane
       print("Tabele utworzone")
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