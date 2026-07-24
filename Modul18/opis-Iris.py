"""
1. Określenie rodzaju problemu
Chcemy przewidzieć gatunek kwiatu na podstawie jego wymiarów.
Zmienna wynikowa może przyjąć trzy wartości:
Setosa,
Versicolor,
Virginica.
Jest to więc klasyfikacja wieloklasowa, a nie klasyfikacja binarna.
Każdy kwiat należy dokładnie do jednej klasy.
2. Wczytanie danych
Zbiór Iris zawiera 150 obserwacji i pięć kolumn:
sepal.length – długość działki kielicha,
sepal.width – szerokość działki kielicha,
petal.length – długość płatka,
petal.width – szerokość płatka,
variety – gatunek kwiatu.
Pierwsze cztery kolumny są cechami wejściowymi, natomiast variety jest wartością, którą model ma przewidywać.
X = df[feature_columns]
y_text = df["variety"]
3. Wstępna kontrola danych
Przed budową modelu sprawdzamy:
df.shape
df.isnull().sum()
df["variety"].value_counts()
Chcemy się upewnić, że:
dane zostały poprawnie wczytane,
nie występują braki danych,
wszystkie gatunki mają odpowiednią liczbę przykładów.
W zbiorze Iris każda klasa ma po 50 obserwacji, więc dane są zbalansowane. Nie musimy stosować dodatkowego ważenia klas.
4. Zamiana nazw gatunków na liczby
Sieć neuronowa nie może bezpośrednio pracować z napisami takimi jak Setosa. Dlatego zamieniamy nazwy gatunków na liczby:
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y_text)
Otrzymujemy przykładowo:
Setosa      → 0
Versicolor  → 1
Virginica   → 2
Liczby nie oznaczają, że jedna klasa jest ważniejsza od drugiej. Są jedynie identyfikatorami klas.
5. Podział danych
Dane dzielimy na trzy części:
60% – zbiór treningowy,
20% – zbiór walidacyjny,
20% – zbiór testowy.
Zbiór treningowy
Służy do aktualizowania wag sieci neuronowej.
Zbiór walidacyjny
Pozwala obserwować zachowanie modelu podczas trenowania. Model nie aktualizuje wag na podstawie tych danych.
Zbiór testowy
Jest używany dopiero na końcu do niezależnej oceny modelu.
Podczas dzielenia stosujemy:
stratify=y
Dzięki temu w każdym zbiorze zachowane są podobne proporcje wszystkich trzech gatunków.
Ustawienie:
random_state=42
sprawia, że przy ponownym uruchomieniu otrzymamy taki sam podział danych.
6. Standaryzacja cech
Poszczególne cechy mają różne zakresy wartości. Dlatego wykonujemy standaryzację:
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)
Po standaryzacji wartości mają w przybliżeniu:
średnią równą 0,
odchylenie standardowe równe 1.
To zazwyczaj ułatwia i przyspiesza trenowanie sieci neuronowej.
Bardzo ważne jest to, że:
scaler.fit_transform(X_train)
wykonujemy wyłącznie na danych treningowych. Dla danych walidacyjnych i testowych używamy już tylko:
scaler.transform(...)
Zapobiega to przeciekowi informacji ze zbioru testowego do procesu trenowania.
7. Architektura sieci neuronowej
Model ma następującą budowę:
4 cechy wejściowe
       ↓
16 neuronów, ReLU
       ↓
8 neuronów, ReLU
       ↓
3 neurony, Softmax
Kod:
model = Sequential([
    Input(shape=(4,)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(3, activation="softmax")
])
Warstwa wejściowa
Input(shape=(4,))
Każdy kwiat jest opisany przez cztery cechy, dlatego sieć przyjmuje cztery wartości.
Pierwsza warstwa ukryta
Dense(16, activation="relu")
Ma 16 neuronów. Funkcja ReLU pozwala modelowi uczyć się nieliniowych zależności pomiędzy wymiarami kwiatu a jego gatunkiem.
Druga warstwa ukryta
Dense(8, activation="relu")
Przetwarza informacje znalezione przez poprzednią warstwę. Model jest celowo niewielki, ponieważ zbiór Iris ma tylko 150 obserwacji.
Warstwa wyjściowa
Dense(3, activation="softmax")
Potrzebujemy trzech neuronów, ponieważ mamy trzy gatunki.
Softmax zamienia wyniki sieci na prawdopodobieństwa, których suma wynosi 1.
Przykładowy wynik:
Setosa:      0.02
Versicolor:  0.91
Virginica:   0.07
Model wybierze klasę Versicolor, ponieważ otrzymała najwyższe prawdopodobieństwo.
8. Kompilacja modelu
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss=SparseCategoricalCrossentropy(from_logits=False),
    metrics=["accuracy"]
)
Optymalizator Adam
Adam odpowiada za aktualizowanie wag sieci tak, aby błąd stopniowo się zmniejszał.
Learning rate:
learning_rate=0.001
określa wielkość zmian wag wykonywanych podczas uczenia.
Funkcja straty
Używamy:
SparseCategoricalCrossentropy()
ponieważ:
mamy więcej niż dwie klasy,
klasy są zapisane jako liczby 0, 1, 2,
etykiety nie zostały zamienione na zapis one-hot.
Parametr:
from_logits=False
jest poprawny, ponieważ w ostatniej warstwie zastosowaliśmy Softmax. Model zwraca już prawdopodobieństwa, a nie surowe wyniki.
Metryka accuracy
metrics=["accuracy"]
Accuracy pokazuje, jaki procent przykładów został poprawnie sklasyfikowany.
9. Zabezpieczenie przed przeuczeniem
Zastosowaliśmy EarlyStopping:
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=15,
    restore_best_weights=True
)
Model obserwuje błąd na zbiorze walidacyjnym.
Jeśli val_loss nie poprawi się przez 15 kolejnych epok, trening zostanie zatrzymany.
restore_best_weights=True
przywraca wagi z najlepszej epoki, a nie z ostatniej.
10. Trenowanie modelu
history = model.fit(
    X_train_scaled,
    y_train,
    validation_data=(X_val_scaled, y_val),
    epochs=150,
    batch_size=16,
    callbacks=[early_stopping],
    verbose=1
)
Najważniejsze parametry:
epochs=150 – maksymalnie 150 pełnych przejść przez dane,
batch_size=16 – wagi są aktualizowane po przetworzeniu 16 przykładów,
validation_data – dane służące do kontrolowania jakości uczenia,
callbacks – uruchamia mechanizm wcześniejszego zatrzymania.
Model nie musi wykonać wszystkich 150 epok. EarlyStopping może zakończyć trening wcześniej.
11. Wykresy procesu uczenia
Notebook pokazuje:
stratę treningową i walidacyjną,
accuracy treningowe i walidacyjne.
Jeżeli obie wartości accuracy rosną, a błędy maleją, model prawidłowo się uczy.
O przeuczeniu mogłaby świadczyć sytuacja, w której:
train_accuracy nadal rośnie,
val_accuracy przestaje rosnąć,
val_loss zaczyna wyraźnie rosnąć.
12. Ocena na zbiorze testowym
test_loss, test_accuracy = model.evaluate(
    X_test_scaled,
    y_test
)
Dopiero tutaj sprawdzamy model na danych testowych.
To najważniejszy wynik, ponieważ zbiór testowy nie uczestniczył w trenowaniu ani wybieraniu najlepszej epoki.
13. Generowanie predykcji
Model zwraca prawdopodobieństwa:
y_probability = model.predict(X_test_scaled)
Przykładowo:
[0.01, 0.96, 0.03]
Następnie wybieramy indeks największego prawdopodobieństwa:
y_pred = np.argmax(y_probability, axis=1)
W tym przykładzie wynikiem będzie klasa 1, czyli Versicolor.
14. Raport klasyfikacji
Raport pokazuje dla każdego gatunku:
precision – jak często wskazanie danej klasy było poprawne,
recall – ile prawdziwych przykładów danej klasy model znalazł,
f1-score – połączenie precision i recall,
support – liczba przykładów danej klasy.
Dzięki temu widzimy więcej niż tylko ogólne accuracy.
15. Macierz pomyłek
Macierz pomyłek pokazuje:
prawdziwe klasy,
klasy przewidziane przez model,
miejsca, w których model się pomylił.
W zbiorze Iris Setosa jest zazwyczaj najłatwiejsza do rozpoznania. Ewentualne pomyłki częściej występują pomiędzy Versicolor i Virginica, ponieważ ich wymiary mogą być do siebie bardziej podobne.
Najważniejszy wniosek
Rozwiązanie spełnia wymagania zadania, ponieważ wykorzystuje sieć neuronową do klasyfikacji trzech gatunków, a ostatnia warstwa ma trzy neurony i funkcję Softmax.
Ze względu na mały zbiór danych wybraliśmy prostą sieć. Większy model miałby więcej parametrów, ale mógłby szybciej zapamiętać dane zamiast nauczyć się ogólnych zależności.


"""