print("Zadanie 1")

Lista_zakupów = {
    "Piekarnia": ['Chleb','Pączek', 'Bułki'],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola']
}


sum = 0

for sklep, produkty in Lista_zakupów.items():
    print (f'Idę do {sklep}, i kupuję tam {", ".join(produkty).upper()}')
    sum += len(produkty)

print(f"W sumie kupuję {sum} produktów.")

print("Zadanie 2")

numbers = []

for i in range(1, 101):
    if i % 5 == 0:
        numbers.append(i)
for n in numbers:
    print(n, end=" ")
print()
for n in numbers:
    print(n**3, end=" ")



"print('TESTKOLEGA')"

