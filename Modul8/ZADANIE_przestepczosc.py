"""
🔥 1. Wczytanie danych
import pandas as pd

# wczytanie danych o śmiertelnych interwencjach policji
df = pd.read_csv('fatal-police-shootings-data.csv')

📌 Co robimy:

ładujemy bazę incydentów
każda linia = jedno zdarzenie
🔥 2. Zestawienie: rasa + choroba psychiczna
# grupujemy dane:
# - race (rasa ofiary)
# - signs_of_mental_illness (czy były objawy choroby psychicznej)

race_mental = df.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)

# zmiana nazw kolumn dla czytelności
race_mental.columns = ['No_mental_illness', 'Mental_illness']

📌 Co robimy:

liczymy ile osób w każdej rasie miało / nie miało objawów
unstack() rozbija dane na kolumny
🔥 3. Odsetek choroby psychicznej (MAP / APPLY)
# obliczamy procent osób z objawami choroby psychicznej
race_mental['mental_illness_pct'] = race_mental.apply(
    lambda row: (row['Mental_illness'] / (row['Mental_illness'] + row['No_mental_illness'])) * 100,
    axis=1
)

📌 Co robimy:

.apply() działa na wierszach
liczymy procent dla każdej rasy
🧠 odpowiedź na pytanie: która rasa ma najwyższy %
race_mental.sort_values('mental_illness_pct', ascending=False)

👉 pierwsza pozycja = najwyższy odsetek

🔥 4. Dzień tygodnia + wykres
import matplotlib.pyplot as plt

# konwersja daty
df['date'] = pd.to_datetime(df['date'])

# dodanie dnia tygodnia
df['weekday'] = df['date'].dt.day_name()

# liczenie incydentów
weekday_counts = df['weekday'].value_counts()
📊 sortowanie od poniedziałku do niedzieli
order = [
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday'
]

weekday_counts = weekday_counts.reindex(order)
📉 wykres
weekday_counts.plot(kind='bar')
plt.title('Incydenty według dnia tygodnia')
plt.xlabel('Dzień tygodnia')
plt.ylabel('Liczba incydentów')
plt.show()
🔥 5. Populacja + skróty + incydenty (NAJWAŻNIEJSZE)
📌 5.1 incydenty per stan
incidents = df['state'].value_counts().reset_index()
incidents.columns = ['abbr', 'count']
📌 5.2 populacja
url_pop = "https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"

pop_table = pd.read_html(url_pop, header=0, storage_options={"User-Agent": "Mozilla/5.0"})
pop_df = pop_table[0]

# czyszczenie nazw kolumn
pop_df.columns = pop_df.columns.str.replace(r"\[.*\]", "", regex=True).str.strip()

# wybór danych
pop = pop_df[['State', 'Census population, April 1, 2020']].copy()
pop.columns = ['state', 'population']
📌 5.3 skróty stanów
url_codes = "https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations"

codes_table = pd.read_html(url_codes, header=0, storage_options={"User-Agent": "Mozilla/5.0"})

codes = codes_table[2][['State', 'USPS Code']].copy()
codes.columns = ['state', 'abbr']
📌 5.4 merge (łączenie tabel)
# 1. incydenty + skróty
df_final = incidents.merge(codes, on='abbr', how='left')

# 2. dodanie populacji
df_final = df_final.merge(pop, on='state', how='left')
📌 5.5 czyszczenie danych
# usuwamy DC (brak populacji)
df_final = df_final.dropna(subset=['population'])
📌 5.6 KPI: incydenty na 1000 mieszkańców
df_final['incidents_per_1000'] = (
    df_final['count'] / df_final['population']
) * 1000
📊 wynik końcowy
result = df_final.sort_values('incidents_per_1000', ascending=False)

result[['abbr', 'state', 'incidents_per_1000']].head(10)

"""