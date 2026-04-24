"""
🧠 GROUPBY w Pandas — wyjaśnienie z komentarzami
📌 Co to jest groupby?

👉 groupby() =

„podziel dane na grupy + wykonaj na nich operację”

🔥 Analogia (SQL / Excel)
SQL: GROUP BY
Excel: tabela przestawna
Pandas: groupby()
📊 Dane (Kickstarter)
df = pd.DataFrame({
    'Category': ['Games','Games','Games','Film&Video','Film&Video','Film&Video'],
    'Project_Title': ['The Last Faith','Magic Puzzles','Dinosaur Fossil Hunter',
                      'Beyond Your Eyes','5150','8-Bit Wars'],
    'Pledged': [92774,2873519,7962,276,23963,6950],
    'Country': ['UK','USA','Poland','Bulgaria','USA','UK'],
    'Date_Start': ['2020-03-21','2020-03-11','2020-04-16',
                   '2020-02-09','2020-04-10','2020-03-19']
})
🧠 OPIS KOLUMN
Category       → typ projektu
Project_Title  → nazwa projektu
Pledged        → ile pieniędzy zebrano
Country        → kraj
Date_Start     → data startu
🔹 1. samo groupby (bez agregacji)
df.groupby('Category')

👉 co się dzieje:

Pandas dzieli dane na grupy
ALE nic jeszcze nie liczy

💥 wynik:

<pandas.core.groupby.generic.DataFrameGroupBy object>

👉 tylko „obiekt grupowania”

🔹 2. SUMA
df.groupby('Category').sum()
🧠 komentarz:
# grupujemy po Category
# sumujemy wszystkie numeryczne kolumny
df.groupby('Category').sum()

👉 wynik:

Games → suma Pledged
Film&Video → suma Pledged
🔹 3. ŚREDNIA
df.groupby('Category').mean()
🧠 komentarz:
# średnia dla każdej kategorii
df.groupby('Category').mean()

👉 pokazuje średnie finansowanie projektów

🔹 4. COUNT (liczenie)
df.groupby('Category').count()
🧠 komentarz:
# liczy ile NIE-pustych wartości w każdej kolumnie
df.groupby('Category').count()

👉 ważne:

count działa na wszystkich kolumnach
bo liczy „ile wierszy”
🔥 KLUCZOWA RÓŻNICA
funkcja	co robi
sum	dodaje liczby
mean	średnia
count	liczy wiersze
📅 5. GROUPBY + DATY (Grouper)
najpierw konwersja:
df['Date_Start'] = pd.to_datetime(df['Date_Start'])
groupby po miesiącach:
df.groupby(pd.Grouper(key='Date_Start', freq='M')).sum()
🧠 komentarz:
# key = kolumna z datą
# freq = jak grupujemy (M = miesiąc)
df.groupby(pd.Grouper(key='Date_Start', freq='M')).sum()
📌 freq znaczenie:
freq	znaczenie
M	miesiąc
Y	rok
W	tydzień
D	dzień
H	godzina
🔥 6. GROUPBY + AGG (NAJWAŻNIEJSZE)
df.groupby(pd.Grouper(key='Date_Start', freq='M')).agg({
    'Pledged': 'sum',
    'Project_Title': 'count'
})
🧠 komentarz:
# dla każdej grupy miesięcznej:
# - sumuj Pledged
# - licz projekty
📊 efekt:

| miesiąc | Pledged sum | liczba projektów |

🔥 DLACZEGO agg jest lepsze?

Bo pozwala zrobić:

różne operacje dla różnych kolumn
🔹 7. GROUPBY na wielu kolumnach
df.groupby(['Country','Category']).sum()
🧠 komentarz:
# najpierw grupuj po Country
# potem po Category
# potem sumuj Pledged
📊 efekt:

MultiIndex:

Country → Category
🔥 NAJWAŻNIEJSZA INTUICJA GROUPBY

👉 groupby = 3 kroki:

1. SPLIT

dziel dane na grupy

2. APPLY

wykonaj funkcję (sum, mean...)

3. COMBINE

złącz wynik

🧠 TL;DR
groupby() → tworzy grupy
sum() → dodaje
mean() → średnia
count() → liczba rekordów
agg() → wiele operacji naraz
Grouper() → grupowanie po czasie
🔥 Najważniejsze zdanie

👉 groupby = „mini-silnik analityczny w Pandas”



🧪 1. Top 3 kategorie według finansowania
df.groupby('Category')['Pledged'].sum().sort_values(ascending=False).head(3)
🧠 komentarz:
# 1. grupujemy po Category
# 2. sumujemy Pledged
# 3. sortujemy malejąco
# 4. bierzemy top 3
🔥 sprawdza:
groupby
sortowanie
ranking
🧪 2. Średnie finansowanie per kraj
df.groupby('Country')['Pledged'].mean()
🧠 komentarz:
# średnia kwota wsparcia w każdym kraju
🔥 sprawdza:
mean
agregacje
🧪 3. Liczba projektów w każdej kategorii i kraju
df.groupby(['Country','Category'])['Project_Title'].count()
🧠 komentarz:
# ile projektów w każdej kombinacji Country + Category
🔥 sprawdza:
multi-column groupby
count
🧪 4. Suma + liczba projektów jednocześnie (agg)
df.groupby('Category').agg({
    'Pledged': 'sum',
    'Project_Title': 'count'
})
🧠 komentarz:
# sumujemy pieniądze
# i liczymy projekty w jednej operacji
🔥 sprawdza:
agg (mega ważne na rozmowach)
🧪 5. Finansowanie miesięczne (time series)
df['Date_Start'] = pd.to_datetime(df['Date_Start'])

df.groupby(pd.Grouper(key='Date_Start', freq='M'))['Pledged'].sum()
🧠 komentarz:
# konwersja daty
# grupowanie po miesiącach
# suma finansowania w czasie
🔥 sprawdza:
daty
Grouper
time-series grouping
🧠 BONUS (bardzo rekrutacyjne)
🧪 Top projekt w każdym kraju
df.loc[df.groupby('Country')['Pledged'].idxmax()]
🧠 komentarz:
# idxmax → zwraca indeks największej wartości
# loc → wybiera cały wiersz
🔥 to jest poziom „good junior / mid interview”
🔥 NAJWAŻNIEJSZE WZORCE GROUPBY
✔️ 1 kolumna:
df.groupby('X')['Y'].sum()
✔️ wiele kolumn:
df.groupby(['X','Y'])['Z'].mean()
✔️ różne agregacje:
df.groupby('X').agg({'Y':'sum','Z':'count'})
✔️ czas:
df.groupby(pd.Grouper(key='date', freq='M'))
🧠 TL;DR (rekrutacyjne sedno)

👉 groupby = najważniejsze narzędzie analityka
👉 80% pytań = sum / mean / count / agg / top N



🧪 1. Jaka kategoria zebrała najwięcej pieniędzy?
df.groupby('Category')['Pledged'].sum().sort_values(ascending=False).head(1)
# grupujemy po Category
# sumujemy Pledged
# sortujemy malejąco
# bierzemy top 1
🧪 2. Który kraj ma najwyższą średnią wpłatę?
df.groupby('Country')['Pledged'].mean().sort_values(ascending=False).head(1)
# średnia wpłat per kraj
# ranking krajów
🧪 3. Ile projektów jest w każdej kategorii?
df.groupby('Category')['Project_Title'].count()
# count = liczba projektów
🧪 4. Ile projektów w każdym kraju i kategorii?
df.groupby(['Country','Category'])['Project_Title'].count()
# multi-level grouping
🧪 5. Top 1 projekt w każdym kraju (najwięcej pieniędzy)
df.loc[df.groupby('Country')['Pledged'].idxmax()]
# idxmax = indeks największej wartości
# loc = pobiera cały wiersz
🧪 6. Suma + liczba projektów jednocześnie
df.groupby('Category').agg({
    'Pledged': 'sum',
    'Project_Title': 'count'
})
# agg = wiele operacji naraz
🧪 7. Średnie finansowanie per kraj i kategoria
df.groupby(['Country','Category'])['Pledged'].mean()
# granularna analiza
🧪 8. Który kraj ma najwięcej projektów?
df.groupby('Country')['Project_Title'].count().sort_values(ascending=False).head(1)
# ranking krajów
🧪 9. Miesięczne finansowanie (time series)
df['Date_Start'] = pd.to_datetime(df['Date_Start'])

df.groupby(pd.Grouper(key='Date_Start', freq='M'))['Pledged'].sum()
# Grouper = grupowanie po czasie
🧪 10. Która kategoria ma największy pojedynczy projekt?
df.loc[df.groupby('Category')['Pledged'].idxmax()]
# największy pojedynczy rekord w grupie
🧠 BONUS — czego rekruter naprawdę sprawdza
✔️ groupby basics:
sum
mean
count
✔️ advanced:
agg()
idxmax / idxmin
Grouper (daty)
✔️ thinking:
„jak dzielisz dane?”
„co agregujesz?”
🔥 SUPER WAŻNA INTUICJA

👉 groupby = 3 kroki:

SPLIT → APPLY → COMBINE

czyli:

dzielisz dane
liczysz coś
łączysz wynik
🟢 TL;DR

Jeśli umiesz to:

groupby().sum()
groupby().agg()
idxmax()
Grouper


"""