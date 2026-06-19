from sklearn.metrics import roc_curve  # funkcja do obliczenia punktów krzywej ROC (TPR i FPR)
from sklearn.metrics import roc_auc_score  # funkcja do obliczenia pola pod krzywą ROC (AUC)

# prognoza prawdopodobieństwa
predictions_probability_lr = model_lr.predict_proba(X_test_standardized)  
# zwraca prawdopodobieństwa dla każdej klasy (np. [P(0), P(1)])

# obliczenie FPR oraz TPR w zależności od punktu odcięcia
fpr, tpr, thresholds = roc_curve(y_test, predictions_probability_lr[:,1])  
# ROC liczony dla prawdopodobieństwa klasy 1 (cukrzyca)

# wizualizacja ROC Curve
fig = plt.figure(figsize=(6, 6))  # ustawienie rozmiaru wykresu

# rysowanie prostej dla modelu losowego
plt.plot([0, 1], [0, 1], 'k--')  
# linia odniesienia: model losowy (brak mocy predykcyjnej)

plt.plot(fpr, tpr)  
# właściwa krzywa ROC: zależność TPR od FPR

plt.xlabel('False Positive Rate')  # opis osi X (fałszywie pozytywne)
plt.ylabel('True Positive Rate')  # opis osi Y (prawdziwie pozytywne)
plt.title('ROC Curve')  # tytuł wykresu

plt.show()  # wyświetlenie wykresu

# obliczenie AUC
auc = roc_auc_score(y_test, predictions_probability_lr[:,1])  
# AUC = pole pod krzywą ROC (miara jakości modelu)

print('AUC: ' + str(auc))  # wyświetlenie wyniku AUC


"""
Co robi ten kod?

Ten fragment ocenia model w bardziej „zaawansowany” sposób niż accuracy czy F1-score.

1. Co to jest ROC Curve?

ROC = Receiver Operating Characteristic

Pokazuje zależność:

Oś	Znaczenie
TPR	True Positive Rate (czułość / recall)
FPR	False Positive Rate (fałszywe alarmy)
Jak to działa?

Model nie daje tylko:

0 lub 1

ale daje:

prawdopodobieństwo

np.:

Pacjent	P(cukrzyca)
A	0.10
B	0.80
C	0.55
2. predict_proba
predictions_probability_lr = model_lr.predict_proba(...)

Zwraca:

[ [P(0), P(1)],
  [P(0), P(1)],
  ... ]

np.:

[[0.9, 0.1],
 [0.2, 0.8],
 [0.4, 0.6]]

My bierzemy tylko:

[:,1]

czyli:

prawdopodobieństwo klasy 1 (cukrzyca)

3. ROC curve (fpr, tpr)
fpr, tpr, thresholds = roc_curve(...)

Model testuje wiele progów:

Próg	Co się dzieje
0.2	prawie wszyscy = cukrzyca
0.5	standard
0.8	tylko pewne przypadki

Dla każdego progu liczy:

TPR (Recall) = ile chorych wykryto
FPR = ile zdrowych błędnie uznano za chorych
4. Wykres ROC
plt.plot([0, 1], [0, 1], 'k--')

to linia losowego modelu:

im bardziej blisko tej linii → tym gorzej

Krzywa ROC:

idealny model → lewy górny róg
losowy model → przekątna
5. Co oznacza AUC?
auc = roc_auc_score(...)

AUC = Area Under Curve

czyli:

pole pod krzywą ROC

Interpretacja AUC:
AUC	Znaczenie
1.0	idealny model
0.9–1.0	bardzo dobry
0.8–0.9	dobry
0.7–0.8	średni
0.5	losowy model
6. Dlaczego ROC jest ważne?

Bo:

nie zależy od konkretnego progu (np. 0.5)
pokazuje ogólną jakość modelu
działa dobrze przy niezbalansowanych danych (np. medycyna)
7. Intuicja (najprościej)

ROC mówi:

czy model dobrze oddziela chorych od zdrowych, niezależnie od progu decyzji

8. Co chcesz zobaczyć na dobrym modelu?

✔ krzywa blisko lewego górnego rogu
✔ AUC bliskie 1.0

Podsumowanie

Ten kod:

bierze prawdopodobieństwa predykcji
testuje różne progi klasyfikacji
liczy TPR i FPR
rysuje ROC curve
oblicza AUC jako końcową miarę jakości modelu

"""