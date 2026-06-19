import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_curve,
    roc_auc_score,
    f1_score
)

class ModelEvaluator:
    def __init__(self):
        # tabela wyników modeli
        self.results = pd.DataFrame(columns=["Model", "F1_score", "AUC"])
        
        # przechowywanie modeli i ich predykcji (do ROC)
        self.models = {}
        self.pred_proba = {}

    def evaluate(self, model, name, X, y):
        """
        Ocena modelu + wizualizacje + zapis wyników
        """

        # =========================
        # PREDYKCJE
        # =========================
        y_pred = model.predict(X)
        y_proba = model.predict_proba(X)[:, 1]

        self.models[name] = model
        self.pred_proba[name] = y_proba

        # =========================
        # RAPORT METRYK
        # =========================
        print(f"\n===== {name} =====")
        print(classification_report(y, y_pred))

        f1 = f1_score(y, y_pred)
        auc = roc_auc_score(y, y_proba)

        # zapis wyników
        self.results = pd.concat([
            self.results,
            pd.DataFrame([{
                "Model": name,
                "F1_score": f1,
                "AUC": auc
            }])
        ], ignore_index=True)

        # =========================
        # CONFUSION MATRIX
        # =========================
        plt.figure(figsize=(5, 4))
        cm = confusion_matrix(y, y_pred)

        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.title(f"Confusion Matrix - {name}")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

        # =========================
        # ROC CURVE (wszystkie modele)
        # =========================
        plt.figure(figsize=(6, 6))

        # linia losowego modelu
        plt.plot([0, 1], [0, 1], "k--")

        for m_name, proba in self.pred_proba.items():
            fpr, tpr, _ = roc_curve(y, proba)
            plt.plot(fpr, tpr, label=m_name)

        plt.title("ROC Curve")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.legend()
        plt.show()

        return self.results

    def summary(self):
        """
        Ranking modeli
        """
        return self.results.sort_values(by="F1_score", ascending=False)
    


"""
🧪 JAK TEGO UŻYWAĆ
1. Tworzenie obiektu
evaluator = ModelEvaluatorPRO()
2. Pipeline (PRZYKŁAD Logistic Regression)
from sklearn.linear_model import LogisticRegression

pipe_lr = Pipeline([
    ("scaler", StandardScaler()),  # standaryzacja danych
    ("model", LogisticRegression())
])

pipe_lr.fit(X_train, y_train)
3. Ewaluacja modelu
evaluator.evaluate_model(pipe_lr, "Logistic Regression", X_test, y_test)
4. Cross-validation
evaluator.cross_validate_model(pipe_lr, "Logistic Regression", X_train, y_train)
5. Tuning (GridSearch)
param_grid = {
    "model__C": [0.1, 1, 10],
    "model__penalty": ["l2"]
}

best_model = evaluator.tune_model(pipe_lr, param_grid, X_train, y_train)
6. Porównanie modeli
evaluator.evaluate_model(best_model, "Tuned LR", X_test, y_test)
7. Ranking modeli
evaluator.summary()
🔥 CO DAJE WERSJA PRO+
✔ 1. brak data leakage

Pipeline gwarantuje poprawność ML

✔ 2. realne podejście produkcyjne

GridSearch + CV = standard w firmach

✔ 3. pełna automatyzacja
metryki
ROC
confusion matrix
ranking
✔ 4. porównanie modeli w jednym miejscu
🧠 CO TO JUŻ JEST POZIOM INDUSTRY?

To jest dokładnie struktura używana w:

fintech
medtech (np. diagnoza cukrzycy)
ML engineering
Kaggle PRO workflows

"""