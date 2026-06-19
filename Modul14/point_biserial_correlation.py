"""
KORELACJA PUNKTOWO-BISEKCYJNA

Dlaczego używamy pointbiserialr?

Funkcja:

stats.pointbiserialr()

liczy korelację punktowo-dwuseryjną.

Jest to specjalny przypadek korelacji Pearsona używany wtedy, gdy:

jedna zmienna jest liczbowa,
druga jest binarna (0/1).

W Twoim przypadku:

PlasmaGlucose -> liczba
Diabetic -> 0 lub 1

więc jest to idealne zastosowanie.

Jak działa pętla?

Pierwsza iteracja:

col = 'Pregnancies'

wykonuje:

stats.pointbiserialr(X['Pregnancies'], y)

Druga iteracja:

col = 'PlasmaGlucose'

wykonuje:

stats.pointbiserialr(X['PlasmaGlucose'], y)

I tak dla wszystkich cech.

Co zwraca pointbiserialr?

Funkcja zwraca dwie wartości:

(r, pvalue)

gdzie:

r = współczynnik korelacji
pvalue = wartość p testu statystycznego

Przykład:

(0.64, 0.000001)

W kodzie:

[0]

oznacza:

stats.pointbiserialr(X[col], y)[0]

czyli:

pobierz tylko współczynnik korelacji.

Co trafia do słownika?

Po wykonaniu pętli słownik może wyglądać tak:

corr_dict = {
    'PlasmaGlucose': 0.67,
    'BMI': 0.34,
    'Age': 0.22,
    'Pregnancies': 0.19,
    'SerumInsulin': 0.12
}
Ostatnia linia
pd.Series(corr_dict).sort_values(ascending=False)

zamienia słownik na serię Pandas:

PlasmaGlucose    0.67
BMI              0.34
Age              0.22
Pregnancies      0.19
SerumInsulin     0.12

oraz sortuje od największej wartości.

Jak interpretować wyniki?

Współczynnik korelacji może przyjmować wartości od:

-1  do  1
Wartość	Interpretacja
1	bardzo silna dodatnia zależność
0.7	silna dodatnia zależność
0.3	umiarkowana zależność
0	brak zależności
-0.3	umiarkowana ujemna zależność
-1	bardzo silna ujemna zależność

Przykład:

PlasmaGlucose    0.68
BMI              0.35
Age              0.21

oznacza:

im wyższy poziom glukozy, tym większe prawdopodobieństwo cukrzycy,
BMI również jest związane z cukrzycą,
wiek ma słabszy wpływ.
Po co to robimy?

To jest analiza cech (feature analysis) przed budową modelu.

Pozwala szybko sprawdzić:

które zmienne są najbardziej związane z klasą Diabetic,
które mogą być najważniejsze dla modelu,
czy istnieją cechy o bardzo słabym związku z wynikiem.

W przypadku zbiorów dotyczących cukrzycy zwykle najwyższą korelację z Diabetic mają:

PlasmaGlucose
BMI
Age
Pregnancies

co często potwierdzają później modele uczenia maszynowego.


"""