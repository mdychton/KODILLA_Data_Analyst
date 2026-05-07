📦 Import bibliotek

import pandas as pd  # import biblioteki pandas do analizy danych tabelarycznych
import matplotlib.pyplot as plt  # import matplotlib do tworzenia wykresów

📥 1. Wczytanie danych
movies = pd.read_csv('tmdb_movies.csv')  # wczytanie bazy filmów do DataFrame movies
genres = pd.read_csv('tmdb_genres.csv')  # wczytanie bazy gatunków do DataFrame genres

⭐ 2. Top 10 najwyżej ocenianych filmów
📊 Obliczenie 3. kwartyla

q3 = movies['vote_count'].quantile(0.75)  # obliczenie 3 kwartyla liczby głosów (75% wartości)

🎬 Filtrowanie i sortowanie
top_movies = (
    movies[movies['vote_count'] > q3]  # wybór filmów z liczbą głosów większą niż 3 kwartyl
    .sort_values('vote_average', ascending=False)  # sortowanie malejąco po średniej ocenie
    [['title', 'vote_average', 'vote_count']]  # wybór tylko potrzebnych kolumn
    .head(10)  # pobranie 10 najlepszych filmów
)
📤 Wyświetlenie wyników

print(top_movies)  # wypisanie wynikowej tabeli


📅 3. Średni revenue i budget (2010–2016)
🕒 Konwersja daty i wyciągnięcie roku
movies['release_date'] = pd.to_datetime(movies['release_date'])  # zamiana tekstu na format daty
movies['year'] = movies['release_date'].dt.year  # wyciągnięcie roku z daty
🔍 Filtrowanie zakresu lat
movies_2010_2016 = movies[
    (movies['year'] >= 2010) &  # filtr od roku 2010
    (movies['year'] <= 2016)    # filtr do roku 2016
]
📊 Grupowanie danych
grouped = (
    movies_2010_2016
    .groupby('year')[['revenue', 'budget']]  # grupowanie po roku
    .mean()  # liczenie średnich wartości
)
📈 4. Wykres
🖼️ Utworzenie figury i osi
fig, ax = plt.subplots(figsize=(10,6))  # stworzenie wykresu o określonym rozmiarze
📊 Wykres słupkowy (revenue)
grouped['revenue'].plot(
    kind='bar',  # wykres słupkowy
    ax=ax,  # rysowanie na tej samej osi
    label='Średni revenue'  # opis w legendzie
)
📈 Wykres liniowy (budget)
grouped['budget'].plot(
    kind='line',  # wykres liniowy
    ax=ax,  # ta sama oś
    color='red',  # kolor linii
    marker='o',  # punkty na wykresie
    linewidth=3,  # grubość linii
    label='Średni budget'  # opis w legendzie
)
🏷️ Opisy osi i tytuł
ax.set_title('Średni revenue i budget filmów (2010-2016)')  # tytuł wykresu
ax.set_xlabel('Rok')  # opis osi X
ax.set_ylabel('Kwota')  # opis osi Y
📌 Legenda
ax.legend(
    loc='upper left',  # pozycja legendy
    bbox_to_anchor=(1,1)  # przesunięcie legendy poza wykres
)
🎯 Dopasowanie i wyświetlenie
plt.tight_layout()  # automatyczne dopasowanie elementów
plt.show()  # wyświetlenie wykresu
🔗 5. Połączenie tabel
movies_with_genres = movies.merge(
    genres,  # druga tabela
    left_on='genre_id',  # klucz w tabeli movies
    right_on='id',  # klucz w tabeli genres
    how='left'  # zachowanie wszystkich filmów
)
🏆 6. Najczęstszy gatunek
genre_count = movies_with_genres['genres'].value_counts()  # liczba wystąpień każdego gatunku

most_common_genre = genre_count.idxmax()  # gatunek z największą liczbą filmów
count = genre_count.max()  # liczba filmów tego gatunku

print("Najczęstszy gatunek:", most_common_genre)  # wypisanie gatunku
print("Liczba filmów:", count)  # wypisanie liczby
⏱️ 7. Najdłuższy średni runtime



📊 Obliczenia
runtime_mean = (
    movies_with_genres
    .groupby('genres')['runtime']  # grupowanie po gatunku
    .mean()  # średni czas trwania
)

longest_genre = runtime_mean.idxmax()  # gatunek z najdłuższym średnim czasem
longest_runtime = runtime_mean.max()  # wartość tego czasu

print("Najdłuższy średni runtime:")
print(longest_genre)
print(longest_runtime)
📊 8. Histogram runtime
longest_movies = movies_with_genres[
    movies_with_genres['genres'] == longest_genre  # wybór filmów danego gatunku
]

plt.figure(figsize=(10,6))  # rozmiar wykresu

plt.hist(longest_movies['runtime'], bins=20)  # histogram czasu trwania

plt.title(f'Histogram runtime - {longest_genre}')  # tytuł
plt.xlabel('Czas trwania filmu')  # oś X
plt.ylabel('Liczba filmów')  # oś Y

plt.show()  # wyświetlenie