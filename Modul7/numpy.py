"""
🔹 Tworzenie tablic (ndarray)
one_dim = np.array([1, 2, 3, 4])   # tworzy jednowymiarową tablicę (wektor)
my_nested_list = [[1,2,3],[4,5,6],[7,8,9]]
np.array(my_nested_list)   # tworzy tablicę 2D (macierz) z listy zagnieżdżonej
🔹 Właściwości tablic
one_dim.shape   # zwraca kształt tablicy (np. (4,) = 4 elementy w 1D)
one_dim.ndim   # zwraca liczbę wymiarów tablicy (1D, 2D, 3D...)
two_dim.size   # zwraca całkowitą liczbę elementów w tablicy
two_dim.itemsize   # zwraca rozmiar jednego elementu w bajtach
🔹 Zmiana kształtu (reshape)
one_dim_horizontal = np.array([[1,2,3,4]])   # tworzy macierz 1x4 (wiersz poziomy)
one_dim_vertical = one_dim_horizontal.reshape(-1, 1)   # zamienia na wektor pionowy (kolumna), -1 dopasowuje automatycznie
one_dim_vertical.reshape(1, -1)   # zamienia z powrotem na wektor poziomy
🔹 Spłaszczanie i transpozycja
two_dim.flatten()   # zamienia macierz na 1D (spłaszcza wszystkie elementy)
two_dim.T   # transpozycja – zamiana wierszy na kolumny
🔹 Generowanie danych
np.arange(0, 20, 2)   # liczby od 0 do 20 co 2 (jak range, ale NumPy)
np.zeros((5,3))   # tworzy macierz 5x3 wypełnioną zerami
np.ones((2,3), dtype=np.int8)   # tworzy macierz 2x3 wypełnioną jedynkami (typ int8)
np.linspace(0, 5, 10)   # 10 równych wartości między 0 a 5
🔹 Macierze specjalne
np.eye(4)   # macierz jednostkowa 4x4 (1 na przekątnej)
np.diag([5, 0, 4, 1])   # macierz diagonalna (wartości na przekątnej)
🔹 Losowe dane
np.random.rand(5)   # 5 losowych liczb z zakresu 0–1
np.random.rand(5,5)   # macierz 5x5 losowych liczb 0–1
np.random.randint(1, 100, 10)   # 10 losowych liczb całkowitych od 1 do 100
🔹 Typy danych
np.array([5, 10, 20.0])   # zamienia wszystko na float (bo występuje float)
np.array([5, 10, "20"])   # zamienia wszystko na string (jeden wspólny typ)



---

# 📌 2) Ultra ściąga A4 (NAJWAŻNIEJSZE)

## 🧠 NumPy – szybka ściąga

### 🔹 Tworzenie
- `np.array()` → tworzy tablicę  
- `np.zeros((a,b))` → tablica zer  
- `np.ones((a,b))` → tablica jedynek  
- `np.arange(start, stop, step)` → zakres liczb  
- `np.linspace(a,b,n)` → n równych punktów  

---

### 🔹 Wymiary
- `.shape` → rozmiar (wiersze, kolumny)  
- `.ndim` → liczba wymiarów  
- `.size` → liczba elementów  

---

### 🔹 Zmiana kształtu
- `.reshape(a,b)` → zmiana układu  
- `.flatten()` → spłaszczenie do 1D  
- `.T` → transpozycja  

---

### 🔹 Losowe
- `np.random.rand()` → 0–1 float  
- `np.random.randint()` → losowe int  

---

### 🔹 Kluczowe zasady
- NumPy = szybkie tablice (lepsze niż listy)
- wszystkie elementy muszą mieć TEN SAM typ
- reshape nie zmienia danych tylko układ
- używa się w analizie danych i ML

---

## 🚀 Jak to zapamiętać
👉 array = dane  
👉 shape = rozmiar  
👉 reshape = układ  
👉 random = testowe dane  
👉 T = obrót macierzy  

---

Jeśli chcesz, mogę Ci zrobić jeszcze:
👉 :contentReference[oaicite:0]{index=0}  
👉 albo :contentReference[oaicite:1]{index=1}



🧠 Najważniejsze zasady NumPy
1. ndarray = tablica wielowymiarowa
2. wszystkie elementy mają jeden typ
3. reshape zmienia tylko układ, nie dane
4. flatten = spłaszczenie do 1D
5. T = transpozycja (wiersze ↔ kolumny)
6. random = dane testowe i symulacje

"""