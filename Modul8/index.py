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

"""