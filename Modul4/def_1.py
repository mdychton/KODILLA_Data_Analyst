def show_2_values():
    print("Value 1: 10")
    print("Value 2: 20")
show_2_values()



print()


a = 1

def scope_demo():
    a = 2
    print(a)

scope_demo()
print(a)


print()

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())

shopping_result = shopping()
print(shopping_result)



def no_result_function():
    print("I am just printing I love you")
    print("and returning nothing to you!") 
print(no_result_function())
print(type(no_result_function())    )

print()
def day_times():
    return "morning", "afternoon", "evening", "night"

times = day_times()
print(times)
print(type(times))


first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)  #old style
print(f"Trzeci element to {third}") #new style, f-string


print()

def customized_hello(first_name, last_name):
    print("Hello Mr %s %s" % (first_name, last_name))
    print(f"Hello Mr {first_name} {last_name}")

customized_hello("John", "Cleese")

print()

def customized_hello(first_name, last_name, gender_prefix='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name}!")

customized_hello("John", "Cleese")
customized_hello("Clara", "Cleese", "Ms") #tu jest podany 3 argument, który nadpisuje wartość domyślną "Mr"

"""Chociaż zdefiniowaliśmy trzeci parametr, to nadal przy wywołaniu podajemy dwa. 
Jest to możliwe, ponieważ ten trzeci jest argumentem domyślnym, który w razie jego braku przyjmuje wartość „Mr”."""

print()

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor"
]

def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)


print()

shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy",
]

def shopping(items):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopping(shopping_items)
print(basket)


"""
🔄 

✔ Prawie dobrze, ale lepiej powiedzieć:

👉 argument staje się wartością parametru w momencie wywołania funkcji

🧠 Proste zdanie do zapamiętania

👉 Argument → wchodzi do funkcji
👉 Parametr → odbiera argument w środku funkcji

"""


 
