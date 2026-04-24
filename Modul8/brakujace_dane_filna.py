"""
🧠 fillna() — CO TO ROBI?

👉 fillna() =

„wypełnij brakujące wartości (NaN) czymś sensownym”

📊 1. Twoje dane
df_with_nulls = pd.DataFrame({
    'A':[1,100,np.nan,1000,10000],
    'B':[2,4,2,4,np.nan],
    'C':[40,np.nan,20,np.nan,np.nan]
})
🔹 2. Wypełnianie stałą wartością
df_with_nulls.fillna('NOWA WARTOŚĆ')
🧠 komentarz:
# każdy NaN → zamieniany na string
# NIE ma sensu analitycznego
# tylko pokazuje mechanizm
🔥 3. fillna z mean (najczęstsze)
df_with_nulls['B'].fillna(df_with_nulls['B'].mean())
🧠 komentarz:
# średnia ignoruje NaN
# brakujące wartości → zastąp średnią
📊 przykład:
B = [2,4,2,4,NaN]
mean = 3

👉 NaN → 3

🔁 4. ffill (forward fill)
df_with_nulls.fillna(method='ffill')
🧠 komentarz:
# bierze poprzednią wartość i kopiuje w dół
# działa dobrze w danych czasowych
🔁 5. bfill (backward fill)
df_with_nulls.fillna(method='bfill')
🧠 komentarz:
# bierze następną wartość i kopiuje w górę
📊 PRZYKŁAD LOGIKI (mega ważne)
A:
1
100
NaN   ← ffill = 100
1000
NaN   ← ffill = 1000
⚠️ WAŻNE: fillna NIE zmienia danych na stałe
df_with_nulls.fillna(0)

👉 tylko zwraca nowy DataFrame

✔️ jeśli chcesz zapisać:
df_with_nulls = df_with_nulls.fillna(0)
🧠 6. fillna vs ffill/bfill
metoda	co robi
fillna(0)	stała wartość
fillna(mean)	statystyka
ffill	poprzednia wartość
bfill	następna wartość
🔥 7. NAJWAŻNIEJSZA INTUICJA

👉 fillna = „strategia uzupełniania danych”

Nie ma jednej dobrej metody — zależy od danych:

📊 kiedy co używać
✔️ mean/median

👉 dane numeryczne (np. ceny)

✔️ ffill

👉 dane czasowe (np. kursy, pogoda)

✔️ bfill

👉 dane „przyszłościowe” / brakujące końcówki

✔️ 0

👉 liczniki / brak aktywności

🧠 8. WAŻNA RÓŻNICA (częsty błąd)
❌ to NIE zmienia oryginału:
df.fillna(0)
✔️ to zmienia:
df = df.fillna(0)
🔥 TL;DR

👉 fillna() = uzupełnianie braków
👉 4 główne strategie:

stała wartość
średnia / mediana
ffill
bfill
🧠 Jedno zdanie do zapamiętania

👉 „fillna to sposób, w jaki decydujesz co zastępuje brak wiedzy w danych”

"""