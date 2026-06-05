# Importujemy model Elastic Net
# Elastic Net łączy regularyzację Lasso (L1) oraz Ridge (L2)
from sklearn.linear_model import ElasticNet

# Tworzymy Pipeline:
# 1. PolynomialFeatures - generuje cechy wielomianowe
# 2. ElasticNet - uczy model regresji z regularyzacją
polynomial_regression_pipeline = make_pipeline(
    PolynomialFeatures(),
    ElasticNet()
)

# Definiujemy siatkę hiperparametrów do przetestowania
params = {
    # Stopień wielomianu
    'polynomialfeatures__degree': [1, 2, 3, 4, 5],

    # Siła regularyzacji
    # Im większa wartość alpha, tym mocniej karane są duże współczynniki
    'elasticnet__alpha': [
        1e-5, 1e-4, 1e-3,
        1e-2, 1e-1,
        0.0, 1.0, 10.0, 100.0
    ],

    # Proporcja między regularyzacją L1 i L2
    # 0.0 = czysty Ridge
    # 1.0 = czysty Lasso
    # wartości pośrednie = Elastic Net
    'elasticnet__l1_ratio': np.arange(0, 1.1, 0.1)
}

# Tworzymy Grid Search
polynomial_regression_gridsearch = GridSearchCV(
    estimator=polynomial_regression_pipeline,
    param_grid=params,
    scoring='neg_mean_squared_error',
    cv=cv
)

# Uruchamiamy wyszukiwanie najlepszych parametrów
polynomial_regression_gridsearch.fit(X_train, y_train)

# Wyświetlamy najlepszą kombinację parametrów
print(
    "\nNajlepsze hiperparametry:",
    polynomial_regression_gridsearch.best_params_,
    "\n"
)

# Pobieramy najlepszy model znaleziony przez Grid Search
polynomial_regression_model = (
    polynomial_regression_gridsearch.best_estimator_
)

# Wykonujemy predykcję na zbiorze testowym
predictions = polynomial_regression_model.predict(X_test)

# Obliczamy błąd RMSE
print(
    f'RMSE: {np.sqrt(mean_squared_error(y_test, predictions))}'
)



"""
Co to jest Elastic Net?

Elastic Net jest połączeniem dwóch popularnych metod regularyzacji:

Ridge (L2)

Kara za duże współczynniki:

λ∑β
i
2
	​


Efekt:

zmniejsza współczynniki,
ogranicza overfitting,
nie usuwa cech z modelu.
Lasso (L1)

Kara za wartości bezwzględne współczynników:

λ∑∣β
i
	​

∣

Efekt:

zmniejsza współczynniki,
może wyzerować niektóre współczynniki,
automatycznie wybiera najważniejsze cechy.
Elastic Net

Łączy oba podejścia:

Loss=RSS+λ(l1_ratio⋅L1+(1−l1_ratio)⋅L2)

Dzięki temu:

ogranicza przeuczenie (overfitting),
radzi sobie z silnie skorelowanymi cechami,
może usuwać nieistotne cechy.
Parametr alpha
'elasticnet__alpha'

Określa siłę regularyzacji.

Małe wartości
alpha = 0.00001

Model jest bardzo podobny do zwykłej regresji liniowej.

Duże wartości
alpha = 100

Model jest silnie uproszczony.

Może wystąpić:

underfitting,
zbyt prosta krzywa.
Parametr l1_ratio
'elasticnet__l1_ratio'

Określa proporcję między Lasso i Ridge.

l1_ratio	Interpretacja
0.0	Ridge
0.1	10% Lasso + 90% Ridge
0.5	50% Lasso + 50% Ridge
0.9	90% Lasso + 10% Ridge
1.0	Lasso

Przykład:

alpha = 0.1
l1_ratio = 0.7

oznacza:

regularyzacja jest umiarkowana (alpha=0.1),
70% wpływu pochodzi z Lasso,
30% wpływu pochodzi z Ridge.
Ile modeli sprawdzi Grid Search?

Dla:

degree = 5 wartości
alpha = 9 wartości
l1_ratio = 11 wartości

liczba kombinacji:

5×9×11=495

Jeżeli:

cv = 5

to zostanie wytrenowanych:

495×5=2475

modeli.

Uwaga

W siatce parametrów masz:

'elasticnet__alpha': [..., 0.0, ...]

alpha=0 oznacza brak regularyzacji i często generuje ostrzeżenie:

ConvergenceWarning

W praktyce lepiej usunąć 0.0:

'elasticnet__alpha': [
    1e-5, 1e-4, 1e-3,
    1e-2, 1e-1,
    1.0, 10.0, 100.0
]

ponieważ zwykłą regresję liniową testowałeś już wcześniej.

"""