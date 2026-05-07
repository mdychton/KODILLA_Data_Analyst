"""
🔹 Dwa podejścia

Masz dwa style pracy:

1. Funkcyjne (prostsze)

👉 szybkie wykresy
👉 dobre na start

2. Obiektowe (bardziej profesjonalne)

👉 większa kontrola
👉 używane w realnych projektach

🔹 1. Podejście funkcyjne (najprostsze)
👉 Import
import matplotlib.pyplot as plt
import numpy as np
👉 Tworzenie danych
x = np.arange(11)   # [0,1,2,...,10]
y = x ** 2          # kwadraty

👉 Czyli:

x = oś X
y = oś Y
👉 Najprostszy wykres
plt.plot(x, y)
plt.show()

👉 Efekt: linia rosnąca (bo x²)

🔹 Personalizacja (czyli wygląd)
plt.plot(x, y, color='red')           # kolor
plt.plot(x, y-10, color='blue', ls='--')  # druga linia

plt.xlabel('oś X')   # podpis
plt.ylabel('oś Y')
plt.title('Mój wykres')
👉 Co tu się dzieje?
plot() → rysuje linię
color → kolor
ls (linestyle) → styl (np. przerywana)
xlabel() → podpis osi
🔹 Dodatkowe opcje
plt.grid()  # siatka

plt.axhline(y=50, linestyle='--')  # linia pozioma
plt.axvline(x=5, linestyle='--')   # linia pionowa

👉 To jest mega przydatne w analizie (np. próg, target)

🔹 Wiele wykresów (subplot)
plt.subplot(1,2,1)   # 1 wiersz, 2 kolumny, wykres 1
plt.plot(x,y)

plt.subplot(1,2,2)   # drugi wykres
plt.plot(y,x)

plt.show()

👉 Czyli:

robisz „siatkę”
każdy wykres osobno
🔹 Wykres punktowy (scatter)
rand_arr = np.random.randint(1,1000,2000).reshape(1000,2)

plt.scatter(rand_arr[:,0], rand_arr[:,1])
plt.show()

👉 Użycie:

analiza rozkładu
clustering
outliery
🔹 Kolorowanie punktów (ważne!)
cmap = np.empty(rand_arr.shape, dtype='object')
cmap[:] = 'blue'

cmap[rand_arr.min(axis=1) > 500] = 'red'

plt.scatter(rand_arr[:,0], rand_arr[:,1], c=cmap[:,0])

👉 Co tu się dzieje:

każdy punkt ma kolor
jeśli spełnia warunek → czerwony

👉 To jest bardzo realny use case w pracy

🔹 Rozmiar wykresu
plt.figure(figsize=(10,5))

👉 szerokość, wysokość

🔹 Wykres kołowy
pie_data = [30,20,20,40,10]
labels = ['A','B','C','D','E']

plt.pie(pie_data, labels=labels, autopct='%1.1f%%')
plt.show()

👉 autopct = procenty

🔹 Zaawansowane (fill, alpha)
plt.fill(x, y, color='red', alpha=0.5)

👉 alpha = przezroczystość
👉 używane gdy dużo elementów

🔹 2. Podejście obiektowe (ważniejsze w pracy)

👉 Tutaj tworzysz „obiekty wykresu”

👉 Start
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])

👉 To znaczy:

tworzysz „płótno”
dodajesz osie
👉 Wykres
axes.plot(x,y)

axes.set_xlabel('oś X')
axes.set_ylabel('oś Y')
axes.set_title('Tytuł')

👉 zamiast plt.* używasz axes.*

🔹 Wiele osi (ważne!)
fig = plt.figure()

axes1 = fig.add_axes([0,0,1,1])
axes2 = fig.add_axes([0.2,0.2,0.8,0.8])

👉 czyli:

jeden wykres na drugim
często używane w dashboardach
🔹 Subplots (najczęściej używane w praktyce)
fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[1].plot(y,x)

👉 bardzo popularne rozwiązanie

🔥 Najważniejsze rzeczy do zapamiętania

👉 1. plot() → linie
👉 2. scatter() → punkty
👉 3. figure() → rozmiar
👉 4. subplot() / subplots() → wiele wykresów
👉 5. axes → podejście profesjonalne

💡 Kiedy czego używać?
sytuacja	wykres
trend w czasie	plot
zależność	scatters
udział %	pie
wiele wykresów	subplots
🚀 Jak to się przyda Tobie (realnie)

W pracy analityka:
s
wykres sprzedaży w czasie → plot
zależność np. cena vs sprzedaż → scatter
dashboard → subplots
raport → Matplotlib / Plotly

"""