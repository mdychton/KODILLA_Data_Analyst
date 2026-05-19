"""
One‑hot encoding to sposób zamiany zmiennych kategorycznych (np. „S”, „C”, „Q”) na kolumny liczbowe 0/1, które modele ML potrafią przetwarzać.

Zamiast jednej kolumny:

Kod
Embarked
S
C
Q
S
dostajesz:

C	Q
0	0
1	0
0	1
0	0


Dlaczego nie ma kolumny S?
Bo drop_first=True usuwa jedną kategorię, żeby uniknąć pułapki zmiennej fikcyjnej.

🎨 Co robi get_dummies()?
pd.get_dummies():

bierze kolumnę kategoryczną,

tworzy dla każdej kategorii osobną kolumnę,

wpisuje 1, jeśli wiersz należy do tej kategorii,

wpisuje 0, jeśli nie należy.

Najczęściej używana do:

przygotowania danych do modeli ML,

zamiany tekstu na liczby,

kodowania kategorii w regresji/logregu/lasach/XGBoost.

🧪 Przykład 1 — prosta kolumna
python
import pandas as pd

df = pd.DataFrame({'Color': ['Red', 'Blue', 'Red', 'Green']})

dummies = pd.get_dummies(df['Color'])
print(dummies)
Wynik:

Blue	Green	Red
0	0	1
1	0	0
0	0	1
0	1	0


🧪 Przykład 2 — z drop_first=True
python
dummies = pd.get_dummies(df['Color'], drop_first=True)
print(dummies)
Wynik:

Green	Red
0	1
0	0
0	1
1	0


Kolumna „Blue” została usunięta → jest kategorią bazową.

get_dummies() wybiera kategorię bazową według kolejności sortowania wartości kategorycznych, a nie według częstości.
Czyli:

jeśli masz kategorie: ['Red', 'Blue', 'Green']

Pandas sortuje je alfabetycznie:

Kod
Blue
Green
Red
i pierwszą w kolejności alfabetycznej usuwa, gdy drop_first=True


🧠 Dlaczego w Titanic pojawiają się kolumny C i Q?
Bo Embarked ma 3 wartości:

S

C

Q

A drop_first=True usuwa pierwszą kategorię (S).
Zostają:

C → 1 jeśli pasażer wsiadł w Cherbourg

Q → 1 jeśli pasażer wsiadł w Queenstown

Jeśli obie są 0 → to znaczy, że wsiadł w S.

🧩 Przykładowy kod z komentarzem (Titanic)
python
# 1. Znajdujemy najczęstszą wartość w Embarked
embarked_mode = titanic_train_prepared['Embarked'].mode()[0]

# 2. Uzupełniamy braki tą wartością
titanic_train_prepared['Embarked'] = titanic_train_prepared['Embarked'].fillna(embarked_mode)

# 3. Tworzymy kolumny 0/1 dla C i Q
dummies = pd.get_dummies(titanic_train_prepared['Embarked'], drop_first=True)

# 4. Doklejamy je do DataFrame
titanic_train_prepared = pd.concat([titanic_train_prepared, dummies], axis=1)

# 5. Usuwamy oryginalną kolumnę Embarked
titanic_train_prepared.drop(['Embarked'], axis=1, inplace=True)
🔥 Podsumowanie w jednym zdaniu
One‑hot encoding zamienia tekstowe kategorie na kolumny 0/1, a get_dummies() to najprostszy sposób w Pandas, żeby to zrobić — i jest używany w każdym projekcie ML.


"""
