"""

🎨 MATPLOTLIB
Matplotlib to podstawowa biblioteka do tworzenia wykresów w Pythonie.
Najczęściej używany import:
import matplotlib.pyplot as plt

1️⃣ plt.plot() — wykres liniowy
Służy do pokazywania zmian wartości w czasie lub zależności między zmiennymi.
✅ Przykład
x = [1,2,3,4]y = [10,20,15,30]plt.plot(x, y)plt.show()

🎯 Najważniejsze parametry
plt.plot(    x,    y,    color='red',       # kolor linii    linestyle='--',    # styl linii    linewidth=3,       # grubość    marker='o',        # znaczniki punktów    label='Dane'       # legenda)

2️⃣ plt.scatter() — wykres punktowy
Pokazuje zależność między dwiema zmiennymi.
✅ Przykład
plt.scatter(df['Age'], df['Salary'])plt.xlabel('Wiek')plt.ylabel('Pensja')plt.show()

📌 Zastosowanie


korelacje


outliery


grupy danych



3️⃣ plt.bar() — wykres słupkowy
Porównywanie kategorii.
✅ Przykład
categories = ['A', 'B', 'C']values = [10, 25, 15]plt.bar(categories, values)plt.show()

4️⃣ plt.hist() — histogram
Pokazuje rozkład danych.
✅ Przykład
plt.hist(df['Salary'], bins=20)plt.show()

📌 bins
Liczba przedziałów histogramu.

5️⃣ plt.boxplot() — boxplot
Pokazuje:


medianę


kwartyle


outliery


✅ Przykład
plt.boxplot(df['Salary'])plt.show()

6️⃣ plt.pie() — wykres kołowy
✅ Przykład
sizes = [40, 35, 25]labels = ['Python', 'SQL', 'Excel']plt.pie(sizes, labels=labels)plt.show()

7️⃣ plt.figure() — tworzenie figury
✅ Przykład
plt.figure(figsize=(10,6))

8️⃣ plt.subplots() — wiele wykresów
✅ Przykład
fig, axes = plt.subplots(1,2)axes[0].plot(x,y)axes[1].hist(y)

9️⃣ Opisy wykresu
✅ Tytuł
plt.title('Mój wykres')
✅ Oś X
plt.xlabel('Wiek')
✅ Oś Y
plt.ylabel('Pensja')

🔟 plt.legend() — legenda
✅ Przykład
plt.plot(x,y,label='Dane')plt.legend()

1️⃣1️⃣ plt.show()
Wyświetla wykres.
plt.show()


🌊 SEABORN
Seaborn bazuje na matplotlib, ale:


ma ładniejsze style


mniej kodu


lepsze wykresy statystyczne


Import:
import seaborn as sns

1️⃣ sns.histplot()
Histogram.
✅ Przykład
sns.histplot(df['Salary'], bins=20)plt.show()

KDE
sns.histplot(df['Salary'], kde=True)

2️⃣ sns.kdeplot()
Wygładzony rozkład danych.
✅ Przykład
sns.kdeplot(df['Salary'], fill=True)plt.show()

3️⃣ sns.scatterplot()
Wykres punktowy.
✅ Przykład
sns.scatterplot(    x='Age',    y='Salary',    data=df)plt.show()

4️⃣ sns.lineplot()
Wykres liniowy.
✅ Przykład
sns.lineplot(    x='Year',    y='Revenue',    data=df)plt.show()

5️⃣ sns.barplot()
Średnie wartości dla kategorii.
✅ Przykład
sns.barplot(    x='Department',    y='Salary',    data=df)plt.show()

6️⃣ sns.boxplot()
Boxplot.
✅ Przykład
sns.boxplot(    x='Sex',    y='Salary',    data=df)plt.show()

7️⃣ sns.violinplot()
Połączenie:


boxplota


KDE


✅ Przykład
sns.violinplot(    x='Sex',    y='Salary',    data=df)plt.show()

8️⃣ sns.countplot()
Liczenie kategorii.
✅ Przykład
sns.countplot(    x='Department',    data=df)plt.show()

9️⃣ sns.heatmap()
Mapa ciepła.
✅ Przykład
corr = df.corr(numeric_only=True)sns.heatmap(corr)plt.show()

📌 Bardzo często używane do korelacji
sns.heatmap(corr, annot=True)
annot=True
→ pokazuje liczby.

🔟 sns.pairplot()
Macierz relacji między zmiennymi.
✅ Przykład
sns.pairplot(df.select_dtypes(float))

1️⃣1️⃣ sns.jointplot()
Histogram + scatterplot razem.
✅ Przykład
sns.jointplot(    x='Age',    y='Salary',    data=df)

1️⃣2️⃣ sns.regplot()
Scatterplot + linia regresji.
✅ Przykład
sns.regplot(    x='Age',    y='Salary',    data=df)

🎨 Style seaborn
✅ Styl siatki
sns.set_style('whitegrid')

🎨 Palette
sns.set_palette('Set2')

📌 Najważniejsze różnice
MatplotlibSeabornbardziej technicznybardziej „data science”większa kontrolamniej kodusurowe wykresyładne styledobry do customizacjidobry do analizy danych

🎯 Co najczęściej używa się w praktyce?
Matplotlib


custom wykresy


dokładna kontrola


Seaborn


analiza danych


szybkie dashboardy


EDA (exploratory data analysis)

"""