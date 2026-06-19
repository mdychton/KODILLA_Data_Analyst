from numpy import where      # funkcja do wyszukiwania elementów spełniających warunek
from numpy import meshgrid   # tworzenie siatki punktów na płaszczyźnie
from numpy import arange     # generowanie zakresu wartości z określonym krokiem
from numpy import hstack     # łączenie tablic poziomo

def plot_classification_surface(X_plot, y_plot, trained_model):

    plt.figure(figsize=(12, 7))  # utworzenie okna wykresu

    # określenie granic zbioru
    min1, max1 = X_plot[:, 0].min()-1, X_plot[:, 0].max()+1  # minimalna i maksymalna wartość pierwszej cechy
    min2, max2 = X_plot[:, 1].min()-1, X_plot[:, 1].max()+1  # minimalna i maksymalna wartość drugiej cechy

    # skalowanie dla obu osi
    x1grid = arange(min1, max1, 0.1)  # punkty na osi X
    x2grid = arange(min2, max2, 0.1)  # punkty na osi Y

    # utworzenie siatki punktów
    xx, yy = meshgrid(x1grid, x2grid)

    # przetworzenie siatki na długie wektory
    r1, r2 = xx.flatten(), yy.flatten()

    # zamiana na kolumny
    r1 = r1.reshape((len(r1), 1))
    r2 = r2.reshape((len(r2), 1))

    # połączenie współrzędnych w zbiór danych
    grid = hstack((r1, r2))

    # predykcja klasy dla każdego punktu siatki
    yhat = trained_model.predict(grid)

    # odtworzenie oryginalnego kształtu siatki
    zz = yhat.reshape(xx.shape)

    # pokolorowanie obszarów zgodnie z przewidywaną klasą
    plt.contourf(xx, yy, zz, cmap='Paired')

    # rysowanie punktów treningowych
    for class_value in range(2):

        # znalezienie indeksów obserwacji należących do danej klasy
        row_ix = where(y_plot == class_value)

        # narysowanie punktów tej klasy
        plt.scatter(
            X_plot[row_ix, 0],
            X_plot[row_ix, 1],
            cmap='Paired',
            alpha=0.3,
            label=class_value
        )

    # dodanie legendy
    plt.legend(loc='upper right')

    # wyświetlenie wykresu
    plt.show()


# wywołanie funkcji dla wytrenowanego modelu
plot_classification_surface(
    X_plot=X_train_standardized,
    y_plot=y_train,
    trained_model=model_lr
)