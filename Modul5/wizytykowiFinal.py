from faker import Faker                 #print(dir(fake)) zeby sprawdzic jakie metody ma faker ( np jak nie ma tam position, czy company_name to nie wygeneruje nam takich fakowych danych)

fake = Faker()  # ❗ brakowało tego  print(fake.providers)

class BusinessCard:   # ❗ konwencja: klasy z dużej litery
    def __init__(self, first_name, last_name, company,job, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.job = job
        self.email = email
    
    def contact(self):
        print (f"Kontaktuje sie z  {self.first_name} {self.last_name}, {self.job}, {self.email}")

    @property
    def full_name_length(self):
        return len(f"{self.first_name} {self.last_name}")


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

    w.contact() #metoda

    print("Długość imienia i nazwiska:", w.full_name_length) #property  
    print("----")