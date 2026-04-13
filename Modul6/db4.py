import sqlite3
from sqlite3 import Error
import os

# =========================
# ŚCIEŻKA DO BAZY DANYCH
# =========================
print(os.path.abspath("database.db"))  # pokazuje gdzie fizycznie powstaje plik bazy


# =========================
# DEFINICJE TABEL (SQL)
# =========================
# To są "instrukcje budowy bazy" – NIE wykonują się same

create_projects_sql = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- unikalne ID generowane automatycznie
    name TEXT NOT NULL,                    -- nazwa projektu (wymagana)
    start_date TEXT,
    end_date TEXT
);
"""

create_tasks_sql = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- unikalne ID zadania
    project_id INTEGER NOT NULL,           -- powiązanie z projektem (FOREIGN KEY)
    name TEXT NOT NULL,                    -- nazwa zadania
    opis TEXT,
    status TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,

    FOREIGN KEY (project_id) REFERENCES projects (id) ON DELETE CASCADE
    -- jeśli usuniesz projekt → wszystkie taski też się usuwają
);
"""


# =========================
# POŁĄCZENIE Z BAZĄ
# =========================
def create_connection(db_file):
    """Tworzy połączenie z bazą SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return conn
    except Error as e:
        print("Connection error:", e)
    return conn


# =========================
# WYKONYWANIE SQL (CREATE TABLE, DROP, itp.)
# =========================
def execute_sql(conn, sql):
    """Wykonuje pojedyncze zapytanie SQL"""
    try:
        cur = conn.cursor()
        cur.execute(sql)     # wykonanie SQL
        conn.commit()        # zapis zmian w bazie
    except Error as e:
        print("SQL error:", e)


# =========================
# DODAWANIE PROJEKTU
# =========================
def insert_project(conn, project):
    sql = """
    INSERT INTO projects(name, start_date, end_date)
    VALUES (?, ?, ?)
    """
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid   # zwraca ID nowo dodanego projektu


# =========================
# DODAWANIE ZADANIA
# =========================
def insert_task(conn, task):
    sql = """
    INSERT INTO tasks(project_id, name, opis, status, start_date, end_date)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid   # zwraca ID nowego zadania

# =========================
# SELECT
# =========================

def get_projects(conn, project_id):
    """Pobiera jeden projekt z bazy danych"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects WHERE id=?", (project_id,))  # pobiera projekt o konkretnym ID, wynik jest w formie listy krotek (tu tylko jedna krotka, bo ID jest unikalne)
    row = cur.fetchone()  # zwraca pojedynczy rekord (krotkę), musisz to miec zeby wystwietlic projekt, bo cur.execute zwraca obiekt kursora, a nie dane, więc musisz wywołać fetchone() lub fetchall() żeby dostać dane z bazy danych  

    print("\n ===SINGLE PROJECT===")
    print(row)  # wyświetla pobrany projekt (krotka z danymi projektu)

def get_all_projects(conn):
    """Pobiera wszystkie projekty z bazy"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")  # pobiera wszystkie projekty, wynik jest w formie listy krotek (każda krotka to jeden projekt)
    rows = cur.fetchall()  # zwraca listę wszystkich rekordów (lista krotek), musisz to miec zeby wystwietlic projekty, bo cur.execute zwraca obiekt kursora, a nie dane, więc musisz wywołać fetchone() lub fetchall() żeby dostać dane z bazy danych  """
    print("\n ===ALL PROJECTS===")  #najpierw wyświetla nagłówek, a potem listę projektów
    for row in rows:
        print(row)  # wyświetla każdy projekt (krotkę z danymi projektu)

def get_all_tasks(conn):
    """Pobiera wszystkie zadania z bazy danych"""           #te komenarze sa wazne bo pozniej jak sie odpali help(get_all_tasks) to bedzie wiadomo co ta funkcja robi i jakie dane zwraca, a to jest kluczowe do zrozumienia jak używać tej funkcji i co można z nią zrobić, a także jakie dane musisz jej przekazać, żeby działała poprawnie   
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")  # pobiera wszystkie zadania, wynik jest w formie listy krotek (każda krotka to jedno zadanie)
    rows = cur.fetchall()  # zwraca listę wszystkich rekordów (lista krotek), musisz to miec zeby wystwietlic zadania, bo cur.execute zwraca obiekt kursora, a nie dane, więc musisz wywołać fetchone() lub fetchall() żeby dostać dane z bazy danych   

    print("\n ===ALL TASKS===")  #najpierw wyświetla nagłówek, a potem listę zadań
    for row in rows:
        print(row)  # wyświetla każde zadanie (krotkę z danymi zadania)
    

def get_tasks_by_project(conn, project_id):
    """Pobiera zadania dla konkretnego projektu"""          #to daje ostatni wynik, czyli zadania dla konkretnego projektu, ale bez nazwy projektu, bo tu nie ma JOIN, więc mamy tylko ID projektu, a nie jego nazwę
    cur = conn.cursor()
    cur.execute("""
         SELECT tasks.id, tasks.name, tasks.status
         FROM tasks
         WHERE tasks.project_id = ?
    """, (project_id,))

    rows = cur.fetchall()

    print(f"\n ===TASKS FOR PROJECT {project_id}===")
    for row in rows:
        print(row)  # wyświetla każde zadanie (krotkę z danymi zadania)

def get_tasks_with_project_name(conn):
    """Pobiera zadania wraz z nazwą projektu (JOIN)"""
    cur = conn.cursor()
    cur.execute("""
         SELECT tasks.id, tasks.name, tasks.status, projects.name
         FROM tasks
         JOIN projects ON tasks.project_id = projects.id
         ORDER BY projects.id
    """)

    rows = cur.fetchall()

    print("\n ===TASKS WITH PROJECT NAMES===")
    for row in rows:
        print(row)  # wyświetla każde zadanie (krotkę z danymi zadania)

def select_taks_by_status(conn, status):
    """Pobiera zadania o konkretnym statusie"""
    cur = conn.cursor()
    cur.execute("""
         SELECT tasks.id, tasks.name, tasks.status
         FROM tasks
         WHERE tasks.status = ?
    """, (status,))

    rows = cur.fetchall()

    print(f"\n ===TASKS WITH STATUS {status}===")
    for row in rows:
        print(row)  # wyświetla każde zadanie (krotkę z danymi zadania)


def select_all(conn,table):
    """Pobiera wszystkie rekordy z dowolnej tabeli"""
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")  # pobiera wszystkie rekordy z podanej tabeli, wynik jest w formie listy krotek (każda krotka to jeden rekord)
    rows = cur.fetchall()  # zwraca listę wszystkich rekordów (lista krotek), musisz to miec zeby wystwietlic dane, bo cur.execute zwraca obiekt kursora, a nie dane, więc musisz wywołać fetchone() lub fetchall() żeby dostać dane z bazy danych   

    print(f"\n ===ALL RECORDS FROM {table.upper()}===")  #najpierw wyświetla nagłówek, a potem listę rekordów
    for row in rows:
        print(row)  # wyświetla każdy rekord (krotkę z danymi)

def select_where(conn, table, **query):  #„query” przyjmij dowolną liczbę nazwanych argumentów i zbierz je do słownika”
    """
    Dynamiczne zapytanie SELECT z warunkiem WHERE

    Przykład:
    select_where(conn, "tasks", project_id=1, status="W toku")
    """
    cur = conn.cursor()  
    # tworzymy cursor - obiekt do wykonywania zapytań SQL

    qs = []  
    # lista warunków SQL, np. ["status=?", "project_id=?"] qs to „zbieracz warunków”, do którego będziemy dodawać warunki na podstawie przekazanego słownika query, dzięki temu możemy dynamicznie budować zapytanie SQL w zależności od tego, jakie argumenty zostały przekazane do funkcji (np. jeśli przekazano status i project_id, to dodamy oba warunki do zapytania SQL)

    values = ()  
    # tuple z wartościami do podstawienia w SQL, np. ("W toku", 1)

    for k, v in query.items():
        # przechodzimy po słowniku query
        # k = nazwa kolumny (np. "status")
        # v = wartość (np. "W toku")

        qs.append(f"{k}=?")  
        # dodajemy warunek SQL np. "status=?"

        values += (v,)  
        # dodajemy wartość do tuple
        # przecinek ważny -> tworzy tuple jednolity

    q = " AND ".join(qs)  
    # łączy warunki w jeden string:
    # np. "status=? AND project_id=?"

    sql = f"SELECT * FROM {table} WHERE {q}"  
    # budujemy finalne zapytanie SQL:
    # np. "SELECT * FROM tasks WHERE status=? AND project_id=?"

    cur.execute(sql, values)  
    # wykonujemy SQL i podstawiamy wartości bezpiecznie (bez SQL injection)

    rows = cur.fetchall()  
    # pobieramy wszystkie wyniki jako listę krotek

    return rows  
    # zwracamy wynik do miejsca gdzie funkcja została wywołana


# =========================
# UPDATE
# =========================

def update(conn,table,id,**kwargs):
    """
     update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
    """
    parameters = [f"{k} = ?" for k in kwargs]  # tworzymy listę parametrów do aktualizacji, np. ["status = ?", "start_date = ?", "end_date = ?"]
    parameters = ", ".join(parameters)  # łączymy parametry w string, np. "status = ?, start_date = ?, end_date = ?"
    values = tuple(kwargs.values())  # tworzymy tuple z wartościami do aktualizacji, np. ("Gotowe", "2026-04-01", "2026-06-01")
    values += (id,)  # dodajemy ID na koniec tuple, bo będzie potrzebne w WHERE
    sql = f"UPDATE {table} SET {parameters} WHERE id = ?"  # budujemy zapytanie SQL, np. "UPDATE tasks SET status = ?, start_date = ?, end_date = ? WHERE id = ?"
    try:
        cur = conn.cursor()  # tworzymy cursor do wykonania zapytania
        cur.execute(sql, values)  # wykonujemy zapytanie SQL z wartościami
        conn.commit()  # zatwierdzamy zmiany w bazie danych
        print(f"Row with id {id} updated successfully")  # informacja o sukcesie aktualizacji
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")  # informacja o błędzie, np. jeśli tabela nie istnieje
    


def delete(conn, table, **kwargs):
    """
    Usuwa rekordy z tabeli na podstawie warunków (WHERE)

    Przykład:
    delete(conn, "tasks", id=1)
    delete(conn, "tasks", status="Done", project_id=2)
    """

    qs = []  
    # lista warunków SQL, np. ["id=?", "status=?"]

    values = tuple()  
    # tuple z wartościami do podstawienia, np. (1, "Done")

    for k, v in kwargs.items():
        # przechodzimy po wszystkich filtrach przekazanych do funkcji

        qs.append(f"{k}=?")  
        # dodajemy warunek SQL, np. "id=?"

        values += (v,)  
        # dodajemy wartość do tuple (ważny przecinek!)

    q = " AND ".join(qs)  
    # łączymy warunki w jeden string:
    # np. "id=? AND status=?"

    sql = f"DELETE FROM {table} WHERE {q}"  
    # budujemy finalne zapytanie SQL:
    # np. DELETE FROM tasks WHERE id=? AND status=?

    cur = conn.cursor()  
    # tworzymy cursor (narzędzie do wykonywania SQL)

    cur.execute(sql, values)  
    # wykonujemy DELETE z bezpiecznym podstawieniem wartości (bez SQL injection)

    conn.commit()  
    # zapisujemy zmiany w bazie danych

    print(f"Deleted {cur.rowcount} record(s) from {table}")  
    # informacja o liczbie usuniętych rekordów

def delete_all(conn, table):
    """
    Usuwa wszystkie rekordy z tabeli

    UWAGA: brak WHERE = kasuje CAŁĄ tabelę!
    """

    sql = f"DELETE FROM {table}"  
    # budujemy zapytanie SQL:
    # np. DELETE FROM tasks
    # f-string pozwala dynamicznie podać nazwę tabeli

    cur = conn.cursor()  
    # tworzymy cursor (narzędzie do komunikacji z bazą danych)

    cur.execute(sql)  
    # wykonujemy zapytanie SQL (usuwa wszystkie wiersze z tabeli)

    conn.commit()  
    # zapisujemy zmiany w bazie (bez tego dane NIE zostaną usunięte)

    print(f"Deleted all records from {table}")  
    # informacja dla użytkownika, że operacja się wykonała




# =========================
# MAIN
# =========================
if __name__ == "__main__":
    db_file = "database.db"  

    # 2. połączenie z bazą
    conn = create_connection(db_file)

    if conn is not None:

        # 3. tworzenie tabel (jeśli nie istnieją)
        execute_sql(conn, create_projects_sql)
        execute_sql(conn, create_tasks_sql)

        print("Tabele gotowe")

        # =========================
        # 4. DODANIE PROJEKTU
        # =========================
        project = ("Aplikacja MASLO", "2026-04-01", "2026-08-01")
        project_id = insert_project(conn, project)
        print("Projekt ID:", project_id)

        # =========================
        # 5. DODANIE ZADANIA
        # =========================
        task = (
            project_id,          # powiązanie z projektem
            "Zadanie 1",
            "Zrobic backend",
            "Cancelled",
            "2026-04-01",
            "2026-06-01"
        )

        task_id = insert_task(conn, task)
        print("Task ID:", task_id)
        get_projects(conn, project_id)  # pobiera i wyświetla dodany projekt
        get_all_projects(conn)  # pobiera i wyświetla wszystkie projekty
        get_all_tasks(conn)  # pobiera i wyświetla wszystkie zadania
        get_tasks_by_project(conn, project_id)  # pobiera i wyświetla zadania dla konkretnego projektu
        get_tasks_with_project_name(conn)  # pobiera i wyświetla zadania wraz z nazwą projektu (JOIN)
        #update(conn, "tasks", task_id, status="Gotowe", start_date="2028-04-01", end_date="2030-06-01")  # aktualizuje zadanie o konkretnym ID, zmieniając jego status, start_date i end_date
        update(conn, "projects", project_id, name="Aplikacja MASLO 2.0")  # aktualizuje projekt o konkretnym ID, zmieniając jego nazwę
        update(conn, "tasks",project_id, status="TESTUJE")  # aktualizuje projekt o konkretnym ID, zmieniając jego nazwę i start_date
        select_taks_by_status(conn, "TESTUJE")  # pobiera i wyświetla zadania o konkretnym statusie (np. "W toku")
        delete(conn, "tasks", id=4)  # usuwa zadanie o konkretnym ID (np. id=3)
        delete(conn, "tasks", status="Cancelled")  # usuwa zadania o konkretnym statusie (np. "Cancelled")
        select_all(conn, "projects")  # pobiera i wyświetla wszystkie rekordy z tabeli projects
        select_where(conn, "projects", id=1)  # pobiera i wyświetla projekt o ID 1
        select_where(conn, "tasks", project_id=17)  # pobiera i wyświetla zadania dla projektu o ID 2
        select_where(conn, "tasks", status="W toku") # pobiera i wyświetla zadania dla projektu o ID 1, które mają status "W toku"
        
        #help(get_tasks_by_project)  # pokazuje dokumentację funkcji get_tasks_by_project, czyli jakie parametry przyjmuje i co zwraca, to jest ważne, bo dzięki temu wiesz jak używać tej funkcji i co możesz z nią zrobić, a także jakie dane musisz jej przekazać, żeby działała poprawnie    

        # 6. zamknięcie połączenia
        conn.close()