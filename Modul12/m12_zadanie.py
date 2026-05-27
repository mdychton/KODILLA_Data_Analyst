# ==========================================
# IMPORT BIBLIOTEK
# ==========================================

# gotowe datasety ze sklearn
from sklearn.datasets import load_iris, load_wine

# funkcja do podziału danych
from sklearn.model_selection import train_test_split

# metryka accuracy
from sklearn.metrics import accuracy_score

# klasyfikatory
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


# ==========================================
# ŁADOWANIE DATASETÓW
# ==========================================

# dataset irysów
iris = load_iris()

# dataset win
wine = load_wine()

# słownik datasetów
# dzięki temu możemy przejść pętlą po wszystkich danych
datasets = {
    "Iris": iris,
    "Wine": wine
}


# ==========================================
# DEFINICJA KLASYFIKATORÓW
# ==========================================

# tworzymy kilka modeli do porównania
classifiers = {

    # drzewo decyzyjne
    "Decision Tree": DecisionTreeClassifier(),

    # K najbliższych sąsiadów
    "KNN": KNeighborsClassifier(),

    # Support Vector Machine
    "SVM": SVC()
}


# ==========================================
# TESTOWANIE MODELI
# ==========================================

# przechodzimy po każdym datasecie
for dataset_name, dataset in datasets.items():

    print("\n==============================")
    print("DATASET:", dataset_name)
    print("==============================")

    # X -> dane wejściowe (features)
    X = dataset.data

    # y -> prawdziwe etykiety / klasy
    y = dataset.target


    # ==========================================
    # PODZIAŁ DANYCH
    # ==========================================

    # 70% danych -> trening
    # 30% danych -> test

    # random_state=42 gwarantuje
    # zawsze taki sam podział danych

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )


    # ==========================================
    # TRENOWANIE KAŻDEGO MODELU
    # ==========================================

    # przechodzimy po wszystkich klasyfikatorach
    for clf_name, clf in classifiers.items():

        print("\nClassifier:", clf_name)

        # ==========================================
        # UCZENIE MODELU
        # ==========================================

        # model uczy się na danych treningowych
        clf.fit(X_train, y_train)


        # ==========================================
        # PREDYKCJA
        # ==========================================

        # przewidywanie dla danych testowych
        y_pred = clf.predict(X_test)


        # ==========================================
        # OCENA MODELU
        # ==========================================

        # accuracy dla treningu
        # jak dobrze model zapamiętał trening
        train_score = clf.score(X_train, y_train)

        # accuracy dla testu
        # jak dobrze model działa na nowych danych
        test_score = clf.score(X_test, y_test)

        print("Train score:", round(train_score, 2))
        print("Test score :", round(test_score, 2))


        # ==========================================
        # ANALIZA OVERFITTINGU
        # ==========================================

        # jeśli różnica między train i test
        # jest duża -> możliwy overfitting

        if train_score - test_score > 0.15:
            print("Possible overfitting")
        else:
            print("Model generalizes well")


"""
Jak interpretować wyniki

Przykład:

Train score: 1.0
Test score : 0.78
Possible overfitting

oznacza:

model nauczył się treningu idealnie,
ale gorzej działa na nowych danych,
więc prawdopodobnie overfittuje.
Co możesz napisać w raporcie
Opis danych
Do eksperymentu wykorzystano datasety Iris oraz Wine z biblioteki sklearn.datasets.
Dane zostały podzielone na:
- 70% treningowe
- 30% testowe

Podział wykonano przy pomocy train_test_split z random_state=42.
Użyte modele
Przetestowano następujące klasyfikatory:
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
Wnioski
Decision Tree osiągnął bardzo wysokie wyniki treningowe, jednak w niektórych przypadkach wynik testowy był niższy, co może świadczyć o overfittingu.

KNN osiągnął stabilne wyniki zarówno dla treningu jak i testu, dzięki czemu dobrze generalizował dane.

SVM osiągnął jedne z najlepszych wyników testowych i wykazał dobrą zdolność generalizacji.

"""