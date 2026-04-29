""""
# 📥 Wczytanie wszystkich tabel HTML ze strony
# pd.read_html zwraca listę DataFrame’ów
tables = pd.read_html(url, header=0)

url = "https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"

table_1 = pd.read_html(
    url,
    header=0,
    storage_options={
        "User-Agent": "Mozilla/5.0"
    }
)




# 📊 Wybór pierwszej tabeli z listy (najczęściej właściwa tabela)
df = tables[0]

# 🧹 Usunięcie zbędnych spacji z nazw kolumn
df.columns = df.columns.str.strip()

# 🌍 Zmiana nazw kolumn na polskie odpowiedniki
df = df.rename(columns={
    'TITLE': 'TYTUŁ',
    'ARTIST': 'ARTYSTA',
    'YEAR': 'ROK',
    'HIGH POSN': 'MAX POZ'
})

# 📌 ANALIZA DANYCH

# 🔢 liczba unikalnych artystów na liście
print("Liczba pojedynczych artystów:")
print(df['ARTYSTA'].nunique())

# 🏆 top 10 najczęściej występujących artystów
print("\nNajczęściej występujący artyści:")
print(df['ARTYSTA'].value_counts().head(10))

# 📅 rok, w którym wydano najwięcej albumów
print("\nRok z największą liczbą albumów:")
print(df['ROK'].value_counts().idxmax())

# 📆 liczba albumów wydanych między 1960 a 1990 rokiem (włącznie)
print("\nAlbumy z lat 1960–1990:")
print(df[(df['ROK'] >= 1960) & (df['ROK'] <= 1990)].shape[0])

# 🧒 najnowszy (najmłodszy) album na liście
print("\nNajmłodszy rok wydania albumu:")
print(df['ROK'].max())

# 📉 najwcześniejszy album każdego artysty
# idxmin → zwraca indeks wiersza z najstarszym rokiem dla każdego artysty
earliest = df.loc[df.groupby('ARTYSTA')['ROK'].idxmin()]

# 💾 zapis wyniku do pliku CSV
earliest.to_csv('earliest_albums.csv', index=False)

print("\nZapisano plik: earliest_albums.csv")

"""