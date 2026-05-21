import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych
miedz = pd.read_csv('ca_c_f_d.csv')
kghm = pd.read_csv('kgh_d.csv')

# Konwersja dat
miedz['Data'] = pd.to_datetime(miedz['Data'])
kghm['Data'] = pd.to_datetime(kghm['Data'])

# Styl wykresu
plt.style.use('ggplot')

# Tworzenie wykresów
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Szare tło dla całej figury
fig.patch.set_facecolor('lightgray')

# KGHM
axes[0].plot(kghm['Data'], kghm['Zamkniecie'])
axes[0].set_title('Ceny zamknięcia KGHM')
axes[0].set_ylabel('Cena')
axes[0].set_facecolor('#d3d3d3')   # szare tło
axes[0].grid(color='white')        # białe linie siatki

# Miedź
axes[1].plot(miedz['Data'], miedz['Zamkniecie'], color='red')
axes[1].set_title('Ceny zamknięcia miedzi')
axes[1].set_ylabel('Cena')
axes[1].set_xlabel('Data')
axes[1].set_facecolor('#d3d3d3')   # szare tło
axes[1].grid(color='white')        # białe linie siatki

plt.tight_layout()
plt.show()


"""
W tym fragmencie:

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

parametry (2, 1) oznaczają układ wykresów:

2 → liczba wierszy (rows)
1 → liczba kolumn (columns)

czyli:

[ wykres 1 ]
[ wykres 2 ]

Gdyby było:

plt.subplots(1, 2)

to wykresy byłyby obok siebie:

[ wykres 1 ] [ wykres 2 ]
Co oznacza sharex=True

To właśnie ten parametr powoduje, że oba wykresy mają wspólną oś X.

sharex=True

Dzięki temu:

lata (2015, 2016, itd.) są zsynchronizowane,
oba wykresy mają tę samą skalę czasu,
przesuwanie/zoom działa wspólnie,
dolny wykres pokazuje etykiety osi X, a górny ich nie powiela.
Skąd biorą się lata na osi X

Z tej części:

axes[0].plot(kghm['Data'], kghm['Zamkniecie'])

i

axes[1].plot(miedz['Data'], miedz['Zamkniecie'])

Ponieważ kolumna Data została wcześniej zamieniona na typ daty:

pd.to_datetime(...)

matplotlib automatycznie:

rozpoznaje daty,
wyświetla lata/miesiące,
ustawia skalę czasu.

"""