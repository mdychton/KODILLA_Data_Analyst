"""
🔹 1. Co robi reset_index()

👉 reset_index():

usuwa aktualny indeks (np. Student A, B, C…)
zamienia go na zwykłą kolumnę
tworzy nowy indeks 0,1,2,3...
📌 Przykład
df_new_index = df.reset_index()

# df ma indeks: Student A, B, C...
# po reset_index:

df_new_index
   index        e1   e2
0  Student A   80   75
1  Student B   85   88
2  Student C   90   92

💡 Komentarz:

stary indeks → kolumna index
nowy indeks → liczby
🔹 2. Dodanie nowej kolumny
df_new_index['student_name'] = ['Adrian','Bartłomiej','Celina','Dagmara']

# dodajemy nową kolumnę ręcznie

📌 wynik:

   index        e1   e2   student_name
0  Student A   80   75   Adrian
1  Student B   85   88   Bartłomiej
2  Student C   90   92   Celina
3  Student D   ...  ...  Dagmara
🔥 3. set_index() — co robi?

👉 set_index():

wybiera kolumnę
i robi z niej nowy indeks
📌 Przykład
df_new_index.set_index('student_name')
💡 co się dzieje:
student_name   e1   e2
Adrian        80   75
Bartłomiej    85   88
Celina        90   92
Dagmara       ...  ...
🔥 komentarz:
# ustawiamy kolumnę 'student_name' jako nowy indeks
# stare numery 0,1,2,3 znikają z indeksu
⚠️ WAŻNE

set_index():

✔️ zmienia indeks
❌ NIE zmienia oryginalnego DataFrame (chyba że inplace=True)

df_new_index.set_index('student_name', inplace=True)
🔹 4. Drugi sposób — ręczna zmiana index
df_new_index2 = df.reset_index()

# bezpośrednio podmieniamy indeks

df_new_index2.index = ['Adrian','Bartłomiej','Celina','Dagmara']
📌 efekt:
               index        e1   e2
Adrian        Student A   80   75
Bartłomiej    Student B   85   88
Celina        Student C   90   92
Dagmara       Student D   ...  ...
💡 komentarz:
# ręcznie ustawiamy nowy indeks (lista musi mieć tyle samo elementów co wierszy)
# nie zmieniamy kolumny — tylko "etykiety wierszy"
🔥 KLUCZOWA RÓŻNICA
metoda	co robi
set_index()	używa kolumny jako indeksu
df.index = [...]	ręcznie nadpisuje indeks
reset_index()	zamienia indeks na kolumnę
🧠 INTUICJA (najważniejsze)
reset_index() → „rozbij indeks na kolumnę”
set_index() → „z kolumny zrób indeks”
df.index = ... → „ręcznie przepisz etykiety”
💡 PRO TIP (praktyka)

W pracy najczęściej używa się:

df.set_index('id')

a nie ręcznego df.index = ...

"""