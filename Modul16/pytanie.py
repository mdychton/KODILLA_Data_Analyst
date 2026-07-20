"""
KMeans

Algorytm klasteryzacji dzielący dane na k klastrów poprzez iteracyjne wyznaczanie centroidów i przypisywanie do nich obserwacji na podstawie odległości.

K-Fold

Metoda walidacji modelu. Zbiór danych jest dzielony na k części, a model trenowany i oceniany wielokrotnie na różnych podziałach danych. Nie jest algorytmem uczenia maszynowego.

K Nearest Neighbors (KNN)

Algorytm klasyfikacji lub regresji. Przewiduje klasę nowej obserwacji na podstawie k najbliższych sąsiadów w zbiorze treningowym.

Pomimo podobnej nazwy, KMeans, K-Fold i KNN rozwiązują zupełnie różne problemy:

KMeans służy do klasteryzacji,
K-Fold do walidacji modeli,
KNN do klasyfikacji lub regresji.


Na rozmowie kwalifikacyjnej bardzo często pada pytanie:

Kiedy używać stratify?

Dobra odpowiedź:

Stratyfikację stosujemy w problemach klasyfikacyjnych, szczególnie gdy klasy są niezbalansowane. Pozwala ona zachować proporcje klas w zbiorze treningowym i testowym, dzięki czemu ocena modelu jest bardziej wiarygodna.

"""

