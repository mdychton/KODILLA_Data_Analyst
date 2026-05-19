"""
Callbacki w Dash to mechanizm, który łączy interakcje użytkownika z aktualizacją aplikacji.

Najprościej:

Callback = funkcja, która uruchamia się automatycznie, gdy coś w interfejsie się zmieni.

🔁 Jak to działa (intuicja)

Masz 3 elementy:

1. Input (co wywołuje zmianę)

Np.:

kliknięcie przycisku
przesunięcie slidera
wpisanie tekstu
2. Callback (logika)

Funkcja, która:

bierze dane z Input
robi obliczenia / przetwarza
tworzy wynik
3. Output (gdzie trafia wynik)

Np.:

tekst na stronie
wykres
tabela
🧠 Schemat myślowy
USER ACTION → INPUT → CALLBACK → OUTPUT (UI UPDATE)
📦 Przykład z Twojego kalkulatora
@app.callback(
    Output('output', 'children'),   # gdzie wynik się pokazuje
    Input('submit-btn', 'n_clicks'), # co uruchamia funkcję
    [State('product-1', 'value'), State('product-2', 'value')] # dane do użycia
)
def multiply(n_clicks, a, b):
    return a * b
🟡 Co się dzieje krok po kroku:
Użytkownik wpisuje liczby
NIC się nie dzieje (bo State nie uruchamia callbacka)
Użytkownik klika Oblicz
n_clicks się zmienia → callback się uruchamia
funkcja bierze wartości product-1 i product-2
liczy wynik
wynik trafia do output
🔵 Input vs State (ważne)
Input
uruchamia callback
State
tylko dostarcza dane
NIE uruchamia callbacka
🧩 Dlaczego to jest ważne?

Bo dzięki callbackom Dash:

nie przeładowuje strony (jak klasyczny HTML)
działa jak aplikacja (dynamicznie)
wszystko jest reaktywne
⚡ Prosta analogia

Callback = automat w sklepie

wrzucasz monetę (Input)
automat liczy co masz dostać (Callback)
wypada produkt (Output)


"""