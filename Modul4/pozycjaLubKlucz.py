shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy",
]

def shopping(items, payment='card', shop='local'):
    shopping_cart = "Koszyk zawiera:\n"
    
    for item in items:                                          #skad funcja wie ze items odnosi sie do shopping_items? Bo w momencie wywolania funkcji, argument shopping_items staje sie wartoscia parametru items
        shopping_cart += item + '\n'
    
    shopping_cart += "\nSposób płatności: " + payment
    shopping_cart += "\nSklep: " + shop
    
    return shopping_cart

basket = shopping(shopping_items, shop='lidl', payment='cash')           #argument shopping_items staje sie wartoscia parametru items w momencie wywolania funkcji #funcja basket otrzymuje wartosc zwrocona przez funkcje shopping, a ta wartosc jest zbudowana na podstawie argumentu shopping_items, ktory staje sie wartoscia parametru items w funkcji shopping
print(basket)                                                              # dopiero tutaj funkcja shopping jest wykonywana, a nie w momencie jej definicji, dlatego items dostaje wartosc dopiero przy wywolaniu funkcji, a nie w momencie jej tworzenia - dodatkowo jak podajemy jawnie to kolejnosc argumentow nie ma znaczenia, bo sa one przypisywane do odpowiednich parametrow na podstawie nazw, a nie pozycji


"""
🔹 1. shopping_items — co to jest?
shopping_items = [...]

👉 To jest po prostu:
lista (list) — czyli zbiór elementów

✔️ Tu wszystko jest jasne

🔹 2. Definicja funkcji
def shopping(items, payment='card', shop='local'):

👉 Tworzysz funkcję o nazwie shopping

Parametry:
items → zmienna (placeholder) — jeszcze nie ma wartości!
payment='card' → domyślna wartość
shop='local' → domyślna wartość

📌 WAŻNE:
Na tym etapie:
👉 funkcja NIE jest wykonywana
👉 tylko ją definiujesz (tworzysz przepis)

🔹 3. Co to jest shopping_cart?
shopping_cart = "Koszyk zawiera:\n"

👉 To NIE jest:

❌ funkcja
❌ metoda

👉 To jest po prostu:
zmienna (variable) typu string

📌 Możesz myśleć o niej jak o:
➡️ "kartce", na której budujesz wynik

🔹 4. Pętla
for item in items:

👉 I tu masz bardzo dobre pytanie:

skąd wiadomo czym jest items?

Odpowiedź:
👉 JESZCZE NIE WIADOMO

Bo funkcja tylko czeka na dane.

To tak jak:

„dla każdego elementu w czymś, co dopiero dostanę”

🔹 5. Budowanie wyniku
shopping_cart += item + '\n'

👉 To znaczy:

weź tekst z shopping_cart
dodaj kolejny produkt
shopping_cart += "\nSposób płatności: " + payment
shopping_cart += "\nSklep: " + shop

👉 Dalej:

dopisujesz informacje o płatności i sklepie
🔹 6. return
return shopping_cart

👉 Funkcja:
➡️ oddaje gotowy wynik (tekst)

🔹 7. KLUCZOWY MOMENT — wywołanie funkcji
basket = shopping(shopping_items)

👉 Tu dzieje się magia 🔥

Co się dzieje krok po kroku:
Wywołujesz funkcję shopping

Podajesz:

items = shopping_items

👉 I DOPIERO TERAZ:

for item in items:

👉 Python wie:
➡️ items = ["jajka", "bułka", ...]

🔹 8. Co to jest basket?
basket = shopping(shopping_items)

👉 basket to:

❌ nie funkcja
❌ nie metoda

👉 To jest:
zmienna

📌 która przechowuje wynik funkcji

Czyli:

basket = "Koszyk zawiera:\n..."
🔥 Całość w jednym zdaniu

👉 Funkcja to przepis,
👉 items to puste miejsce na dane,
👉 shopping_cart to zmienna budująca wynik,
👉 a basket to gotowy rezultat po wykonaniu funkcji


💡 Ultra skrót (1 zdanie)

👉 Funkcja to przepis,
👉 wywołanie to moment gotowania,
👉 items dostaje wartość dopiero przy wywołaniu.

"""