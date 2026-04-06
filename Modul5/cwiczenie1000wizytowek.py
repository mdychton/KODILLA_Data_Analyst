from faker import Faker
from datetime import datetime

fake = Faker()

# 🔹 Klasa wizytówki
class Contact:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


# 🔹 Dekorator mierzący czas
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()

        result = func(*args, **kwargs)

        end = datetime.now()
        duration = (end - start).total_seconds()

        print(f"Czas wykonania: {duration} sekund")

        return result

    return wrapper


# 🔹 Funkcja tworząca 1000 wizytówek
@measure_time
def create_contacts():
    contacts = []

    for _ in range(1000):
        contact = Contact(
            fake.first_name(),
            fake.last_name(),
            fake.email()
        )
        contacts.append(contact)

    return contacts


# 🔹 Uruchomienie
contacts = create_contacts()

# 🔹 Podgląd kilku rekordów
for c in contacts[:100]:
    print(c.first_name, c.last_name, "-", c.email)