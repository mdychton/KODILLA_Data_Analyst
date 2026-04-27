"""
🚀 1. CSV — NOWOCZESNY STANDARD
📥 Wczytanie
import pandas as pd

df = pd.read_csv('myCsvFile.csv')
👀 podgląd danych
df.head()        # pierwsze 5 wierszy
df.tail()        # ostatnie 5
df.info()        # struktura danych
df.describe()    # statystyki
📤 Zapis
df.to_csv('myNewCsvFile.csv', index=False)
🧠 co robi index=False?

👉 usuwa kolumnę indeksu (zwykle niepotrzebna w Excel/CSV)

🚀 2. EXCEL — NOWOCZESNY STANDARD (POLECANY)
📥 Wczytanie
df = pd.read_excel('myExcelFile.xlsx', sheet_name='my_data')
👀 podgląd
df.head()
df.info()
df.describe()
📤 Zapis (NOWY STANDARD)
df.to_excel('myNewExcelFile.xlsx', sheet_name='my_new_data', index=False)

👉 to jest najprostsza i najczęściej używana metoda

🚀 3. WIELE SHEETÓW (NOWOCZESNIE)
⭐ BEST PRACTICE (bez save()!)
with pd.ExcelWriter('many_sheets.xlsx', engine='xlsxwriter') as writer:
    
    df.to_excel(writer, sheet_name='my_df1', index=False)
    df.to_excel(writer, sheet_name='my_df2', index=False)
🧠 co się dzieje?
otwierasz plik Excel
zapisujesz kilka arkuszy
Python automatycznie:
✔ zapisuje
✔ zamyka plik
✔ commituje dane
❌ STARE (NIE UŻYWAĆ)
writer = pd.ExcelWriter(...)
df.to_excel(writer)
writer.save()   ❌
🚀 4. PODGLĄD ZAPISANEGO EXCELA
📥 wczytanie
df1 = pd.read_excel('many_sheets.xlsx', sheet_name='my_df1')
df2 = pd.read_excel('many_sheets.xlsx', sheet_name='my_df2')
👀 szybki podgląd
df1.head()
df2.head()
🔍 sprawdzenie arkuszy
xls = pd.ExcelFile('many_sheets.xlsx')
xls.sheet_names
📦 wczytanie wszystkiego naraz
all_sheets = pd.read_excel('many_sheets.xlsx', sheet_name=None)
🧠 5. PEŁNY „WORKFLOW” (REAL PRACA)
import pandas as pd

# 1. Wczytanie danych
df = pd.read_csv('file.csv')

# 2. Podgląd
df.head()
df.info()

# 3. Czyszczenie / analiza
df = df.dropna()

# 4. Eksport do Excela (multi-sheet)
with pd.ExcelWriter('report.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='clean_data', index=False)
    df.describe().to_excel(writer, sheet_name='summary')
🔥 6. NAJWAŻNIEJSZE DO ZAPAMIĘTANIA
📌 CSV
read_csv / to_csv
📌 Excel (prosto)
read_excel / to_excel
📌 Excel (multi-sheet)
with ExcelWriter(...)
📌 podgląd danych
head()
info()
describe()
🚀 TL;DR

👉 nowoczesny pandas =

with ExcelWriter
head/info/describe
brak save()
index=False prawie zawsze


🚀 1. PEŁNY PRZYKŁAD: DATA + WYKRES + FORMATOWANIE
import pandas as pd

df = pd.DataFrame({
    'Month': ['Jan','Feb','Mar','Apr','May'],
    'Sales': [100, 150, 130, 180, 220]
})

with pd.ExcelWriter('report.xlsx', engine='xlsxwriter') as writer:
    
    # 📥 zapis danych
    df.to_excel(writer, sheet_name='data', index=False)
    
    workbook  = writer.book
    worksheet = writer.sheets['data']
🎨 2. FORMATOWANIE (nagłówki)
header_format = workbook.add_format({
    'bold': True,
    'bg_color': '#4F81BD',
    'font_color': 'white',
    'border': 1
})
📌 zastosowanie formatowania
for col_num, value in enumerate(df.columns):
    worksheet.write(0, col_num, value, header_format)

👉 zamienia nagłówki na „Excel-style report”

📏 3. SZEROKOŚĆ KOLUMN
worksheet.set_column('A:A', 12)
worksheet.set_column('B:B', 10)

👉 A = Month
👉 B = Sales

📊 4. FORMAT LICZB (np. waluta)
money_format = workbook.add_format({
    'num_format': '#,##0 €'
})
zastosowanie:
worksheet.set_column('B:B', 10, money_format)
📈 5. WYKRES (LINE)
chart = workbook.add_chart({'type': 'line'})
dane do wykresu
chart.add_series({
    'name': 'Sales',
    'categories': ['data', 1, 0, 5, 0],
    'values':     ['data', 1, 1, 5, 1],
})
opis wykresu
chart.set_title({'name': 'Monthly Sales'})
chart.set_x_axis({'name': 'Month'})
chart.set_y_axis({'name': 'Revenue'})
chart.set_legend({'none': True})
wstawienie wykresu
worksheet.insert_chart('D2', chart)

=================================== gotowy raport ===============================
🚀 6. CAŁOŚĆ (PRO RAPORT)
import pandas as pd

df = pd.DataFrame({
    'Month': ['Jan','Feb','Mar','Apr','May'],
    'Sales': [100, 150, 130, 180, 220]
})

with pd.ExcelWriter('report.xlsx', engine='xlsxwriter') as writer:
    
    df.to_excel(writer, sheet_name='data', index=False)
    
    workbook  = writer.book
    worksheet = writer.sheets['data']
    
    # 🎨 nagłówki
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#4F81BD',
        'font_color': 'white',
        'border': 1
    })
    
    for col_num, value in enumerate(df.columns):
        worksheet.write(0, col_num, value, header_format)
    
    # 📏 szerokość kolumn
    worksheet.set_column('A:A', 12)
    worksheet.set_column('B:B', 12)
    
    # 📊 wykres
    chart = workbook.add_chart({'type': 'line'})
    
    chart.add_series({
        'name': 'Sales',
        'categories': ['data', 1, 0, 5, 0],
        'values':     ['data', 1, 1, 5, 1],
    })
    
    chart.set_title({'name': 'Monthly Sales'})
    chart.set_x_axis({'name': 'Month'})
    chart.set_y_axis({'name': 'Sales'})
    chart.set_legend({'none': True})
    
    worksheet.insert_chart('D2', chart)
🧠 7. CO TU SIĘ NAUCZYŁEŚ
🔹 formatowanie
workbook.add_format()
worksheet.write()
🔹 układ raportu
data + header format + chart + layout
🔹 Excel = mini BI tool
Python → dane → Excel → raport dla ludzi
🔥 TL;DR

👉 Excel raport = 4 rzeczy:

1. dane
2. format nagłówków
3. szerokości kolumn
4. wykres






"""