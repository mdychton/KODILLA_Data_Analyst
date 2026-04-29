"""
🔹 Co to jest map w Pandas?

👉 map() służy do zamiany wartości według reguły (słownika / funkcji)

Najprościej:

„weź każdą wartość i zamień ją na coś innego”

🔹 Najważniejsze różnice vs apply
Funkcja	Gdzie działa	Co robi
map()	tylko Series (jedna kolumna)	szybkie zamiany wartości
apply()	Series + DataFrame	dowolna logika
🔹 Jak działa map?

Masz:

car_dict = {
    'Jan': 'BMW',
    'Anna': 'Audi'
}
✔️ Kod
# map zamienia wartości w kolumnie na podstawie słownika
df['Marka_samochodu'] = df['Przedstawiciel'].map(car_dict)
🔍 Co się dzieje krok po kroku:
bierze wartość z kolumny Przedstawiciel
szuka jej w car_dict
podstawia odpowiadającą wartość
📌 przykład:
Przedstawiciel	wynik
Jan	BMW
Anna	Audi
🔴 WAŻNE (częsty błąd)

Jeśli klucza nie ma w słowniku:

👉 wynik = NaN

🔧 Jak zabezpieczyć brakujące wartości?
df['Marka_samochodu'] = df['Przedstawiciel'].map(car_dict).fillna('brak danych')
🔹 map vs apply vs replace (mega ważne)
✔️ map
df['col'].map(dict)

👉 szybka zamiana wartości

✔️ replace (podobne do map)
df['col'].replace({'A': 'B'})

👉 działa też bez Series-only ograniczenia

✔️ apply
df['col'].apply(lambda x: x*2)

👉 logika, warunki, obliczenia



============ZADANIA============

🟢 Zadanie 1 – mapowanie regionów

👉 Dodaj kolumnę Region_kraj:

East → Poland
West → Germany
North → Sweden
South → Italy
# słownik mapowania regionów na kraje
region_dict = {
    'East': 'Poland',
    'West': 'Germany',
    'North': 'Sweden',
    'South': 'Italy'
}

# map zamienia wartości w kolumnie według słownika
df['Region_kraj'] = df['Region'].map(region_dict)
🟢 Zadanie 2 – segment samochodu

👉 Dodaj Segment_auto:

BMW, Audi → premium
Toyota → standard
Fiat → budget
# słownik segmentów aut
car_segment = {
    'BMW': 'premium',
    'Audi': 'premium',
    'Toyota': 'standard',
    'Fiat': 'budget'
}

# mapowanie marki na segment
df['Segment_auto'] = df['Marka_samochodu'].map(car_segment)
🟡 Zadanie 3 – brakujące dane

👉 Dodaj Marka_samochodu i zamień brakujące na "unknown"

# słownik przypisujący przedstawicieli do aut
car_dict = {
    'Szymon': 'Mazda',
    'Grzegorz': 'Toyota',
    'Paulina': 'BMW',
    'Krystian': 'Audi',
    'Franciszek': 'Fiat',
    'Patryk': 'Seat'
}

# map + fillna zabezpiecza brakujące wartości
df['Marka_samochodu'] = (
    df['Przedstawiciel']
    .map(car_dict)
    .fillna('unknown')   # jeśli brak dopasowania
)
🟡 Zadanie 4 – kraj produkcji (odwrotne mapowanie)

👉 Zamień marki na kraj:

BMW, Audi → DE
Toyota → JP
Fiat → IT
# odwrotne mapowanie: marka → kraj
brand_country = {
    'BMW': 'DE',
    'Audi': 'DE',
    'Toyota': 'JP',
    'Fiat': 'IT'
}

# zamiana wartości w kolumnie
df['Kraj_auta'] = df['Marka_samochodu'].map(brand_country)
🔴 Zadanie 5 – status przedstawiciela

👉 Dodaj kolumnę Status:

Szymon → TOP
reszta → REGULAR
# mapowanie konkretnej osoby
status_dict = {
    'Szymon': 'TOP'
}

# map + fillna dla reszty
df['Status'] = (
    df['Przedstawiciel']
    .map(status_dict)
    .fillna('REGULAR')
)
🔴 Zadanie 6 – klasyfikacja sprzedaży (bez apply!)

👉 Dodaj Poziom_sprzedaży:

<300 → low
300–900 → mid

900 → high

# warunki zamienione na kategorie
sales_map = {
    'low': 'low',
    'mid': 'mid',
    'high': 'high'
}

# tworzymy warunek przez cut (lepsze niż apply)
df['Poziom_sprzedazy'] = pd.cut(
    df['Sprzedaż'],
    bins=[0, 300, 900, float('inf')],
    labels=['low', 'mid', 'high']
)
🔥 Co tu było ważne?

✔ map = słownik → szybkie zamiany
✔ .fillna() = zabezpieczenie braków
✔ pd.cut() = profesjonalna alternatywa dla apply
✔ brak logiki w map → tylko „lookup”


KIEDYS BYLO COS TAKIEGO JAK APPLYMAP ALE TO BYLO TYLKO DLA DataFrame (nie Series) I NIE JEST JUŻ WSPARTE

df = df.apply(lambda col: col.str.upper() if col.dtype == 'object' else col)

"""