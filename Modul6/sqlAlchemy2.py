from sqlalchemy import Table, Column, Integer, String, MetaData  # importujemy elementy do definiowania tabeli
from sqlalchemy import create_engine  # importujemy funkcję do połączenia z bazą danych

engine = create_engine('sqlite:///database.db',echo=True)  # tworzymy silnik (połączenie) do pliku SQLite database.db

meta = MetaData()  # tworzymy obiekt przechowujący metadane (opis tabel)

students = Table(  # definiujemy tabelę "students"
   'students', meta,  # nazwa tabeli + przypięcie do MetaData
   Column('id', Integer, primary_key=True),  # kolumna id (liczba, klucz główny)
   Column('name', String),  # kolumna name (tekst)
   Column('lastname', String),  # kolumna lastname (tekst)
)

meta.create_all(engine)  # tworzy tabelę w bazie, jeśli jeszcze nie istnieje

print(engine.table_names())  # wypisuje listę tabel w bazie (UWAGA: przestarzałe w SQLAlchemy 2.x)