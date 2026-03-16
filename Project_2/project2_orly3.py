
"rozwiazanie1"

fibonacci = [1, 1]

for i in range(28):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)

"rozwiazanie2"

fibonacci = []
num = 30

n = 1
while len(fibonacci) < num:
    if n == 1 or n == 2:
        fibonacci.append(1)
    else:
        fibonacci.append(sum(fibonacci[-2:]))
    n += 1

print(fibonacci)