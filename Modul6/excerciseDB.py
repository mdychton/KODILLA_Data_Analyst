import sqlite3
import csv

# Połączenie z bazą danych ,Jeśli plik nie istnieje, zostanie utworzony

conn = sqlite3.connect("weather.db")               
cursor = conn.cursor()  # tworzymy obiekt kursora, który pozwala nam wykonywać zapytania SQL na bazie danych
cursor.execute("PRAGMA foreign_keys = ON")       #To jest ważne, aby włączyć obsługę kluczy obcych w SQLite, ponieważ domyślnie jest ona wyłączona. Dzięki temu możemy zapewnić integralność danych między tabelami Projekt i Zadanie




#Tabela stacji
cursor.execute("""              
CREATE TABLE IF NOT EXISTS stations (
    station TEXT PRIMARY KEY,       -- identyfikator stacji
    latitude REAL,       -- szerokość geograficzna (float)
    longitude REAL,      -- długość geograficzna (float)
    elevation REAL,      -- wysokość nad poziomem morza
    name TEXT,           -- nazwa stacji
    country TEXT,        -- kraj
    state TEXT           -- stan / region
)
""")

# Tabela pomiarów
cursor.execute("""
CREATE TABLE IF NOT EXISTS measurements (
    station TEXT NOT NULL,
    date TEXT NOT NULL,
    precip REAL,
    tobs REAL,
    PRIMARY KEY (station, date),
    FOREIGN KEY (station) REFERENCES stations(station) ON DELETE CASCADE
)
""")
#--FOREING KEY oznacza, pilnuje zeby nie dodac smieciowyych danych do tebali measurements. station w measurements musi istnieć w stations, a ON DELETE CASCADE oznacza, że jeśli usuniemy stację z tabeli stations, to wszystkie pomiary związane z tą stacją w tabeli measurements również zostaną usunięte

# 3. Wczytanie danych: stations

with open("clean_stations.csv", newline='', encoding='utf-8') as f:  
    # otwarcie pliku CSV w trybie odczytu
    # newline='' zapobiega problemom z pustymi liniami
    # encoding='utf-8' obsługuje znaki specjalne (np. polskie litery)

    reader = csv.reader(f)  
    # tworzy obiekt czytający CSV (wiersz po wierszu jako lista wartości)

    next(reader)  # pomijamy nagłówek
    # pierwszy wiersz (header) jest pomijany, bo to nazwy kolumn

    for row in reader:
        try:
            cursor.execute("""
            INSERT INTO stations (
                station, latitude, longitude, elevation, name, country, state
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, row)

        except Exception as e:
            print("ERROR ROW:", row)
            print("ERROR:", e)
            # miejsca (?) to parametry zapytania (bezpieczne przed SQL injection)
            # przekazanie całego wiersza CSV jako wartości do INSERT

# 4. Wczytanie danych: measurements
#================================

with open("clean_measure.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # pomijamy nagłówek

    for row in reader:
        cursor.execute("""
        INSERT INTO measurements (
            station, date, precip, tobs
        )
        VALUES (?, ?, ?, ?)
        """, row)


# 5. Zapis zmian do bazy
# ================================
conn.commit()



# Pobranie pierwszych 5 rekordów ze stacji
result1 = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print("Stations:", result1)

# Pobranie pierwszych 5 rekordów z pomiarów
result2 = conn.execute("SELECT * FROM measurements LIMIT 5").fetchall()
print("Measurements:", result2)


# 7. JOIN - połączenie danych z dwóch tabel
# ================================
result3 = conn.execute("""
SELECT s.name, s.country, m.date, m.tobs, m.precip
FROM stations s
JOIN measurements m
ON s.station = m.station
LIMIT 5
""").fetchall()

print("JOIN result:", result3)

conn.close() # Zamknięcie połączenia