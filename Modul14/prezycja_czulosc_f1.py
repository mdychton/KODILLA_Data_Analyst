from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score  # import metryk oceny modelu klasyfikacyjnego

print('Accuracy: ', accuracy_score(y_test, predictions_lr))  # obliczenie i wyświetlenie dokładności modelu

print("Precision:", precision_score(y_test, predictions_lr))  # obliczenie i wyświetlenie precyzji modelu

print("Recall:", recall_score(y_test, predictions_lr))  # obliczenie i wyświetlenie czułości (Recall)

print("F1_score:", f1_score(y_test, predictions_lr))  # obliczenie i wyświetlenie miary F1


"""
Co robi ten kod?

Po wytrenowaniu modelu i wygenerowaniu predykcji:

predictions_lr = model_lr.predict(X_test_standardized)

chcemy ocenić:

Jak dobrze model przewiduje cukrzycę?

Do tego służą metryki klasyfikacyjne.

1. Accuracy (dokładność)

Obliczana przez:

accuracy_score(y_test, predictions_lr)

Wzór:

Accuracy=
TP+TN+FP+FN
TP+TN
	​


czyli:

Jaki procent wszystkich przewidywań był poprawny?

Przykład:

Rzeczywista	Predykcja
0	0
1	1
0	0
1	0

3 z 4 odpowiedzi są poprawne.

Accuracy = 75%
2. Precision (precyzja)

Wzór:

Precision=
TP+FP
TP
	​


Pokazuje:

Jeśli model powiedział "cukrzyca", jak często miał rację?

Przykład:

Model wskazał 100 osób jako chore.

80 rzeczywiście chorych
20 zdrowych

Wtedy:

Precision=
100
80
	​

=0.8

czyli:

Precision = 80%
3. Recall (czułość)

Wzór:

Recall=
TP+FN
TP
	​


Pokazuje:

Jaki procent wszystkich chorych osób został wykryty?

Przykład:

Mamy 100 chorych pacjentów.

Model wykrył:

90 osób

a przeoczył:

10 osób

Wtedy:

Recall=
100
90
	​

=0.9

czyli:

Recall = 90%
4. F1-score

Wzór:

F1=2⋅
Precision+Recall
Precision⋅Recall
	​


Jest to średnia harmoniczna Precision i Recall.

Pokazuje:

Jak dobrze model równoważy precyzję i czułość.

Przykład:

Precision = 0.80
Recall = 0.90

to:

F1≈0.85
Związek z macierzą pomyłek

Przypomnijmy układ macierzy:

	Pred 0	Pred 1
Actual 0	TN	FP
Actual 1	FN	TP

Na jej podstawie liczone są wszystkie metryki:

Accuracy → wykorzystuje TN, TP, FP, FN
Precision → wykorzystuje TP i FP
Recall → wykorzystuje TP i FN
F1-score → wykorzystuje Precision i Recall
Która metryka jest najważniejsza przy wykrywaniu cukrzycy?

Zwykle bardzo ważny jest Recall.

Dlaczego?

Jeżeli model uzna chorego pacjenta za zdrowego:

Actual = 1
Predicted = 0

powstaje:

False Negative (FN)

czyli przypadek przeoczenia choroby.

W zastosowaniach medycznych często bardziej zależy nam na wysokim Recall niż na maksymalnym Accuracy.

Jak interpretować wyniki?

Przykładowo:

Accuracy:  0.86
Precision: 0.82
Recall:    0.79
F1_score: 0.80

oznacza:

model poprawnie klasyfikuje 86% wszystkich pacjentów,
gdy przewiduje cukrzycę, ma rację w 82% przypadków,
wykrywa 79% wszystkich chorych osób,
ogólna równowaga między Precision i Recall wynosi 80%.
Krótka ściąga
Metryka	Pytanie, na które odpowiada
Accuracy	Jak często model ma rację?
Precision	Jak często przewidziana cukrzyca jest prawdziwa?
Recall	Jaki procent chorych został wykryty?
F1-score	Jak dobrze model równoważy Precision i Recall?

W problemach medycznych (takich jak wykrywanie cukrzycy) zwykle największą uwagę zwraca się na Recall i F1-score, ponieważ samo wysokie Accuracy może ukrywać dużą liczbę niewykrytych przypadków choroby.


"""