"""
🔹 DataFrame — wyjaśnienie + komentarze
📌 Czym jest DataFrame
podstawowa struktura w pandas
2-wymiarowa tabela (wiersze + kolumny)
coś jak Excel / SQL table

👉 mentalnie:

DataFrame = zbiór Series (kolumn)
🔹 Tworzenie DataFrame (najczęściej)
import pandas as pd

# słownik: klucz = kolumna, wartości = dane
df = pd.DataFrame({'e1': exam1, 'e2': exam2}, index=labels)
💬 komentarz
# tworzymy DataFrame:
# 'e1', 'e2' -> nazwy kolumn
# exam1, exam2 -> dane
# labels -> indeks (wiersze, np. studenci)
🔹 Jak działa DataFrame
df['e1']

👉 zwraca:

Series
type(df['e1'])  # pandas.Series

✔ ważne:

DataFrame = kolekcja Series z tym samym indeksem
🔹 Tworzenie z NumPy
import numpy as np

data = np.array([exam1, exam2])

df = pd.DataFrame(
    data.transpose(),
    index=labels,
    columns=['e1', 'e2']
)
💬 komentarz
# transpose() zmienia wiersze na kolumny
# ndarray -> DataFrame
🔹 Konwersja do NumPy
df.to_numpy()

👉 zamienia DataFrame → ndarray

🔴 WAŻNE (często pomijane)
NumPy → jeden typ danych
DataFrame → różne typy w kolumnach

👉 efekt:

df.to_numpy()

może zamienić wszystko na object (wolniejsze!)

🔹 Shape (jak w NumPy)
df.shape

👉 wynik:

(wiersze, kolumny)
🔹 Wybór kolumn
df['e1']        # Series
df[['e1','e2']] # DataFrame
🔴 NIEZALECANE
df.e1
❌ dlaczego:
psuje się przy:
spacje w nazwach
polskie znaki
konflikt z metodami

✔ BEST PRACTICE:

df['e1']
🔹 Dodawanie kolumn
df['e3'] = [67,59,79,84]
💬 komentarz
# długość musi pasować do liczby wierszy!
🔹 Tworzenie kolumn z innych
df['semester1'] = df['e1'] + df['e2'] + df['e3']

✔ albo lepiej:

df['semester1'] = df[['e1','e2','e3']].sum(axis=1)
🔹 Wybór wierszy — .loc
df.loc['Student C']

👉 wybór po nazwie (indeksie)

🔹 Konkretna komórka
df.loc['Student C', 'e2']
🔹 Wiele wierszy/kolumn
df.loc[['Student C','Student D'], ['e2']]
🔹 .iloc — po pozycji
df.iloc[1]

👉 drugi wiersz (index 1)

🔹 slicing
df.iloc[1:, 1]
💬 komentarz
# 1: -> od drugiego wiersza do końca
# 1  -> druga kolumna
🔹 STRESZCZENIE (najważniejsze)
✔ 1. DataFrame = tabela (wiersze + kolumny)
✔ 2. Każda kolumna to Series
✔ 3. Tworzenie:
pd.DataFrame(dict, index=...)
✔ 4. Dostęp:
kolumny → df['col']
wiersze → df.loc[]
pozycje → df.iloc[]
✔ 5. Operacje działają kolumnowo
✔ 6. Można mieć różne typy danych
🔹 BEST PRACTICES (ważniejsze niż teoria)
✔ 1. Zawsze używaj:
df['col']

❌ nie df.col

✔ 2. Do wielu kolumn:
df[['a','b']]
✔ 3. Do obliczeń:
df.sum(axis=1)

✔ zamiast ręcznego dodawania

✔ 4. Używaj .loc i .iloc
metoda	kiedy
.loc	nazwy
.iloc	pozycje
✔ 5. Uważaj na długości danych
df['new'] = [...]

👉 musi pasować do liczby wierszy

✔ 6. Kontroluj typy
df.dtypes
✔ 7. Myśl „kolumnami”, nie „wierszami”

Pandas jest zoptymalizowany pod kolumny

✔ 8. Unikaj .to_numpy() jeśli nie trzeba

👉 tracisz indeks + typy

🔹 Najczęstsze błędy (z Twoich przykładów)

❌

df['e1'] + ['e2']

✔

df['e1'] + df['e2']
🔹 Mentalny model (najważniejsze)
DataFrame = Excel w Pythonie + NumPy w środku

"""