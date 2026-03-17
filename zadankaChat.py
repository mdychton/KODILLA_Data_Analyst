
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


print("zadania wymyslone przez chatGPT   Listy i pętle - 1")

words = ["python", "java", "c++", "html"]
for word in words:
    print(word.upper())

print("zadania wymyslone przez chatGPT   Listy i pętle - 2")

empty_list = []
empty_list = [i for i in range(1, 20) if i % 3 == 0]
print(empty_list)

print("zadania wymyslone przez chatGPT   Slowniki - 1")

grades = {"Jan": 5, "Anna": 4, "Piotr": 3, "Kasia": 5}
for name, value in grades.items():
    if value == 5:
        print(f"{name} ma ocenę: {value}")

print("zadania wymyslone przez chatGPT   Slowniki - 2")

grades = {"Jan": 5, "Anna": 4, "Piotr": 3, "Kasia": 5}

print(f"Suma ocen: {sum(grades.values())}")

print("zadania wymyslone przez chatGPT   Zadania z pętlami zagnieżdżonymi - 1")

