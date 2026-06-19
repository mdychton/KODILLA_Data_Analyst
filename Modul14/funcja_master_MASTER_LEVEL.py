"""1. PIPELINE + TRAINING + SAVE MODEL"""

import joblib  # zapis modeli
import pandas as pd  # dane
from sklearn.pipeline import Pipeline  # pipeline ML
from sklearn.preprocessing import StandardScaler  # skalowanie
from sklearn.linear_model import LogisticRegression  # model
from sklearn.model_selection import train_test_split  # split danych

class Trainer:

    def __init__(self):
        self.model = None

    def build_pipeline(self):

        # pipeline: preprocessing + model
        pipe = Pipeline([
            ("scaler", StandardScaler()),  # normalizacja
            ("model", LogisticRegression(max_iter=1000))  # model
        ])

        return pipe

    def train(self, X, y):

        # split danych
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # pipeline
        self.model = self.build_pipeline()

        # trening
        self.model.fit(X_train, y_train)

        return self.model, X_test, y_test

    def save_model(self, path="artifacts/model.pkl"):

        # zapis modelu do pliku
        joblib.dump(self.model, path)


"""2. EVALUATOR (PRODUCTION VERSION)"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve

class Evaluator:

    def __init__(self):
        self.logs = []

    def evaluate(self, model, X, y, model_name="model"):

        # predykcje
        y_pred = model.predict(X)
        y_proba = model.predict_proba(X)[:, 1]

        # raport
        print(classification_report(y, y_pred))

        # AUC
        auc = roc_auc_score(y, y_proba)
        print("AUC:", auc)

        # confusion matrix
        plt.figure()
        sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt="d", cmap="Blues")
        plt.title(model_name)
        plt.show()

        # logi
        self.logs.append({
            "model": model_name,
            "auc": auc
        })

        return self.logs
    

"""3. API (FASTAPI - DEPLOYMENT)"""

from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# wczytanie modelu
model = joblib.load("artifacts/model.pkl")

# endpoint health check
@app.get("/")
def home():
    return {"status": "ML API running"}

# endpoint predykcji
@app.post("/predict")
def predict(data: dict):

    # konwersja inputu do DataFrame
    df = pd.DataFrame([data])

    # predykcja
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }

"""4. LOGGING PREDYKCJI (MONITORING)"""

import pandas as pd
from datetime import datetime

class Logger:

    def __init__(self, path="logs/predictions.csv"):
        self.path = path

    def log(self, input_data, prediction, probability):

        row = {
            "time": datetime.now(),
            "input": str(input_data),
            "prediction": prediction,
            "probability": probability
        }

        df = pd.DataFrame([row])

        # dopisanie do pliku
        df.to_csv(self.path, mode='a', header=False, index=False)

"""5. FULL FLOW (JAK TO DZIAŁA W PRAWDZIWYM SYSTEMIE)"""   


# 1. trening
trainer = Trainer()
model, X_test, y_test = trainer.train(X, y)

# 2. zapis modelu
trainer.save_model()

# 3. ewaluacja
evaluator = Evaluator()
evaluator.evaluate(model, X_test, y_test)

# 4. API działa osobno (FastAPI)
# 5. logging działa w produkcji (Logger)


"""
CO TO JEST MASTER LEVEL?

To już nie jest „notebook ML”.

To jest:

🔥 REAL ML SYSTEM (jak w firmie)
komponent	poziom
pipeline	production-safe
evaluation	full metrics
API	deployment
logging	monitoring
joblib	model persistence
separation of concerns	YES
🚀 CO UMIESZ PO TYM POZIOMIE?

✔ budować modele
✔ trenować ML pipeline
✔ robić API do ML
✔ wdrażać model jak backend service
✔ monitorować predykcje
✔ rozumiesz cały lifecycle ML
"""