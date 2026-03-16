



i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
    
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i = i + 1

print("koniec programu")


i = 2

while i <= 20:
    print(i)
    i += 2

print("koniec programu")


for i in range(2, 21, 2):
    print(i)


sum = 0

for i in range(1, 101):
    sum += i

print(sum)


names = ["Anna", "Jan", "Piotr"]

for name in names:
    print("Hello", name)


numbers = [3, 7, 2, 9, 4]

sum = 0

for n in numbers:
    sum += n

print(sum)


numbers = [4, 7, 1, 9, 3, 8]

for n in numbers:
    if n > 5:
        print(n)



numbers = [10, 15, 22, 33, 41]

result = [n**2 for n in numbers if n > 20]

print(result)


numbers = [1,2,3,4,5,6]

result = [x**2 for x in numbers if x % 2 == 0]

print(result)