"""
W Pythonie dekorator jest funkcją, która jako parametr przyjmuje inną funkcję 
(pamiętaj, że wszystko w Pythonie jest obiektem, więc bez problemu możemy przypisać funkcję do zmiennej, bez jej wywołania).
 Dzięki temu zachowaniu jesteśmy w stanie dynamicznie zmienić zachowanie dekorowanej funkcji. Dekoratory w Pythonie wywołujemy z użyciem @.

"""

# dekorator to funkcja, która przyjmuje inną funkcję jako argument i rozszerza jej funkcjonalność bez modyfikowania jej kodu źródłowego.

def say_hello():
   greeting = "Hello stranger!"
   return greeting

def say_louder(func):
   def wrapper():
       result = func()
       return result.upper()
   return wrapper

say_hello_louder = say_louder(say_hello)
print(say_hello())  # Output: Hello stranger!
print(say_hello_louder())  # Output: HELLO STRANGER!

# Możemy również użyć składni dekoratora @, aby osiągnąć ten sam efekt: składnia dekoratora @ jest bardziej elegancka i czytelna, ponieważ bezpośrednio wskazuje, że funkcja jest dekorowana.   