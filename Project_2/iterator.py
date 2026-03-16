
vegetables = ["burak", "ziemniak", "szczypior", "cebula"]





shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]


shopping_dict = dict(shopping)

for product in shopping_dict.items():
    print(product)

#dlaczego nie musze tu zastosować dict? ok ma dwa sposoby albo prezz disc albo tak jak nizej
poland_neighbours = {"Niemcy": "Berlin", "Czechy": "Praga", "Słowacja": "Bratysława", "Ukraina": "Kijów", "Białoruś": "Mińsk", "Litwa": "Wilno", "Rosja": "Moskwa"} 
for country, capital in poland_neighbours.items():
    print(f"{country}: {capital}")


numbers = [1, 3, 5, 11, 20]
squares = []
for number in numbers:
    squares.append(number * number)
print(f"Na wstępie mieliśmy taką listę {numbers}")
print(f"A oto jej kwadraty {squares}")



squares = [number * number for number in numbers]
print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")


numbers = [1, 2, 0, 3, 0, 0, 0]
squares = [number * number for number in numbers if number > 0]
print(f"Bez zer {squares} uzyskano dzięki list comprehension")


names = ['Arystoteles','Platon','Sokrates']
names_len = [len(name) for name in names]
print(names_len)


weekdays = ["pon", "wto", "śro", "czw", "pią", "sob", "nie"]
# indeks:     0      1      2      3      4      5      6
weekdays[0:2]
print(weekdays[0:2])
print(weekdays[:5])
print(weekdays[5:])
print(weekdays[-2:])
print(weekdays[-1:])
print(weekdays[:-1])

