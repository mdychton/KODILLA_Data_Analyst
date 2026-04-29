"""
🔹 Co to są accessory .dt i .str?

👉 Accessory = „specjalny sposób dostępu do metod dla konkretnego typu danych”

Accessor	Do czego służy
.dt	daty (datetime)
.str	tekst (string)
🟦 .dt – praca z datami
🔹 Najpierw musisz mieć datetime
# konwersja kolumny na datę
df['Data'] = pd.to_datetime(df['Data'])

👉 bez tego .dt nie zadziała

🔹 Dzień tygodnia
# nazwa dnia tygodnia (np. Monday, Tuesday)
df['Data'].dt.day_name()
🔹 Miesiąc
# nazwa miesiąca (January, February...)
df['Data'].dt.month_name()
🔹 Czy początek miesiąca?
# True jeśli pierwszy dzień miesiąca
df['Data'].dt.is_month_start
🔹 Filtrowanie (bardzo ważne!)
# tylko transakcje z czwartku
df[df['Data'].dt.day_name() == 'Thursday']
🔥 Najczęściej używane .dt
day, month, year
hour, minute, second
day_name, month_name
is_month_start
is_month_end
is_year_start
🟩 .str – praca z tekstem

👉 działa tylko na kolumnach tekstowych

🔹 Wielkie litery
df['Produkt'].str.upper()
🔹 Małe litery
df['Produkt'].str.lower()
🔹 Czy tekst kończy się na coś?
# True/False
df['Region'].str.endswith('ód')
🔹 Czy zawiera tekst?
# filtrujemy wiersze
df[df['Region'].str.contains('Zachód')]
🔹 Czy zaczyna się od czegoś?
df['Produkt'].str.startswith('Lap')
🔹 Czyszczenie tekstu
df['Produkt'].str.strip()   # usuwa spacje
🔥 Najczęstsze .str
upper()
lower()
strip()
contains()
startswith()
endswith()
len()
replace()
🔴 WAŻNA ZASADA

👉 .str i .dt NIE działają na całym DataFrame
👉 tylko na Series (kolumna)

================Zadania================

🟢 Zadanie 1 – Dzień tygodnia

👉 Dodaj kolumnę Dzien_tygodnia

# upewniamy się, że kolumna Data ma format datetime
df['Data'] = pd.to_datetime(df['Data'])

# .dt.day_name() zwraca nazwę dnia tygodnia
df['Dzien_tygodnia'] = df['Data'].dt.day_name()
🟢 Zadanie 2 – filtr: tylko Monday
# filtrujemy wiersze gdzie dzień tygodnia to Monday
df_monday = df[df['Data'].dt.day_name() == 'Monday']
🟡 Zadanie 3 – tekst upper
# .str.upper() zamienia tekst na wielkie litery
df['Produkt_upper'] = df['Produkt'].str.upper()
🟡 Zadanie 4 – filtr tekstowy (Region zawiera "East")
# .str.contains() sprawdza czy tekst zawiera dany fragment
df_east = df[df['Region'].str.contains('East', na=False)]

👉 na=False zabezpiecza przed błędami jeśli są NaN

🔴 Zadanie 5 – weekend + sprzedaż > 1000
# tworzymy kolumnę dzień tygodnia
df['Dzien_tygodnia'] = df['Data'].dt.day_name()

# filtr: weekend + wysoka sprzedaż
df_weekend_high = df[
    (df['Dzien_tygodnia'].isin(['Saturday', 'Sunday'])) &
    (df['Sprzedaż'] > 1000)
]
🔴 Zadanie 6 – długość tekstu produktu
# .str.len() liczy liczbę znaków w tekście
df['Dlugosc_produktu'] = df['Produkt'].str.len()
🔥 Podsumowanie (co tu ćwiczyłeś)

✔ .dt → praca z datami
✔ .str → operacje tekstowe
✔ .isin() → filtrowanie wielu wartości
✔ .contains() → wyszukiwanie w tekście
✔ łączenie warunków logicznych (&)


"""