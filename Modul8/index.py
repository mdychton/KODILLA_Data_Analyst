"""
🧠 Co robi index w Pandas?

👉 index to etykiety wierszy (row labels)

Czyli zamiast:

0, 1, 2, 3

możesz mieć:

Alice, Bob, Charlie

albo nawet kilka poziomów:

(School, Student)
🔑 Do czego służy index
1. Identyfikacja danych
df.loc['Alice']

➡️ wybierasz po indeksie, nie po pozycji

2. Łączenie danych (merge/join)

Pandas często dopasowuje dane właśnie po indeksie:

df1.join(df2)
3. Grupowanie i agregacje

Index często reprezentuje strukturę danych:

szkoła
student
data
poziomy organizacji
4. MultiIndex = dane wielowymiarowe

Zamiast tabeli 2D masz coś jak mini-hierarchię:

School         Student
High School X  John
               Anna
High School Y  Mike

To pozwala robić rzeczy typu:

df.loc['High School X']

➡️ dostajesz wszystkich studentów z tej szkoły

⚠️ Index ≠ kolumna

To ważne:

kolumna → zwykłe dane
index → sposób organizacji i dostępu do danych
🔥 W Twoim przypadku

Masz coś typu:

(e1, e2, e3, semestr1)

To znaczy:
👉 te wartości definiują unikalny wiersz

Po dodaniu:

df.set_index('School', append=True)

masz:

(School, e1, e2, e3, semestr1)

czyli:
👉 każdy wiersz = konkretna szkoła + konkretne parametry

🧩 Kiedy używać indexu?

✔️ gdy:

dane mają hierarchię
chcesz łatwo filtrować (.loc)
robisz agregacje

❌ gdy:

to zwykła kolumna informacyjna (np. imię bez znaczenia strukturalnego)
TL;DR

👉 index = sposób organizacji danych + klucz do ich wyboru
👉 MultiIndex = kilka poziomów tej organizacji (hierarchia)


🧠 1. Co naprawdę jest index?

👉 index to ID wiersza

Nie musi to być liczba.

Może być:

liczba → 0,1,2
tekst → "Alice", "Bob"
data → "2024-01-01"
para wartości → (School, Student)
🔥 Najważniejsze:

👉 index = sposób nazywania i znajdowania wierszy

📌 2. Różnica: index vs kolumna
Kolumna	Index
dane w środku tabeli	„etykieta wiersza”
np. name, age	np. ID, data, klucz
przykład:
df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "age": [20, 30]
}, index=["A", "B"])
        name   age
A       Alice  20
B       Bob    30

👉 A, B to index
👉 name, age to kolumny

🔥 3. Co robi .loc
df.loc["A"]

👉 mówi:

„daj mi wiersz o indexie A”

czyli:

name = Alice
age = 20

📌 ważne:

.loc → działa po indexie (etykiecie)
.iloc → działa po pozycji (0,1,2)
🔗 4. Dlaczego index jest ważny przy łączeniu?
przykład:
df1.join(df2)

pandas robi:

„dopasuj wiersze, które mają TEN SAM index”

czyli:

A z A
B z B

👉 jeśli index się nie zgadza → dostajesz NaN

🧠 5. MultiIndex (czyli „index w indexie”)

To jest po prostu hierarchia

np:

School        Student
High School   John
              Anna

👉 to NIE są 2 kolumny
👉 to jest jedna struktura indexu na 2 poziomach

Jak to działa:
df.loc["High School"]

👉 dostajesz wszystkich studentów z tej szkoły

🔥 6. Co znaczy:
df.set_index(['School', 'Student'])

👉 mówisz:

„te dwie kolumny to teraz identyfikator wiersza”

czyli:

(School, Student) → jeden unikalny wiersz
⚠️ 7. Najważniejsza intuicja

👉 index NIE jest danymi
👉 index to sposób dostępu do danych

💥 8. Kiedy index ma sens?
✔ DOBRZE:
ID klienta
data
kategoria
struktura organizacyjna
❌ ŹLE:
imię (jeśli nie jest unikalne)
zwykłe kolumny opisowe
przypadkowe wartości
🔥 TL;DR (najprostsze możliwe)

👉 index = „jak znaleźć wiersz”
👉 kolumna = „co jest w wierszu”
👉 MultiIndex = „kilka warstw znajdowania”

🧠 Jedno zdanie, które robi klik:

👉 pandas NIE myśli „wiersz 0,1,2”
👉 pandas myśli „wiersz o ID = X”


"""