"""
🔹 Pivot table – proste wyjaśnienie

pivot_table w Pandas działa bardzo podobnie jak tabela przestawna w Excelu.
Pozwala szybko podsumować dane (np. sumy, średnie) w podziale na różne kategorie.

🔹 Przykład – suma sprzedaży
import pandas as pd
import numpy as np

# wczytanie danych
df = pd.read_excel('Pivot.xlsx')

# tabela przestawna
pivot = df.pivot_table(
    values='Sprzedaż',          # kolumna z wartościami do policzenia
    index='Przedstawiciel',     # wiersze (kto sprzedaje)
    columns='Region',           # kolumny (gdzie sprzedaje)
    aggfunc=np.sum              # sposób agregacji (tu: suma)
)

pivot

👉 Co tu się dzieje:

bierzemy kolumnę Sprzedaż
grupujemy po:
wierszach → Przedstawiciel
kolumnach → Region
liczymy sumę sprzedaży
🔹 Poprawa czytelności
pivot = df.pivot_table(
    values='Sprzedaż',
    index='Przedstawiciel',
    columns='Region',
    aggfunc=np.sum
).fillna(0).round(2)   # NaN → 0, zaokrąglenie do 2 miejsc

pivot

👉 Dzięki temu:

brak danych = 0 (zamiast NaN)
liczby są ładniejsze (np. 1234.57)
🔹 Wiele poziomów (MultiIndex)
pivot = df.pivot_table(
    values='Sprzedaż',
    index=['Region', 'Przedstawiciel'],  # najpierw region, potem osoba
    aggfunc=np.sum
).round(2)

pivot

👉 Efekt:

masz zagnieżdżone grupowanie
najpierw Region → potem Przedstawiciel
🔹 Sortowanie (często potrzebne!)
pivot = df.pivot_table(
    values='Sprzedaż',
    index=['Region', 'Przedstawiciel'],
    aggfunc=np.sum
).round(2)

# sortowanie: region rosnąco + sprzedaż malejąco
pivot = pivot.sort_values(
    by=['Region', 'Sprzedaż'],
    ascending=[True, False]
)

pivot

👉 Czyli:

regiony A → Z
w każdym regionie najlepsi sprzedawcy na górze
🔹 Wiele agregacji naraz
pivot = df.pivot_table(
    values='Sprzedaż',
    index='Region',
    aggfunc=[len, np.max, np.min]   # liczba, max, min
).round(0)

pivot

👉 Dostajesz:

ile było transakcji (len)
największa sprzedaż (max)
najmniejsza sprzedaż (min)
🔹 Najprostsze podsumowanie

pivot_table =
👉 groupby + agregacja + reshaping w jedną tabelę

"""