"""
1. Co oznacza, że KNN nie jest separatorem liniowym?

Separator liniowy to granica decyzyjna, którą można opisać prostą linią (w 2D), płaszczyzną (w 3D) lub hiperpłaszczyzną (w większej liczbie wymiarów).

Przykładowo regresja logistyczna tworzy granicę typu:

w
1
	​

x
1
	​

+w
2
	​

x
2
	​

+b=0

Na wykresie wyglądałoby to mniej więcej tak:

OOOOOOOO
OOOOOOOO
---------
XXXXXXXX
XXXXXXXX
XXXXXXXX

Granica jest prosta.

W KNN granica decyzyjna zależy od położenia punktów treningowych.

Przy małym k może wyglądać tak:

OOOOOOXXX
OOOOOXXXX
OOOXXXXXO
OOXXXXXXO
OXXXXXXOO
XXXXXXOOO

Granica jest poszarpana i zakrzywiona.

Jeżeli na Twoim wykresie widzisz nieregularne "wyspy", "zatoki" lub zygzaki pomiędzy kolorami klas, to właśnie oznacza, że model nie jest liniowy.

2. Skąd wiadomo, że model jest przeuczony?

Spójrz na parametr:

n_neighbors = int(X_train_standardized.shape[0] * 0.001)

Załóżmy:

1000 próbek

wtedy:

1000 * 0.001 = 1

czyli:

n_neighbors = 1

Masz model 1-NN.

Przy k=1 klasyfikacja działa tak:

"Sprawdź najbliższy punkt treningowy i przypisz jego klasę."

Model praktycznie zapamiętuje cały zbiór treningowy.

Na wykresie objawia się to tym, że wokół pojedynczych punktów powstają małe kolorowe "wysepki".

Przykład:

BBBBBBBBBBBB

BBBBBRBBBBBB
BBBBRRRBBBBB
BBBBBRBBBBBB

BBBBBBBBBBBB

Jeden czerwony punkt otoczony niebieskimi tworzy własny mały obszar klasy czerwonej.

To nie jest ogólna reguła w danych.

To jest:

"zapamiętałem ten konkretny punkt"

czyli overfitting.

3. Jak potwierdzić przeuczenie liczbowo?

Sam wykres nie zawsze wystarczy.

Najlepiej policzyć accuracy lub F1:

from sklearn.metrics import accuracy_score

y_train_pred = model_knn.predict(X_train_standardized)
y_test_pred = model_knn.predict(X_test_standardized)

print("Train:", accuracy_score(y_train, y_train_pred))
print("Test :", accuracy_score(y_test, y_test_pred))

Jeżeli dostaniesz np.

Train: 1.00
Test : 0.82

to jest klasyczny sygnał przeuczenia.

Model idealnie pamięta trening, ale gorzej działa na nowych danych.

4. Dlaczego KNN z małym k łatwo się przeucza?

Wyobraź sobie:

● = klasa A
× = klasa B

● ● ● ● ●

      ×

● ● ● ● ●

Ten pojedynczy × może być:

szumem,
błędem pomiaru,
nietypowym przypadkiem.

Przy k=1 model uzna:

"w tym miejscu istnieje obszar klasy ×"

i stworzy wokół niego osobną wyspę.

Przy większym k, np. 15:

KNeighborsClassifier(n_neighbors=15)

najbliżsi sąsiedzi będą głównie klasy ●, więc ta mała wyspa zniknie.

Granica stanie się gładsza.

5. Na co patrzeć na wykresie?

Jeżeli widzisz:

✅ gładkie, proste lub lekko zakrzywione granice → model raczej generalizuje.

Jeżeli widzisz:

❌ mnóstwo małych wysepek,
❌ bardzo poszarpane granice,
❌ obszary dopasowane do pojedynczych punktów,

to zwykle jest oznaka overfittingu.

W Twoim przypadku najbardziej podejrzane jest właśnie:

n_neighbors ≈ 1

Przy KNN jest to niemal podręcznikowy przykład przeuczenia. Jeśli pokażesz wykres wygenerowany pprzez plot_classification_surface(), mogę wskazać na konkretnych fragmentach, które elementy świadczą o nieliniowości i przeuczeniu.

"""