import plotly.offline as pyo
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# uruchamia tryb offline Plotly w Jupyterze (żeby wykresy działały bez internetu)
init_notebook_mode(connected=True)

import cufflinks as cf

# integracja cufflinks z plotly (łatwiejsze wykresy z pandas)
cf.go_offline()

import matplotlib.pyplot as plt
from plotly.subplots import make_subplots  # (tu nieużywane, ale do subplotów w plotly)

import pandas as pd


# -------------------- WCZYTANIE DANYCH --------------------

# wczytanie danych o miedzi (CSV → DataFrame)
miedz = pd.read_csv('ca_c_f_d.csv')
miedz.head()

# wczytanie danych o KGHM
kghm = pd.read_csv('kgh_d.csv')
kghm.head()


# -------------------- PRZYGOTOWANIE DANYCH --------------------

# konwersja kolumny Data z tekstu na datetime
# dzięki temu matplotlib rozumie oś czasu (lata, miesiące itd.)
miedz['Data'] = pd.to_datetime(miedz['Data'], errors='coerce')
kghm['Data'] = pd.to_datetime(kghm['Data'], errors='coerce')


# -------------------- ŁĄCZENIE TABEL --------------------

# łączenie danych po wspólnej kolumnie Data
# zostają tylko dni, które występują w obu zbiorach
tabela = pd.merge(
    kghm[['Data','Zamkniecie']],
    miedz[['Data','Zamkniecie']],
    on='Data',
)

# zmiana nazw kolumn na czytelniejsze
# zamiast Zamkniecie_Zamkniecie mamy KGHM i Miedź
tabela.columns = ['Data', 'KGHM', 'Miedź']


# -------------------- UKŁAD WYKRESÓW --------------------

# tworzymy 3 panele: 2 wykresy + tabela
fig, axes = plt.subplots(
    3, 1,                      # 3 wiersze, 1 kolumna (jeden pod drugim)
    figsize=(12, 10),         # rozmiar całej figury
    sharex=False,             # nie współdzielimy osi X (daty osobno)
    gridspec_kw={'height_ratios': [3, 3, 2]}  # tabela mniejsza niż wykresy
)

# styl "ggplot" (siatka i jasne tło)
plt.style.use('ggplot')


# -------------------- WYKRES 1: KGHM --------------------

axes[0].plot(kghm['Data'], kghm['Zamkniecie'], color='blue')
axes[0].set_title('KGHM')

# ustawienie tła wykresu
axes[0].set_facecolor('#d3d3d3')

# biała siatka (lepsza czytelność na szarym tle)
axes[0].grid(color='white')


# -------------------- WYKRES 2: MIEDŹ --------------------

axes[1].plot(miedz['Data'], miedz['Zamkniecie'], color='red')
axes[1].set_title('Miedź')

axes[1].set_facecolor('#d3d3d3')
axes[1].grid(color='white')


# -------------------- TABELA --------------------

# wyłączamy osie (bo tabela nie jest wykresem)
axes[2].axis('off')

# tło dla obszaru tabeli
axes[2].set_facecolor('#d3d3d3')

# bierzemy tylko 10 pierwszych wierszy (czytelność)
table_data = tabela.head(10).copy()

# usunięcie godziny z daty (zostaje tylko YYYY-MM-DD)
table_data['Data'] = pd.to_datetime(table_data['Data']).dt.strftime('%Y-%m-%d')


# tworzenie tabeli w matplotlib
table = axes[2].table(
    cellText=table_data.values,     # dane w komórkach
    colLabels=table_data.columns,   # nagłówki kolumn
    loc='center'                    # wyśrodkowanie tabeli
)

# ustawienia wyglądu tabeli
table.auto_set_font_size(False)  # wyłącz automatyczny font
table.set_fontsize(8)            # rozmiar tekstu
table.scale(1, 1.5)              # skalowanie tabeli (wysokość komórek)


# -------------------- STYLIZACJA KOMÓREK --------------------

for (row, col), cell in table.get_celld().items():

    # nagłówki (pierwszy wiersz tabeli)
    if row == 0:
        cell.set_facecolor('#9e9e9e')  # ciemniejszy szary
        cell.set_text_props(color='white', weight='bold')  # biały, pogrubiony tekst

    # dane (pozostałe wiersze)
    else:
        cell.set_facecolor('#d9d9d9')   # jaśniejszy szary
        cell.set_text_props(ha='left')  # wyrównanie do lewej

    # obramowanie komórek
    cell.set_edgecolor('white')


# -------------------- FINALIZACJA --------------------

plt.tight_layout()  # automatyczne dopasowanie odstępów
plt.show()          # wyświetlenie wszystkiego


💡 Najważniejsze rzeczy, które warto zapamiętać
merge() → łączy dane po dacie
head(10) → tylko podgląd danych
plt.subplots(3,1) → układ pionowy
sharex=False → brak wspólnej osi X
table() → tabela w matplotlib
dt.strftime() → usuwa godzinę z daty