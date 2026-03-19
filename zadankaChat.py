""" Liczby i sumy

Napisz program, który wypisuje liczby od 1 do 50.

Napisz program, który wypisuje tylko parzyste liczby od 1 do 100.

Oblicz sumę wszystkich liczb od 1 do 100 używając pętli for."""

print("zadania wymyslone przez chatGPT   Liczby i sumy - 1")

n = 51

for i in range(1,n):
    print(i, end=" ")


print("zadania wymyslone przez chatGPT   Liczby i sumy - 2")


n = 101
for i in range(1,n):
    if i % 2 == 0:
        print(i, end=" ")

print("zadania wymyslone przez chatGPT   Liczby i sumy - 3")

n = 101
total = 0
for i in range(1,n):
 total += i
print(total)

"""Listy

Utwórz listę z liczbami od 1 do 10 i wypisz każdy element pomnożony przez 2.

Masz listę numbers = [5, 12, 7, 20, 33, 18].

Wypisz tylko liczby większe od 10.

Utwórz listę kwadratów liczb od 1 do 15."""


print("zadania wymyslone przez chatGPT   Listy - 1")

my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
new_list = []
for number in my_list:
        new_list.append(number*2)
print(new_list)

print("zadania wymyslone przez chatGPT   Listy - 2")

numbers = [5, 12, 7, 20, 33, 18]
new_list2 = [number for number in numbers if number > 10]
print(new_list2)

print("zadania wymyslone przez chatGPT   Listy - 3")

n = 15
squares = [i**2 for i in range(1, n+1)]     
print(squares)


"""Łączenie pętli i list

Masz listę words = ["python", "java", "c++", "html"].

Wypisz wszystkie słowa, ale wielkimi literami (upper).

Utwórz pustą listę. Następnie użyj pętli, aby dodać do niej liczby od 1 do 20, które są podzielne przez 3."""


print("zadania wymyslone przez chatGPT   Listy i pętle - 1")

words = ["python", "java", "c++", "html"]
for word in words:
    print(word.upper())

print("zadania wymyslone przez chatGPT   Listy i pętle - 2")

empty_list = []
empty_list = [i for i in range(1, 20) if i % 3 == 0]
print(empty_list)

"""Słowniki

Utwórz słownik grades = {"Jan": 5, "Anna": 4, "Piotr": 3, "Kasia": 5}.

Wypisz imiona uczniów, którzy mają ocenę 5.

Zsumuj wszystkie oceny w słowniku."""


print("zadania wymyslone przez chatGPT   Slowniki - 1")

grades = {"Jan": 5, "Anna": 4, "Piotr": 3, "Kasia": 5}
for name, value in grades.items():
    if value == 5:
        print(f"{name} ma ocenę: {value}")

print("zadania wymyslone przez chatGPT   Slowniki - 2")

grades = {"Jan": 5, "Anna": 4, "Piotr": 3, "Kasia": 5}

print(f"Suma ocen: {sum(grades.values())}")

"""Wypisz tabliczkę mnożenia od 1 do 10 w formie:

1 x 1 = 1
1 x 2 = 2
...

Utwórz listę wszystkich par liczb (i, j) gdzie i i j są od 1 do 5, ale i + j jest większe niż 5."""



print("zadania wymyslone przez chatGPT   Zadania z pętlami zagnieżdżonymi - 1")


for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
print()
print("2opcja")
print()
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end=" ")
    print()


print("zadania wymyslone przez chatGPT   Zadania z pętlami zagnieżdżonymi - 2")


pairs = []

for i in range(1, 6):
    for j in range(1, 6):
        if i + j > 5:
            pairs.append((i, j))

print(pairs)


print()
print("2opcja")

pairs = [(i, j) for i in range(1, 6) for j in range(1, 6) if i + j > 5]
print(pairs)

print()

"""Zadania kreatywne

Napisz program, który pyta użytkownika o 5 liczb i zapisuje je w liście. Następnie wypisz największą i najmniejszą liczbę.

Napisz program, który usuwa duplikaty z listy: numbers = [1, 2, 2, 3, 4, 4, 5].

Napisz prostą grę: losuj liczbę od 1 do 10, a użytkownik ma zgadnąć. Wypisz komunikat, czy zgadł, czy nie."""

print("zadania wymyslone przez chatGPT   Zadania kreatywne - 1")
print()
"""
numbers = []

for i in range(5):
    num = int(input("Podaj liczbę: "))
    numbers.append(num)

print("Największa:", max(numbers))
print("Najmniejsza:", min(numbers)) """


print("zadania wymyslone przez chatGPT   Zadania kreatywne - 2")
print()

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)

print()
print("2opcja")

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)


print("zadania wymyslone przez chatGPT   Zadania kreatywne - 3")
print("Opjca1")

import random

number = random.randint(1, 10)

guess = int(input("Zgadnij liczbę od 1 do 10: "))

if guess == number:
    print("Brawo! Zgadłeś!")
else:
    print(f"Nie zgadłeś. Wylosowana liczba to {number}")

print("Opjca2")

import random

number = random.randint(1, 10)

while True:
    guess = int(input("Zgadnij liczbę: "))
    
    if guess == number:
        print("Brawo!")
        break
    elif guess < number:
        print("Za mała")
    else:
        print("Za duża")
    

print()

