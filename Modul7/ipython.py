"""
IPYTHON – NAJWAŻNIEJSZE NA START

%run file.py – uruchamia plik Pythona jako program
%time command – mierzy czas wykonania jednej komendy
%timeit command – dokładny pomiar wydajności (wiele powtórzeń)
%whos – pokazuje wszystkie zmienne w pamięci (typy + wartości)
%who – pokazuje tylko nazwy zmiennych
%matplotlib inline – włącza wykresy w notebooku (statyczne)
%pwd – pokazuje aktualny katalog roboczy
%ls – listuje pliki w katalogu
%cd folder/ – zmienia katalog roboczy
%load file.py – wczytuje plik do komórki (bez uruchamiania)
%history – pokazuje historię komend
%reset – czyści wszystkie zmienne z pamięci
%debug – wchodzi w tryb debugowania po błędzie
object? – pokazuje dokumentację obiektu
object?? – pokazuje kod źródłowy (jeśli dostępny)

"""


"""
IPYTHON – CODZIENNY WORKFLOW DATA ANALYST
%run script.py – uruchamia pipeline / ETL / czyszczenie danych
%timeit df.groupby(...).mean() – sprawdza wydajność operacji na danych
%whos – kontroluje, jakie DataFrame’y i zmienne są w pamięci
df.head() – szybki podgląd danych
df.info() – sprawdza typy kolumn i braki danych
df.describe() – szybka statystyka danych
df[df["col"] > value] – filtrowanie danych
%matplotlib inline – wyświetlanie wykresów (EDA)
df.plot() / plt.plot() – szybkie wizualizacje
cursor.execute("SELECT ...").fetchall() – szybkie zapytania SQL
%pwd / %ls – ogarnianie plików i ścieżek
%history – wracanie do wcześniejszych komend
object? – sprawdzanie dokumentacji funkcji
%debug – debugowanie błędów krok po kroku
%reset – czyszczenie środowiska przed nową analizą
🧠 Jak to wygląda w praktyce (flow)
%run load_data.py → wczytanie danych
df.head() → szybki preview
df.info() → sprawdzenie jakości
df.groupby(...).agg(...) → analiza
%timeit → optymalizacja
df.plot() → wizualizacja
SQL → joiny / dodatkowe dane
%whos → kontrola pamięci
🎯 Najważniejsze

👉 IPython to:

szybkie eksperymenty
debugowanie
analiza danych
testowanie kodu bez odpalania całego projektu


"""