from sqlalchemy import Table, Column, Integer, String, MetaData
# Table → definicja tabeli
# Column → definicja kolumny
# Integer, String → typy danych
# MetaData → „kontener” na wszystkie tabele

from dbAlchemy import engine
# importujemy engine z pliku dbAlchemy (jedno źródło połączenia)

# tworzymy obiekt przechowujący wszystkie tabele
meta = MetaData()

# definicja tabeli students
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),  # ID (klucz główny)
    Column('name', String),                   # imię
    Column('lastname', String),               # nazwisko
)

# tworzymy tabelę w bazie (jeśli nie istnieje)
meta.create_all(engine)

# UWAGA:
# w SQLAlchemy 2.x nie używamy engine.table_names()
# zamiast tego używamy inspect(engine).get_table_names() do sprawdzenia, czy tabela została utworzona poprawnie.