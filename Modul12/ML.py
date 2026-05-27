# import modeli klasyfikacyjnych z biblioteki sklearn

from sklearn.tree import DecisionTreeClassifier   # drzewo decyzyjne
from sklearn.svm import SVC                       # Support Vector Classifier (SVM)
from sklearn.neighbors import KNeighborsClassifier # k najbliższych sąsiadów


# =========================
# TWORZENIE MODELI
# =========================

# tworzymy obiekt modelu drzewa decyzyjnego
dt_clf = DecisionTreeClassifier()

# tworzymy model SVM
svc_clf = SVC()

# tworzymy model KNN
knn_clf = KNeighborsClassifier()


# =========================
# WCZYTANIE DANYCH
# =========================

# x -> cechy (features)
# y -> prawdziwe odpowiedzi / klasy (labels)
x, y = load_simple_classifier_dataset()


# =========================
# LISTA MODELI
# =========================

# wrzucamy wszystkie modele do jednej listy,
# żeby wykonać tę samą operację dla każdego modelu
klasyfikatory = [dt_clf, svc_clf, knn_clf]


# =========================
# PĘTLA UCZĄCA MODELE
# =========================

for clf in klasyfikatory:

    print("--------------")

    # =========================
    # UCZENIE MODELU
    # =========================

    print("fitting - training...")

    # model uczy się zależności pomiędzy x i y
    clf.fit(x, y)


    # =========================
    # PREDYKCJA
    # =========================

    print("predicting...")

    # model przewiduje klasy dla danych x
    y_pred = clf.predict(x)


    # =========================
    # PORÓWNANIE WYNIKÓW
    # =========================

    # prawdziwe wartości
    print("true values ", y[:10])

    # przewidziane przez model
    print("predicted   ", y_pred[:10])


    # =========================
    # OCENA MODELU
    # =========================

    print("scoring...")

    # score() dla klasyfikacji zwraca accuracy
    # czyli procent poprawnych odpowiedzi
    clf_score = clf.score(x, y)

    print("score = ", clf_score)



    """
    1. Import gotowych modeli
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

Tutaj importujesz:

model drzewa decyzyjnego,
model SVM,
model KNN.

To są gotowe implementacje algorytmów ML.

2. Tworzenie modelu
svc_clf = SVC()

To działa tak samo jak:

auto = Car()
pies = Dog()

Tworzysz obiekt modelu.

Na tym etapie model:

NIC jeszcze nie umie,
nie zna danych,
nie umie przewidywać.

Jest pusty.

3. Dane x i y

To jest najważniejsza część.

x → cechy (features)

To są dane wejściowe.

Np.:

wzrost	waga	wiek
180	80	25
165	55	19
y → prawidłowe odpowiedzi (labels)

To są poprawne klasy.

Np.:

osoba	sportowiec?
1	TAK
2	NIE

czyli:

y = [1, 0]
Co oznacza uczenie modelu?

To kluczowa rzecz.

4. fit(x, y) — UCZENIE
clf.fit(x, y)

Tutaj model dostaje:

dane wejściowe x
poprawne odpowiedzi y

i próbuje znaleźć zależności.

Model uczy się:
jeżeli:
- wzrost duży
- waga duża

to prawdopodobnie klasa = 1

czyli:

model sam odkrywa reguły.

Przykład prostego uczenia

Załóżmy:

x = [
 [180, 80],
 [160, 50],
 [190, 90]
]

y = [1, 0, 1]

Model widzi:

wzrost	waga	wynik
180	80	1
160	50	0
190	90	1

I zaczyna zauważać:

duży wzrost + duża waga => częściej 1

To właśnie jest uczenie.

5. predict(x) — PREDYKCJA

Po nauczeniu model potrafi zgadywać.

y_pred = clf.predict(x)

Model dostaje dane i mówi:

myślę że:
- pierwszy rekord = 0
- drugi rekord = 1
- trzeci rekord = 1
6. Skąd biorą się TRUE VALUES?

To są właśnie prawdziwe odpowiedzi z y.

Czyli:

print(y[:10])

pokazuje:

[0 0 0 0 0 1 1 0 0 0]

To są poprawne klasy zapisane w dataset.

Czyli proces wygląda tak:
KROK 1

Dajemy modelowi dane:

x
KROK 2

Dajemy poprawne odpowiedzi:

y
KROK 3

Model uczy się relacji:

clf.fit(x, y)
KROK 4

Model próbuje zgadywać:

y_pred = clf.predict(x)
KROK 5

Porównujemy:

y_pred VS y
7. Co robi score()?
clf.score(x, y)

Dla klasyfikacji:

liczy accuracy.
Accuracy

To:

accuracy=
wszystkie odpowiedzi
poprawne odpowiedzi
	​

Przykład

Prawdziwe:

y = [0,1,1,0]

Przewidziane:

y_pred = [0,1,0,0]

Porównanie:

true	pred	dobrze?
0	0	✅
1	1	✅
1	0	❌
0	0	✅

3 poprawne z 4:

3/4=0.75

czyli:

score = 0.75
8. Jaki score jest dobry?

To zależy od problemu.

Ogólnie:

score	ocena
0.50	słabo
0.60-0.70	średnio
0.70-0.80	OK
0.80-0.90	dobrze
0.90+	bardzo dobrze
1.0	idealnie
ALE UWAGA — bardzo ważne
score = 1.0

NIE zawsze znaczy:

model jest świetny.

Bo można:

nauczyć model na danych,
a potem testować go na tych samych danych.

Wtedy model:

zapamiętuje odpowiedzi.

To trochę jak:

nauczyć się testu na pamięć

a nie:

naprawdę rozumieć materiał.

Dlatego w ML dzielimy dane:
train set

Do nauki.

test set

Do sprawdzania.

Przykład
x_train, x_test
y_train, y_test

Model:

uczy się na train,
sprawdzamy go na test.

To jest prawdziwa ocena jakości modelu.

Najprostsze podsumowanie
fit(x, y)
UCZ SIĘ
predict(x)
ZGADUJ
score(x, y)
SPRAWDŹ
ile zgadłeś poprawnie
    
    
    """