"""
Imputacja brakujących wartości metodą kNN w uczeniu maszynowym
Wprowadzenie

Zbiory danych często zawierają brakujące wartości (missing values), co może powodować problemy dla wielu algorytmów uczenia maszynowego.

Dlatego dobrą praktyką jest wykrycie i uzupełnienie brakujących danych przed rozpoczęciem budowy modelu. Proces ten nazywa się imputacją danych (data imputation).

Jedną z popularnych metod imputacji jest wykorzystanie modelu do przewidywania brakujących wartości. Dla każdej kolumny zawierającej braki tworzony jest model, który na podstawie pozostałych danych szacuje brakujące wartości.

Bardzo często stosowanym algorytmem jest k-Nearest Neighbors (kNN), czyli k najbliższych sąsiadów. Metoda ta okazała się skuteczna w wielu eksperymentach i jest znana jako:

Nearest Neighbor Imputation (imputacja najbliższym sąsiadem)
KNN Imputation (imputacja metodą kNN)
Czego nauczysz się z tego materiału?

Po jego przeczytaniu będziesz wiedzieć:

jak oznaczać brakujące wartości za pomocą NaN,
jak wczytać plik CSV z brakującymi danymi,
jak policzyć liczbę i procent braków w każdej kolumnie,
jak uzupełniać braki za pomocą algorytmu kNN,
jak stosować imputację podczas trenowania i oceniania modeli,
jak używać imputacji przy przewidywaniu nowych danych.
1. Czym są brakujące wartości?

W zbiorze danych mogą występować rekordy, w których niektóre informacje nie zostały zapisane.

Przykład:

Age	BMI	Glucose
35	27.1	120
42	?	145
29	23.5	?

Znaki ? oznaczają brak danych.

Braki mogą wynikać z:

błędów pomiaru,
uszkodzonych danych,
nieuzupełnionych formularzy,
niedostępności informacji.
2. Dlaczego brakujące dane są problemem?

Większość algorytmów ML wymaga:

wartości liczbowej w każdej komórce,
kompletnego zestawu danych.

Przykładowo:

Age    BMI    Glucose
35     27.1   120
42     NaN    145

Wiele modeli nie będzie potrafiło pracować z wartością NaN.

3. Czym jest imputacja?

Imputacja polega na zastąpieniu brakujących danych oszacowaną wartością.

Przykład:

Przed imputacją:

Age	BMI
35	27.1
42	NaN
38	29.0

Po imputacji:

Age	BMI
35	27.1
42	28.0
38	29.0
4. Jak działa KNN Imputation?

Załóżmy, że mamy pacjenta:

Age	Glucose	BMI
45	150	NaN

Brakuje BMI.

Algorytm:

Krok 1

Szuka najbardziej podobnych pacjentów.

Przykład:

Age	Glucose	BMI
46	148	31
44	152	29
47	149	30

Są oni bardzo podobni pod względem wieku i poziomu glukozy.

Krok 2

Wybiera k najbliższych sąsiadów.

Jeśli:

k = 3

wybierze trzech najbardziej podobnych pacjentów.

Krok 3

Oblicza średnią z ich BMI.

(31 + 29 + 30) / 3 = 30
Krok 4

Wstawia obliczoną wartość.

Age	Glucose	BMI
45	150	30

Brak został uzupełniony.

5. Dlaczego metoda kNN działa dobrze?

Zamiast wpisywać:

0
średnią całej kolumny
medianę

wykorzystujemy informacje od najbardziej podobnych obserwacji.

Dla danych medycznych jest to często dużo bardziej realistyczne.

Przykład:

Pacjent:

wiek 70 lat
glukoza 200

powinien być porównywany do podobnych pacjentów, a nie do wszystkich osób w zbiorze.

6. Co oznacza „k”?

Parametr:

k = 5

oznacza:

użyj 5 najbliższych sąsiadów do oszacowania brakującej wartości.

Przykłady:

k	Znaczenie
1	tylko najbliższy sąsiad
3	trzech najbliższych
5	pięciu najbliższych
10	dziesięciu najbliższych

Najczęściej używa się:

k = 3
k = 5
k = 7
7. Jak mierzone jest podobieństwo?

Najczęściej stosuje się odległość euklidesową.

Dla dwóch punktów:

Pacjent A = (40, 120)
Pacjent B = (42, 125)

odległość wynosi:

(42−40)
2
+(125−120)
2
	​


Im mniejsza odległość, tym pacjenci są bardziej podobni.

8. Co oznacza ten cytat z artykułu?

"A new sample is imputed by finding the samples in the training set closest to it and averages these nearby points to fill in the value."

Tłumaczenie:

Nowa obserwacja jest uzupełniana poprzez znalezienie najbardziej podobnych obserwacji w zbiorze treningowym i obliczenie średniej z ich wartości.

9. Zastosowanie do Twojego zbioru o cukrzycy

Masz kolumny:

Pregnancies
PlasmaGlucose
DiastolicBloodPressure
TricepsThickness
SerumInsulin
BMI
DiabetesPedigree
Age
Diabetic

Jeżeli w kolumnie BMI pojawi się brak:

BMI = NaN

to KNNImputer:

znajdzie pacjentów o podobnym wieku,
podobnym poziomie glukozy,
podobnym ciśnieniu,
podobnej liczbie ciąż itd.

a następnie wyliczy najbardziej prawdopodobne BMI i wstawi je zamiast NaN.

Podsumowanie

KNN Imputation to metoda uzupełniania brakujących danych polegająca na:

znalezieniu najbardziej podobnych rekordów,
wybraniu k najbliższych sąsiadów,
obliczeniu średniej (lub średniej ważonej) ich wartości,
zastąpieniu brakującej wartości wynikiem.

Dla Twojego zbioru o cukrzycy jest to często lepsze rozwiązanie niż zastępowanie braków zwykłą średnią, ponieważ uwzględnia podobieństwo pacjentów.

"""