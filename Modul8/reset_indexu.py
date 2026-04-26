"""
1. Tak — domyślnie axis=0
pd.concat([df1, df2, df3])

👉 to jest to samo co:

pd.concat([df1, df2, df3], axis=0)

👉 czyli: doklejamy wiersze (w dół)

🔹 2. Dlaczego to działa mimo różnych indexów?

Bo przy axis=0:

👉 pandas nie dopasowuje wierszy po indexie
👉 pandas po prostu dokleja je jeden pod drugim

🧠 Co pandas sprawdza przy axis=0?

👉 kolumny, nie index

Czyli:

df1: A B C D
df2: A B C D
df3: A B C D

👉 kolumny pasują → można dokleić

🔍 Co się dzieje z indexem?

pandas mówi:

„OK, biorę indexy takie jakie są i układam je po kolei”

Czyli:

df1 → 0,1,2,3
df2 → 4,5,6,7
df3 → 8,9,10,11

👉 i dokładnie to widzisz w wyniku

🔥 KLUCZOWA różnica
Operacja	Co musi pasować	Co jest ignorowane
axis=0 (w dół)	kolumny	index
axis=1 (w bok)	index	kolumny
💥 Dlatego:
✅ To działa:
pd.concat([df1, df2, df3], axis=0)

bo:

kolumny są takie same ✅
index może być różny ✅ (bo nie jest używany do dopasowania)
❌ To się psuje:
pd.concat([df1, df2, df3], axis=1)

bo:

indexy są różne ❌
więc pandas robi dopasowanie → i wychodzą NaNy
🔥 Jedno zdanie do zapamiętania

👉 axis=0 → patrzy na kolumny
👉 axis=1 → patrzy na index

🧠 BONUS: dlaczego to ma sens?

Wyobraź sobie:

axis=0 (doklejasz wiersze)

To jak dodawanie nowych rekordów do tabeli:

klient 1
klient 2
klient 3

👉 nie muszą mieć tych samych ID — to nowe dane

axis=1 (doklejasz kolumny)

To jak rozszerzanie informacji o tym samym kliencie:

ID | name | age | salary

👉 wtedy ID musi się zgadzać

🚀 TL;DR

✔ axis=0 → „dodaj więcej wierszy” → index nie musi się zgadzać
✔ axis=1 → „dodaj więcej kolumn” → index MUSI się zgadzać
"""