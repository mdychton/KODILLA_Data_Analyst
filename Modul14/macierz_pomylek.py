from sklearn.metrics import confusion_matrix  # import funkcji do tworzenia macierzy pomyłek

import seaborn as sns  # import biblioteki seaborn do tworzenia estetycznych wykresów

cm = confusion_matrix(y_test, predictions_lr)  # obliczenie macierzy pomyłek na podstawie wartości rzeczywistych i przewidzianych

ax = sns.heatmap(cm, annot=True, cmap='Blues', fmt='.0f')  # utworzenie mapy cieplnej przedstawiającej macierz pomyłek

ax.set_title('Confusion Matrix\n\n')  # ustawienie tytułu wykresu

ax.set_xlabel('\nPredicted Values')  # podpis osi X - wartości przewidziane przez model

ax.set_ylabel('Actual Values ')  # podpis osi Y - wartości rzeczywiste

plt.show()  # wyświetlenie wykresu


"""
Co robi ten kod?

Tworzy macierz pomyłek (Confusion Matrix), czyli jedną z najważniejszych metod oceny modelu klasyfikacyjnego.

Dla Twojego problemu:

0 = brak cukrzycy
1 = cukrzyca

macierz może wyglądać tak:

	Pred 0	Pred 1
Actual 0	1200	100
Actual 1	150	550
Jak powstaje macierz?

Funkcja:

confusion_matrix(y_test, predictions_lr)

porównuje:

y_test

czyli prawdziwe etykiety

z

predictions_lr

czyli przewidywaniami modelu.

Interpretacja pól macierzy

Standardowy układ:

	Predicted 0	Predicted 1
Actual 0	TN	FP
Actual 1	FN	TP

gdzie:

TN (True Negative)
Actual = 0
Predicted = 0

Pacjent zdrowy został poprawnie uznany za zdrowego.

FP (False Positive)
Actual = 0
Predicted = 1

Pacjent zdrowy został błędnie uznany za chorego.

FN (False Negative)
Actual = 1
Predicted = 0

Pacjent chory został błędnie uznany za zdrowego.

W medycynie jest to zwykle najgroźniejszy błąd.

TP (True Positive)
Actual = 1
Predicted = 1

Pacjent chory został poprawnie wykryty.

Przykład

Załóżmy wynik:

[[1200  100]
 [ 150  550]]

Oznacza:

Typ	Liczba
TN	1200
FP	100
FN	150
TP	550

Interpretacja:

1200 zdrowych wykryto poprawnie
100 zdrowych uznano za chorych
150 chorych przeoczono
550 chorych wykryto poprawnie
Co robi heatmap?

Ta linia:

sns.heatmap(cm, annot=True, cmap='Blues')

rysuje macierz jako kolorową tabelę.

Parametry:

annot=True

wyświetla liczby wewnątrz komórek.

cmap='Blues'

używa niebieskiej palety kolorów.

Im większa liczba:

ciemniejszy kolor
fmt='.0f'

wyświetla liczby całkowite bez miejsc po przecinku.

Jak ocenić model na podstawie macierzy?

Dobrze, gdy:

TN jest duże,
TP jest duże,
FP jest małe,
FN jest małe.

W problemie wykrywania cukrzycy szczególnie ważne jest:

FN (False Negative)

czyli liczba chorych osób, które model uznał za zdrowe.

Jeżeli FN jest wysokie, model może być niebezpieczny w praktyce, ponieważ przeocza osoby wymagające dalszej diagnostyki.

Dlaczego macierz pomyłek jest ważniejsza od samego Accuracy?

Załóżmy, że:

95% pacjentów jest zdrowych
5% pacjentów jest chorych

Model przewidujący zawsze:

0

osiągnie:

Accuracy = 95%

ale nie wykryje ani jednego chorego pacjenta.

Macierz pomyłek natychmiast pokaże ten problem, ponieważ:

TP = 0
FN = bardzo dużo

Dlatego macierz pomyłek jest podstawowym narzędziem do oceny modeli klasyfikacyjnych, szczególnie w zastosowaniach medycznych takich jak wykrywanie cukrzycy.

"""