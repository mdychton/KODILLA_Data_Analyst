"""
🔹 Co to jest apply?

👉 apply pozwala wykonać funkcję:

na każdym elemencie kolumny
lub
na każdym wierszu DataFrame

Czyli:

„weź moją funkcję i zastosuj ją do każdego rekordu”

🔹 1. Apply na jednej kolumnie (najczęstsze)
✔️ Przykład – prowizja
def commission_fee(x):
    if x <= 300:
        return 0
    elif x <= 900:
        return x * 0.03
    else:
        return x * 0.06

# zastosowanie funkcji do KAŻDEJ wartości w kolumnie
df['commission_fee'] = df['Sprzedaż'].apply(commission_fee)

👉 Co się dzieje:

x = jedna wartość z kolumny Sprzedaż
funkcja liczy prowizję
wynik trafia do nowej kolumny
✔️ To samo z lambda
df['commission_fee'] = df['Sprzedaż'].apply(lambda x: commission_fee(x))

👉 Lambda = skrócona funkcja
👉 ale tutaj jest zbędna (lepiej poprzednia wersja)

🔹 2. Apply z wbudowaną funkcją
✔️ Liczba znaków w tekście
df['Produkt_len'] = df['Produkt'].apply(len)

👉 len działa na każdym elemencie osobno
👉 np. "Laptop" → 6

🔹 3. Apply + lambda (szybkie obliczenia)
✔️ Liczba opakowań
import math

df['#_opakowań'] = df['Sztuki'].apply(lambda x: math.ceil(x / 5))

👉 logika:

dzielimy przez 5
zaokrąglamy w górę (ceil)
zawsze pełne opakowanie
🔹 4. Apply na całym wierszu (ważne!)

Gdy potrzebujesz więcej niż jednej kolumny

✔️ Przykład – bonus
def bonus(row):
    # liczymy marżę
    margin = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']
    
    if margin > 0.55:
        return 200
    else:
        return 0

# UWAGA: axis=1 = działamy na wierszach
df['Bonus'] = df.apply(bonus, axis=1)

👉 Co się dzieje:

row = cały wiersz (jak słownik)
row['Sprzedaż'] → wartość z kolumny
funkcja zwraca wynik dla każdego wiersza
🔴 Bardzo ważne: axis
axis=0 → kolumny (rzadko używane w apply)
axis=1 → wiersze ✅

👉 przy pracy na wielu kolumnach MUSI być axis=1

🔹 Najczęstsze błędy
❌ Brak axis
df.apply(bonus)   # KeyError
❌ Literówki w nazwach kolumn
row['Sprzedaz']  # zamiast 'Sprzedaż'
❌ Niezdefiniowana funkcja
apply(commission_fee)  # a funkcja nie istnieje
🔹 Kiedy używać apply?

✅ gdy:

masz własną logikę (if/else)
potrzebujesz wielu kolumn
nie da się łatwo zrobić tego w jednej linijce

❌ unikaj gdy:

można użyć +, *, np.where (szybsze!)
🔹 TL;DR

👉 apply = wykonaj funkcję dla każdego elementu / wiersza

kolumna:
df['col'].apply(func)
wiersz:
df.apply(func, axis=1)

============================ZADANIE============================

🟢 Zadanie 1

👉 Dodaj kolumnę Poziom_sprzedaży:

< 300 → "niska"
300–900 → "średnia"

900 → "wysoka"

def poziom(x):
    # sprawdzamy poziom sprzedaży
    if x < 300:
        return 'niska'
    elif x <= 900:
        return 'średnia'
    else:
        return 'wysoka'

# apply wykonuje funkcję dla każdej wartości w kolumnie
df['Poziom_sprzedaży'] = df['Sprzedaż'].apply(poziom)
🟢 Zadanie 2

👉 Dodaj kolumnę Produkt_upper (duże litery)

# apply + wbudowana metoda string
df['Produkt_upper'] = df['Produkt'].apply(lambda x: x.upper())

# można też prościej (bez apply):
# df['Produkt_upper'] = df['Produkt'].str.upper()
🟡 Zadanie 3

👉 Dodaj kolumnę Rabat:

1000 → 10%

inaczej → 5%
def rabat(x):
    # warunek na wysokość sprzedaży
    if x > 1000:
        return x * 0.10
    else:
        return x * 0.05

df['Rabat'] = df['Sprzedaż'].apply(rabat)
🟡 Zadanie 4

👉 Dodaj kolumnę Zysk:

Sprzedaż - Koszty
jeśli < 0 → "Strata"
def zysk(row):
    # liczymy zysk z dwóch kolumn
    wynik = row['Sprzedaż'] - row['Koszty']
    
    # jeśli ujemny → tekst
    if wynik < 0:
        return 'Strata'
    else:
        return wynik

# axis=1 → funkcja działa na całym wierszu
df['Zysk'] = df.apply(zysk, axis=1)
🟡 Zadanie 5

👉 Dodaj kolumnę Kategoria_marży:

< 30% → "niska"
30–60% → "średnia"

60% → "wysoka"

def kategoria_marzy(row):
    # obliczamy marżę
    marza = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']
    
    # klasyfikacja
    if marza < 0.3:
        return 'niska'
    elif marza <= 0.6:
        return 'średnia'
    else:
        return 'wysoka'

df['Kategoria_marży'] = df.apply(kategoria_marzy, axis=1)
🔴 Zadanie 6

👉 Dodaj kolumnę Premia:

sprzedaż > 1000 i marża > 50% → 500
jeden warunek → 200
inaczej → 0
def premia(row):
    # liczymy marżę
    marza = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']
    
    # dwa warunki
    if row['Sprzedaż'] > 1000 and marza > 0.5:
        return 500
    
    # jeden z warunków
    elif row['Sprzedaż'] > 1000 or marza > 0.5:
        return 200
    
    # brak warunków
    else:
        return 0

df['Premia'] = df.apply(premia, axis=1)
🔴 Zadanie 7

👉 Pakowanie:

opakowania → liczba paczek (po 5 sztuk)
nadwyżka → ile zostaje
import math

def pakowanie(row):
    sztuki = row['Sztuki']
    
    # liczba pełnych opakowań (zaokrąglenie w górę)
    opakowania = math.ceil(sztuki / 5)
    
    # reszta z dzielenia
    nadwyzka = sztuki % 5
    
    return opakowania, nadwyzka

# apply zwraca krotkę → rozbijamy na dwie kolumny
df[['opakowania', 'nadwyżka']] = df.apply(
    lambda row: pakowanie(row),
    axis=1,
    result_type='expand'  # rozdziela tuple na kolumny
)




🔹 Lambda vs normalna funkcja — o co chodzi?

Masz swoje rozwiązanie:

df['Poziom_sprzedazy'] = df['Sprzedaż'].apply(lambda x: poziom_sprzedazy(x))

👉 To działa, ALE:

👉 lambda tutaj nic nie wnosi

✅ Lepsza wersja
df['Poziom_sprzedazy'] = df['Sprzedaż'].apply(poziom_sprzedazy)

👉 krócej
👉 czytelniej
👉 standard w Pandas

🔥 Kiedy NIE używać lambdy?

👉 gdy masz już funkcję:

def moja_funkcja(x):
    return x * 2

# ❌ niepotrzebnie
apply(lambda x: moja_funkcja(x))

# ✅ poprawnie
apply(moja_funkcja)
🔥 Kiedy używać lambdy?

👉 gdy:

funkcja jest krótka
używasz jej tylko raz
nie chcesz pisać def
✔️ Przykład dobry dla lambda
df['VAT'] = df['Sprzedaż'].apply(lambda x: x * 0.23)
✔️ Przykład lambda + logika
df['Poziom'] = df['Sprzedaż'].apply(
    lambda x: 'wysoka' if x > 1000 else 'niska'
)
🔴 Zasada (mega ważna)

👉 jeśli masz lambda x: funkcja(x)
➡️ usuń lambdę

👉 jeśli masz logikę w środku
➡️ lambda OK

🔥 Zadania rekrutacyjne (często padają)
🔴 Zadanie 1 (SQL-like thinking)

👉 Dodaj kolumnę Top_seller:

jeśli sprzedaż > średnia sprzedaż → 1
inaczej → 0
✅ apply (Twoje podejście)
avg = df['Sprzedaż'].mean()

df['Top_seller'] = df['Sprzedaż'].apply(
    lambda x: 1 if x > avg else 0
)
🚀 wersja PRO (bez apply)
df['Top_seller'] = (df['Sprzedaż'] > df['Sprzedaż'].mean()).astype(int)

👉 szybciej + elegancko

🔴 Zadanie 2 (więcej kolumn)

👉 Dodaj Status:

jeśli zysk > 0 → "OK"
jeśli = 0 → "BREAK EVEN"
jeśli < 0 → "LOSS"
✅ apply
def status(row):
    zysk = row['Sprzedaż'] - row['Koszty']
    
    if zysk > 0:
        return 'OK'
    elif zysk == 0:
        return 'BREAK EVEN'
    else:
        return 'LOSS'

df['Status'] = df.apply(status, axis=1)
🚀 PRO (bez apply)
zysk = df['Sprzedaż'] - df['Koszty']

df['Status'] = np.where(
    zysk > 0, 'OK',
    np.where(zysk == 0, 'BREAK EVEN', 'LOSS')
)
🔴 Zadanie 3 (bucketowanie – bardzo ważne)

👉 Podziel sprzedaż na przedziały:

0–300 → low
300–900 → mid
900+ → high
🚀 PRO rozwiązanie
df['Poziom'] = pd.cut(
    df['Sprzedaż'],
    bins=[0, 300, 900, float('inf')],
    labels=['low', 'mid', 'high']
)

👉 to jest dużo lepsze niż apply

🔥 Zadania PRO (bez apply – ważne w pracy)
🟣 Zadanie 4

👉 Dodaj prowizję (jak wcześniej)

🚀 rozwiązanie
df['commission'] = np.select(
    [
        df['Sprzedaż'] <= 300,
        df['Sprzedaż'] <= 900,
        df['Sprzedaż'] > 900
    ],
    [
        0,
        df['Sprzedaż'] * 0.03,
        df['Sprzedaż'] * 0.06
    ]
)
🟣 Zadanie 5

👉 Liczba opakowań (po 5 sztuk)

df['opakowania'] = np.ceil(df['Sztuki'] / 5)

👉 zero apply 😎

🔥 TL;DR (najważniejsze)

👉 używaj:

apply(func) → gdy masz własną funkcję
lambda → tylko do krótkich rzeczy
NIE rób:
apply(lambda x: func(x))  ❌

👉 najlepiej:

spróbuj bez apply
jeśli się nie da → apply
jeśli prosta logika → lambda
jeśli większa → def



🟢 Zadanie 1 – Segment sprzedaży
def segment(x):
    # klasyfikacja sprzedaży na 3 poziomy
    if x < 300:
        return 'low'
    elif x <= 900:
        return 'mid'
    else:
        return 'high'

# apply uruchamia funkcję dla każdej wartości
df['Segment'] = df['Sprzedaż'].apply(segment)
🟢 Zadanie 2 – czyszczenie tekstu
# .str działa na całej kolumnie tekstowej
df['Produkt_clean'] = df['Produkt'].str.strip().str.lower()

# strip → usuwa spacje z początku i końca
# lower → zamienia na małe litery
🟡 Zadanie 3 – marża %
# liczymy marżę i zaokrąglamy
df['Marża_%'] = ((df['Sprzedaż'] - df['Koszty']) / df['Sprzedaż']).round(2)
🟡 Zadanie 4 – ocena marży (apply + wiersze)
def ocena(row):
    # liczymy marżę dla wiersza
    marza = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']
    
    # klasyfikacja
    if marza > 0.5:
        return 'TOP'
    elif marza >= 0.2:
        return 'OK'
    else:
        return 'LOW'

# axis=1 → działamy na wierszach
df['Ocena'] = df.apply(ocena, axis=1)
🔴 Zadanie 5 – premia
def premia(row):
    marza = (row['Sprzedaż'] - row['Koszty']) / row['Sprzedaż']
    
    # najlepszy przypadek
    if row['Sprzedaż'] > 1000 and marza > 0.4:
        return 500
    
    # tylko sprzedaż spełniona
    elif row['Sprzedaż'] > 1000:
        return 200
    
    # brak warunków
    else:
        return 0

df['Premia'] = df.apply(premia, axis=1)
🔥 Zadanie 6 – bez apply (PRO)
# średnia sprzedaż
avg = df['Sprzedaż'].mean()

# True/False → zamieniamy na 1/0
df['Above_avg'] = (df['Sprzedaż'] > avg).astype(int)
🔥 Zadanie 7 – pakowanie
import math

def pakowanie(row):
    sztuki = row['Sztuki']
    
    # liczba opakowań (zawsze w górę)
    opakowania = math.ceil(sztuki / 5)
    
    # sprawdzamy czy dzieli się idealnie
    if sztuki % 5 == 0:
        czy_pelne = 'tak'
    else:
        czy_pelne = 'nie'
    
    return opakowania, czy_pelne

# rozbijamy wynik na dwie kolumny
df[['opakowania', 'czy_pelne']] = df.apply(
    pakowanie,
    axis=1,
    result_type='expand'
)
🔥 Podsumowanie (co tu było testowane)

✔ .str vs apply
✔ axis=1 (wiersze)
✔ logika biznesowa
✔ unikanie apply gdy się da
✔ vectorization (.mean(), .astype())
✔ zwracanie wielu wartości z apply




"""