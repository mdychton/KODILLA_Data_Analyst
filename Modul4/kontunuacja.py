

""""
def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)

""" 
"""                                                                    #inna wersja powyzszej funkcji
def shopping(items, payment='card', shop='local'):
    lines = []
    lines.append(f"Idę na zakupy do {shop}.")
    lines.append("Kupię następujące rzeczy:")

    for item in items:
        lines.append(f" - {item}")

    lines.append(f"By zapłacić, używam {payment}.")
    
    return "\n".join(lines)
"""

""" # podaj text, a ja go wyświetlę
print("Pokażę wszystko, co wpiszesz!")
text = input()
print("Oto Twój tekst: ***%s***" % text)
print(f"Oto Twój tekst: ***{text}***")

"""
"""
items_text = "cola,whiskey,lód"                 #podaj tekst, a ja go rozdzielę na elementy listy, rozdzielając je przecinkiem (lub innym znakiem , ale wtedy ten znak musi byc tez w tekscie mp cola*whyski*lod)(uzywajac funcji SPLIT) czyli tworząc listę z elementami "cola", "whiskey" i "lód"
items = items_text.split(',')
print(type(items))
print(len(items))
"""

def shopping(items, payment='card', shop='local shop'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)