print("Zadanie 2")
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}

for name in names:
    name_dict.setdefault(name[0], set()).add(name)


print(name_dict['P'])
print(name_dict['A'])
print(name_dict['B'])
print(name_dict['O'])
print(name_dict['J'])

print("Zadanie 3")

