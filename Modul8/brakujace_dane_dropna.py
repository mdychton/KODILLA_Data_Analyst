"""
🧠 BRAKUJĄCE DANE (NaN) w Pandas
📌 Co to jest NaN?

👉 NaN = brakująca wartość (Not a Number)

W Pandas oznacza:

brak danych
nieznana wartość
pusta komórka
📊 1. Tworzenie danych z brakami
df_with_nulls = pd.DataFrame({
    'A': [1,100,np.nan,1000,10000],
    'B': [2,4,2,4,np.nan],
    'C': [40,np.nan,20,np.nan,np.nan]
})
🧠 komentarz:
# np.nan = brak danych
# każda kolumna ma różną liczbę braków
🔍 2. Sprawdzanie braków
✔️ ile braków w kolumnach
df_with_nulls.isnull().sum()
🧠 komentarz:
# True = brak
# False = jest wartość
# sum() liczy True jako 1
✔️ procent braków
df_with_nulls.isnull().mean()
🧠 komentarz:
# mean = średnia z True/False
# daje % braków w kolumnie
🔍 3. filtrowanie braków
df_with_nulls[df_with_nulls['C'].isnull()]
🧠 komentarz:
# pokazuje tylko wiersze gdzie C jest puste
🧹 4. DROPNA — usuwanie braków
❌ domyślne (bardzo agresywne)
df_with_nulls.dropna()
🧠 komentarz:
# usuwa każdy wiersz z choć jednym NaN

👉 zostaje tylko „czysty” wiersz

⚖️ 5. THRESH — kontrola jakości danych
df_with_nulls.dropna(thresh=2)
🧠 komentarz:
# thresh = minimalna liczba NIE-NaN wartości
# tutaj: wiersz musi mieć min 2 wartości

👉 czyli:

2+ wartości → zostaje
mniej → usuwamy
📊 6. usuwanie kolumn (axis=1)
df_with_nulls.dropna(thresh=3, axis=1)
🧠 komentarz:
# axis=1 → działamy na kolumnach
# kolumna musi mieć min 3 wartości

👉 efekt:

kolumna C znika (za dużo braków)
🧠 7. missingno (wizualizacja braków)
import missingno as msno
msno.matrix(df_with_nulls)
🧠 komentarz:
# biały = brak danych (NaN)
# szary = dane istnieją
🔥 CO WIDZISZ NA WYKRESIE?

👉 pionowe linie = kolumny
👉 białe dziury = braki
👉 przesunięcia = wzorce braków

🧠 INTUICJA (bardzo ważne)
📌 dropna = „wyrzuć dane”
📌 isnull = „sprawdź braki”
📌 missingno = „zobacz braki”
🔥 NAJWAŻNIEJSZE WZORCE
✔️ ile braków
df.isnull().sum()
✔️ % braków
df.isnull().mean()
✔️ usuń wiersze
df.dropna()
✔️ usuń kolumny
df.dropna(axis=1)
✔️ kontrola jakości
df.dropna(thresh=...)
🧠 TL;DR

👉 NaN = brak danych
👉 Pandas daje 3 główne narzędzia:

isnull() → wykryj
dropna() → usuń
fillna() → uzupełnij (to kolejny krok)
🔥 Najważniejsza intuicja

👉 brak danych to NIE błąd
👉 to informacja o jakości datasetu

"""