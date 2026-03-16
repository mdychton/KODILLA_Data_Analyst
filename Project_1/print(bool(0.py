text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0
number_of_y = 0



text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

# zmienne do liczenia samogłosek
number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0
number_of_y = 0

# liczenie w pętli
for char in text.lower():   # zamieniamy na małe litery
    if char == 'a':
        number_of_a += 1
    elif char == 'e':
        number_of_e += 1
    elif char == 'i':
        number_of_i += 1
    elif char == 'o':
        number_of_o += 1
    elif char == 'u':
        number_of_u += 1
    elif char == 'y':
        number_of_y += 1

print("a:", number_of_a)
print("e:", number_of_e)
print("i:", number_of_i)
print("o:", number_of_o)
print("u:", number_of_u)
print("y:", number_of_y)


for i in range(10, 0, -1):  # start=10, stop=1, step=-1
    print(i, end=" ")  # end=" " sprawia, że print nie przechodzi do nowej linii


count = 0   # licznik znalezionych liczb
number = 6  # zaczynamy od pierwszej liczby podzielnej przez 6

while count < 30:
    print(number, end=" ")
    number += 6  # następna liczba podzielna przez 6
    count += 1



my_number = 5

for i in range(1,10):
    print(i)
    if i > 5:
        print("wychodzimy z pętli, starczy tego dobrego!")
        break