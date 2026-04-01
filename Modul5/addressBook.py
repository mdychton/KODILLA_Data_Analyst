
"""
 #zaproponowane przez podpowiadacza w VSC
class addressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted."
        else:
            return "Contact not found"

    def list_contacts(self):
        return self.contacts

"""
from faker import Faker                 #print(dir(fake)) zeby sprawdzic jakie metody ma faker ( np jak nie ma tam position, czy company_name to nie wygeneruje nam takich fakowych danych)

fake = Faker()  # ❗ brakowało tego  print(fake.providers)

class BusinessCard:   # ❗ konwencja: klasy z dużej litery
    def __init__(self, first_name, last_name, company,job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email


businessCards = []

for _ in range(6):
    card = BusinessCard(   # ❗ nazwa musi się zgadzać z klasą
        fake.first_name(),     # ❗ nie name()
        fake.last_name(),
        fake.company(),        # ❗ nie company_name()
        fake.job(),            # ❗ nie position()
        fake.email()
    )
    businessCards.append(card)


for w in businessCards:
    print(w.first_name, w.last_name, "-", w.email)




#print(fake.providers)

"""
from faker import Faker — co to znaczy z dużej/malej litery?
from faker import Faker
faker → nazwa modułu (folder / plik .py) → zawsze mała litera
Faker → klasa w tym module → wielka litera (konwencja Pythona: klasy → PascalCase)
Dlaczego to ma znaczenie?
fake = Faker()  # tworzymy obiekt klasy Faker
Faker() = wywołanie klasy → tworzymy instancję → fake
Bez fake = Faker() nie masz instancji, więc nie możesz pisać np.:
fake.first_name()
3️⃣ Co by się stało, gdybyśmy nie mieli fake = Faker()?

Jeśli spróbujesz:

Faker.first_name()
❌ Błąd!
Faker to klasa, a first_name jest metodą instancji tej klasy, nie klasy samej w sobie

✅ Musisz mieć obiekt (fake = Faker()) → wtedy Python wie, którego „konkretnego generatora” użyć

🔹 Podsumowanie prostym językiem
Co	Co oznacza	Czy działa bez instancji?
faker	moduł	tak, można importować
Faker	klasa w module	tak, można importować
fake = Faker()	instancja klasy	trzeba, żeby wywoływać metody typu first_name()
fake.first_name()	metoda instancji	tak, działa tylko na instancji
Faker.first_name()	❌	nie działa

"""
    