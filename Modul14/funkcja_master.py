metrics_dataframe = pd.DataFrame(columns=['Model', 'F1_score', 'AUC'])  
# tworzenie pustej tabeli (DataFrame) do zapisywania wyników modeli

metrics_dataframe  # wyświetlenie pustej tabeli

models = []  # lista do przechowywania wytrenowanych modeli
models_names = []  # lista nazw modeli
predictions_proba_list = []  # lista prawdopodobieństw dla klasy 1 (cukrzyca)

def calculate_metrics(model, name, X_checked, y_checked):  # funkcja do oceny modelu

    models.append(model)  # zapisanie modelu do listy
    models_names.append(name)  # zapisanie jego nazwy

    global metrics_dataframe  # użycie globalnej tabeli wyników

    predictions = model.predict(X_checked)  # predykcja klas (0/1)
    predictions_proba = model.predict_proba(X_checked)  # predykcja prawdopodobieństw
    predictions_proba_list.append(predictions_proba[:,1])  # zapis tylko P(klasa=1)

    ############## metryki dla sprawdzanego modelu ################

    print(classification_report(y_checked, predictions))  
    # raport: precision, recall, f1-score, accuracy dla obu klas

    # Confusion matrix
    plt.figure()  # nowy wykres
    cm = confusion_matrix(y_checked, predictions)  # macierz pomyłek
    ax = sns.heatmap(cm, annot=True, cmap='Blues', fmt='.0f')  # wizualizacja macierzy
    ax.set_title('Confusion Matrix\n\n')  # tytuł wykresu
    ax.set_xlabel('\nPredicted Values')  # opis osi X
    ax.set_ylabel('Actual Values ')  # opis osi Y
    plt.show()  # pokazanie wykresu

    # plot ROC curve
    fig = plt.figure(figsize=(6, 6))  # ustawienie rozmiaru wykresu
    plt.plot([0, 1], [0, 1], 'k--')  # linia modelu losowego

    for model_selected, name_selected, pred_proba in zip(models, models_names, predictions_proba_list):
        # przejście przez wszystkie zapisane modele

        fpr, tpr, thresholds = roc_curve(y_checked, pred_proba)  
        # obliczenie ROC dla danego modelu

        plt.plot(fpr, tpr, label=name_selected)  
        # dodanie krzywej ROC do wykresu

    plt.xlabel('False Positive Rate')  # opis osi X
    plt.ylabel('True Positive Rate')  # opis osi Y
    plt.title('ROC Curve')  # tytuł wykresu
    plt.legend(loc='lower right')  # legenda
    plt.show()  # pokazanie wykresu

    f1_metric = f1_score(y_checked, predictions)  
    # obliczenie F1-score

    auc_metric = roc_auc_score(y_checked, predictions_proba[:,1])  
    # obliczenie AUC (pole pod krzywą ROC)

    metrics_dataframe = metrics_dataframe.append(
        {'Model': name, 'F1_score': f1_metric, 'AUC': auc_metric},
        ignore_index=True
    )
    # dodanie wyników modelu do tabeli

    return metrics_dataframe  # zwrócenie tabeli z wynikami



"""
Co robi ten kod?

To jest uniwersalna funkcja do porównywania modeli ML.

📌 1. Co ta funkcja robi dla jednego modelu?

Dla modelu np.:

model_lr

robi wszystko naraz:

✔ predykcje:
predict() → klasy (0/1)
predict_proba() → prawdopodobieństwa
✔ metryki:
precision
recall
f1-score
accuracy
AUC
✔ wizualizacje:
confusion matrix
ROC curve
📊 2. Co robi ROC w pętli?
for model_selected, name_selected, pred_proba in zip(...)

To oznacza:

rysuj ROC dla wszystkich modeli, które już zostały dodane

Czyli możesz porównać np.:

Logistic Regression
Random Forest
KNN

na jednym wykresie.

📦 3. Co zapisuje metrics_dataframe?

Na końcu dostajesz tabelę:

Model	F1_score	AUC
LR	0.82	0.88
KNN	0.79	0.85
⚠️ WAŻNA UWAGA (bardzo istotna)

Ten fragment:

metrics_dataframe = metrics_dataframe.append(...)

👉 jest przestarzały w pandas (deprecated)

W nowych wersjach powinno być:

metrics_dataframe = pd.concat([
    metrics_dataframe,
    pd.DataFrame([{'Model': name, 'F1_score': f1_metric, 'AUC': auc_metric}])
], ignore_index=True)
🧠 4. Jak myśleć o tej funkcji?

To jest w praktyce:

🔁 pipeline do automatycznej oceny modeli ML

Jedno wywołanie:

calculate_metrics(model_lr, "Logistic Regression", X_test, y_test)

robi:

test modelu
raport klasyfikacji
confusion matrix
ROC curve
zapis wyników
🧪 5. Co jest tu ważne koncepcyjnie?
✔ 1. oddzielasz:
training
evaluation
✔ 2. używasz wielu metryk (nie tylko accuracy)
✔ 3. porównujesz modele w jednym miejscu
🚀 6. Najważniejsza idea

Ten kod buduje mini-system:

„Benchmark modeli klasyfikacyjnych”

czyli:

trenujesz kilka modeli
wrzucasz je do funkcji
dostajesz:
wykresy
metryki
ranking modeli

"""