from sqlalchemy import create_engine  # importujemy funkcję do tworzenia połączenia z bazą danych

engine = create_engine('sqlite:///database.db')  # tworzymy silnik (połączenie) do bazy SQLite (plik database.db)

print(engine.driver)  # wypisuje, jakiego drivera używa (np. 'pysqlite')

print(engine.table_names())  # pobiera i wypisuje listę tabel w bazie danych

print(engine.execute("SELECT * FROM tasks"))  # wykonuje zapytanie SQL i wypisuje obiekt wyniku (nie same dane!)

results = engine.execute("SELECT * FROM tasks")  # wykonujemy zapytanie i zapisujemy wynik do zmiennej

for r in results:  # iterujemy po każdym wierszu wyniku
   print(r)  # wypisujemy każdy rekord (wiersz z tabeli tasks)



"""
TEN KOD WYZEJ NIE DZIALA JUZ Z NAJNOWSZA WERSJA SQLAlchemy, PONIEWAZ WERSJA 2.0 WPROWADZIŁA ZMIANY W SYNTAXIE I SPOSOBIE UŻYWANIA SILNIKA. PONIŻEJ ZNAJDUJE SIĘ POPRAWIONY KOD, KTÓRY JEST KOMPATYBILNY Z SQLALCHEMY 2.0:

from sqlalchemy import create_engine, text, inspect  # importujemy potrzebne narzędzia

engine = create_engine('sqlite:///database.db')  # tworzymy połączenie z bazą SQLite

# sprawdzenie drivera
print(engine.dialect.name)  # zamiast engine.driver w nowszych wersjach

# pobranie listy tabel
inspector = inspect(engine)  # tworzymy obiekt do inspekcji bazy
print(inspector.get_table_names())  # wypisuje listę tabel

# wykonanie zapytania SQL
with engine.connect() as connection:  # otwieramy połączenie (zalecany sposób)
    result = connection.execute(text("SELECT * FROM tasks"))  # wykonujemy zapytanie (text wymagany w 2.x)

    for row in result:  # iterujemy po wynikach
        print(row)  # wypisujemy każdy rekord


"""