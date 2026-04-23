"""
📊 Dane startowe
import pandas as pd

df = pd.DataFrame({
    'A': [100, 44, 56, 99, 85, 100],
    'B': ['Panda', 'Snake', 'Snake', 'Rat', 'Dog', 'Panda']
})
🔹 1. unique() — jakie wartości są w kolumnie?
df['B'].unique()
💡 komentarz:
# zwraca wszystkie unikalne wartości (bez powtórzeń)
# typ: numpy array
🔥 wynik:
['Panda', 'Snake', 'Rat', 'Dog']
🔹 2. nunique() — ile jest unikalnych wartości?
df['B'].nunique()
💡 komentarz:
# zwraca LICZBĘ unikalnych wartości
🔥 wynik:
4
🔥 szybkie porównanie:
funkcja	wynik
unique()	lista wartości
nunique()	liczba wartości
🔹 3. value_counts() — ile razy coś występuje
df['B'].value_counts()
💡 komentarz:
# liczy wystąpienia każdej wartości
# zwraca Series
🔥 wynik:
Panda    2
Snake    2
Rat      1
Dog      1
🔥 wersja procentowa
df['B'].value_counts(normalize=True)
💡 komentarz:
# pokazuje udział procentowy (0-1)
🔥 wynik:
Panda    0.33
Snake    0.33
Rat      0.17
Dog      0.17
🔹 4. sort_values() — sortowanie
df.sort_values(by='A')
💡 komentarz:
# sortuje rosnąco według kolumny A
🔥 malejąco:
df.sort_values(by='A', ascending=False)
💡 komentarz:
# ascending=False → od największej do najmniejszej
🔹 5. drop_duplicates() — usuwanie duplikatów
df.drop_duplicates()
💡 komentarz:
# usuwa identyczne wiersze
# zostawia tylko unikalne rekordy
🔥 WAŻNE

Jeśli masz:

A=100, B=Panda
A=100, B=Panda   <-- duplikat

👉 drugi wiersz znika

🔹 6. subset — sprawdzanie tylko wybranych kolumn
df.drop_duplicates(subset=['B'])
💡 komentarz:
# sprawdza duplikaty tylko w kolumnie B
# A jest ignorowane
🔥 efekt:

Zostaje pierwsze wystąpienie każdej wartości B

🔹 7. keep — który duplikat zostawić
✔️ first (domyślnie)
df.drop_duplicates(keep='first')

👉 zostawia pierwszy

✔️ last
df.drop_duplicates(keep='last')

👉 zostawia ostatni

❌ False
df.drop_duplicates(keep=False)

👉 usuwa WSZYSTKIE duplikaty

🔥 INTUICJA (mega ważne)
funkcja	co robi
unique	jakie wartości istnieją
nunique	ile jest unikalnych
value_counts	ile razy występują
sort_values	porządkuje dane
drop_duplicates	usuwa powtórki
🧠 PROSTA ANALOGIA

Wyobraź sobie kolumnę jak listę osób:

unique() → kto tam jest?
nunique() → ile różnych osób?
value_counts() → kto ile razy przyszedł?
sort_values() → ustaw ludzi wg wieku/wyniku
drop_duplicates() → usuń powtarzające się wpisy
🔥 PRO TIP (praktyka)

W analizie danych najczęściej robisz:

df['B'].value_counts().head(10)   #top 10 najczęstszych wartości

"""