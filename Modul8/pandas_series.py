"""
🔹 Czym jest Series (w skrócie)
1-wymiarowa struktura danych w pandas
coś jak kolumna w Excelu / DataFrame
bazuje na NumPy (ndarray), ale ma indeks (etykiety)
🔹 Najważniejsze cechy (must-know)
1. Indeks (kluczowa różnica vs NumPy)
pd.Series(exam1, labels)
możesz używać własnych etykiet:
e1['Student D']

✔ To jest ogromna przewaga nad ndarray

2. Tworzenie Series – 3 główne sposoby
✔ z listy + indeks
pd.Series([10,20], ['A','B'])
✔ ze słownika (często najlepsze)
pd.Series({'A':10, 'B':20})
✔ z jednego skalaru
pd.Series(5, index=['A','B'])
3. Operacje matematyczne (auto-align!)
e1 + e2

👉 ważne:

Pandas dopasowuje po indeksach, nie po kolejności

Przykład:

s1 = pd.Series([1,2], ['A','B'])
s2 = pd.Series([10,20], ['B','C'])

s1 + s2

wynik:

A NaN
B 12
C NaN

✔ To jest bardzo ważne — często źródło błędów

4. Automatyczna obsługa typów
int → float przy dzieleniu ✔
brak wartości = NaN
5. Broadcasting
e1 / 5

działa jak w NumPy

🔹 Rzeczy, których brakuje (ważne w praktyce)
6. Dostęp do danych — BEST PRACTICE

Zamiast:

e1['Student A']

✔ używaj:

e1.loc['Student A']   # po etykiecie
e1.iloc[0]            # po pozycji

👉 bardziej przewidywalne i bezpieczne

7. Sprawdzanie podstawowych info
e1.index
e1.values
e1.dtype
8. Braki danych (NaN)
e1.isna()
e1.dropna()
e1.fillna(0)

👉 Pandas zawsze wprowadza NaN przy niedopasowaniu indeksów

9. Operacje statystyczne (bardzo często używane)
e1.mean()
e1.sum()
e1.max()
e1.min()
10. Filtrowanie (super ważne)
e1[e1 > 80]
🔹 Best Practices (praktyczne zasady)
✔ 1. Używaj słowników do tworzenia Series

Zamiast:

pd.Series(exam1, labels)

lepiej:

pd.Series(dict(zip(labels, exam1)))

lub od razu:

pd.Series({'A': 10, 'B': 20})

👉 mniejsze ryzyko pomyłki kolejności

✔ 2. Zawsze myśl o indeksie

To nie lista — to mapa (key → value)

✔ 3. Uważaj na operacje między Series
Pandas dopasowuje po indeksach
brak dopasowania = NaN

👉 często trzeba:

e1.add(e2, fill_value=0)
✔ 4. Używaj .loc / .iloc

Unikaj:

e1['A']
✔ 5. Dbaj o typy danych

Po operacjach:

e1.dtype
✔ 6. Konwertuj do DataFrame gdy robi się większe

Series jest ok dla:

jednej kolumny

Ale przy większych danych:

pd.DataFrame(...)
✔ 7. Nazwy!
e1.name = "Exam 1"

👉 bardzo pomaga przy analizie i merge

🔹 Mentalny model (bardzo pomaga)

Myśl o Series jako:

słownik + NumPy + indeks

czyli:

jak dict → ma klucze
jak array → robi szybkie obliczenia
🔹 Podsumowanie

Najważniejsze rzeczy:

✔ Series = 1D dane + indeks
✔ indeks = kluczowa funkcja
✔ operacje dopasowują się po indeksach
✔ NaN pojawia się automatycznie
✔ .loc / .iloc to standard
✔ świetne do prostych analiz i jednej kolumny

"""