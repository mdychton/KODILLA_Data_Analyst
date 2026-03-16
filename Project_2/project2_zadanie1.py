
print("Zadanie 1")

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]

name_dictionary = {}
for name in name_list:
    name_dictionary[name] = len(name)
print(name_dictionary)


print("Zadanie 2")

numbers_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
new_numbers_list = []
for number in numbers_list:
    if number > 1:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            new_numbers_list.append(number)
print(new_numbers_list)


print("Zadanie 3")

week_days = ['pon','śro','pią','sob']
week_days.append('niedz')
week_days.append('czwar')
week_days.append('wto')
print(week_days)

week_days2 = ['pon','śro','pią','sob']
week_days2.insert(1, 'wto')
week_days2.insert(3, 'czwar')
week_days2.insert(7, 'niedz')
print(week_days2)



print("Zadanie 4")

steps = [
    (6, "zalej herbatę(wodą z czajnika)"),
    (3, "wyjmij kubek"),
    (2, "włącz czajnik"),
    (1, "nalej wody do czajnika"),
    (4, "znajdź opakowanie herbaty"),
    (5, "włóż herbatę do kubka")
]
steps.sort()
print("Kosmito, to są kroki do zaparzenia herbaty:" + str(steps))