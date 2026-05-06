'''

🎯 1. Zmienna numeryczna — co to jest?
To taka zmienna, która ma wartości liczbowe, zwykle ciągłe lub dyskretne.

Przykłady:
cena mieszkania: 450 000 zł

wiek: 32

wzrost: 178 cm

dochód: 5200 zł

Możesz na nich wykonywać działania matematyczne (średnia, suma, różnica).

🎯 2. Zmienna kategoryczna — co to jest?
To zmienna opisująca cechę jakościową, a nie liczbową.

Przykłady:
kolor: czerwony, zielony, czarny

płeć: kobieta, mężczyzna

miasto: Kraków, Warszawa, Gdańsk

Komputer nie rozumie słów, więc musimy je zamienić na liczby.

❗ Dlaczego NIE możemy zrobić tak:
Kod
czerwony = 1
zielony = 2
czarny = 3
Bo wtedy komputer myśli, że:

zielony > czerwony

czarny > zielony

różnica między zielonym a czarnym = 1

A to nie ma żadnego sensu, bo kolory nie mają porządku.

🎨 3. Dlatego stosujemy One‑Hot Encoding
One‑Hot Encoding zamienia kategorię na osobne kolumny 0/1.

Przykład:
Mamy kolumnę:

Kod
Color
Red
Blue
Green
Red
Po one‑hot encodingu:

Blue	Green	Red
0	0	1
1	0	0
0	1	0
0	0	1


Każda kolumna = jedna kategoria
1 = ta kategoria występuje
0 = nie występuje

🧪 4. Jak działa get_dummies()?
To funkcja Pandas, która robi one‑hot encoding.

Przykład z kodem:
python
import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Red']})

dummies = pd.get_dummies(df['Color'])
print(dummies)
Wynik:

Blue	Green	Red
0	0	1
1	0	0
0	1	0
0	0	1


🧹 5. drop_first=True — po co?
Żeby uniknąć pułapki zmiennej fikcyjnej (dummy variable trap).

Zamiast 3 kolumn:

Red

Blue

Green

zostają tylko 2:

Blue

Green

A Red jest kategorią bazową.

Przykład:
python
pd.get_dummies(df['Color'], drop_first=True)
Wynik:

Green	Red
0	1
0	0
1	0
0	1


🎓 6. Zmienna kategoryczna porządkowa (ordinal)
To kategoria, która ma sensowną kolejność.

Przykłady:
wykształcenie: podstawowe < średnie < licencjat < magister < doktor

ocena w szkole: 1 < 2 < 3 < 4 < 5 < 6

klasa biletu Titanic: 1 < 2 < 3

Tutaj kolejność ma znaczenie, więc można zostawić liczbę.

🛳️ 7. Pclass w Titanic — przykład zmiennej porządkowej
Pclass = klasa biletu:

1 = pierwsza klasa (najdroższa)

2 = druga

3 = trzecia (najtańsza)

To jest kategoria porządkowa, bo 1 < 2 < 3 ma sens.

Dlatego:

zostawiamy oryginalną kolumnę (1, 2, 3)

ale możemy też dodać one‑hot encoding, żeby model miał więcej informacji

Przykład:
python
dummies = pd.get_dummies(titanic_train_prepared['Pclass'], drop_first=True)
titanic_train_prepared = pd.concat([titanic_train_prepared, dummies], axis=1)
Powstaną kolumny:

2

3

A 1 jest kategorią bazową.

🔥 Podsumowanie w jednym zdaniu
One‑hot encoding zamienia kategorie na kolumny 0/1, get_dummies() to robi automatycznie, a stosujemy to, bo modele nie rozumieją tekstu i nie wolno im narzucać sztucznej kolejności tam, gdzie jej nie ma.


'''