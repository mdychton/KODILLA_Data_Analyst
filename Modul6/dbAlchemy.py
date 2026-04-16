from sqlalchemy import create_engine, inspect, text
# create_engine → tworzy połączenie z bazą
# inspect → pozwala sprawdzić strukturę bazy (tabele)
# text → pozwala pisać surowe SQL

# tworzymy engine = połączenie do pliku SQLite
engine = create_engine('sqlite:///database.db', echo=True)
# echo=True → pokazuje zapytania SQL w konsoli (debug)

# sprawdzamy jakie tabele są w bazie
inspector = inspect(engine)
print(inspector.get_table_names())
# → zwraca listę tabel np. ['students', 'tasks']

# wykonanie testowego SELECT
with engine.connect() as conn:
    # otwieramy połączenie z bazą (automatycznie się zamknie po wyjściu z with)
    
    result = conn.execute(text("SELECT * FROM tasks"))
    # wykonujemy SQL

    for row in result:
        # przechodzimy przez każdy wiersz wyniku
        print(row)
        # wypisujemy dane z tabeli



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