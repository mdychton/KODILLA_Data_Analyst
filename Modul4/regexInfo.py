
import re

# 1️⃣ Czyszczenie tekstu (litery + cyfry tylko)
tekst = "A man, a plan, a canal: Panama!"
czysty = re.sub(r'[^a-z0-9]', '', tekst.lower())
# wynik: "amanaplanacanalpanama"
# użycie: palindromy, preprocessing danych

# 2️⃣ Normalizacja spacji (jedna spacja zamiast wielu)
tekst = "ala    ma   kota"
tekst_norm = re.sub(r'\s+', ' ', tekst)
# wynik: "ala ma kota"
# użycie: czysty tekst, formatowanie

# 3️⃣ Wyciąganie liczb z tekstu
tekst = "mam 2 koty i 15 psów"
liczby = re.findall(r'\d+', tekst)
# wynik: ['2','15']
# użycie: parsowanie danych, ekstrakcja liczb

# 4️⃣ Szybkie czyszczenie wszystkiego co nie jest literą/cyfrą/_
tekst = "Hello, World!_2023"
czysty2 = re.sub(r'\W+', '', tekst)
# wynik: "HelloWorld_2023"
# użycie: identyfikatory, nazwy plików, input od użytkownika

# 🔹 Metody przydatne:
# re.sub(pattern, replace_with, tekst) -> zamienia wszystko pasujące
# re.findall(pattern, tekst) -> lista dopasowań
# re.match(pattern, tekst) -> dopasowanie na początku
# re.search(pattern, tekst) -> dopasowanie w całym tekście

# 🔹 Tipy praktyczne:
# - zawsze używaj r'' (raw string) przy regexach
# - lowercase + regex = ignorowanie wielkości liter
# - chainowanie metod string + regex = super czytelne


tylko litery i cyfry (lepsza wersja)
r'\W+'

👉 usuwa wszystko co NIE jest:

literą
cyfrą
_


re.sub(r'[^a-z0-9]', '', tekst.lower())