class Car:
    def __init__(self, make, model_name, top_speed, color):
        self.make = make
        self.model_name = model_name
        self.top_speed = top_speed
        self.color = color

    # Variables
        self._current_speed = 0

    @property       
    def current_speed(self):
        return self._current_speed
    
    @current_speed.setter
    def current_speed(self, value):
            if value <= self.top_speed:
                self._current_speed = value
            else:
                raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
            



car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
car.current_speed
car.current_speed = 400

print(car.current_speed)



"""
W konstruktorze zmieniliśmy nazwę atrybutu, który przechowuje aktualną wartość prędkości samochodu. Zrobiliśmy to dlatego, że potrzebujemy go “ukryć” przed użytkownikami naszej klasy.

W świecie Pythona tak naprawdę nie da się ukryć żadnego atrybutu czy metody wewnątrz klasy. Jeśli ktoś chce, to i tak odczyta jej realną wartość. Natomiast istnieje konwencja mówiąca, że jeśli nazwa metody lub atrybutu zaczyna się od znaku podkreślenia (_), to jest to metoda ukryta – niewskazana do użycia bezpośrednio na obiekcie. W takich ukrytych metodach czy polach przechowuje się często informacje wewnętrzne, służące jako pomoc w obliczeniach lub przetwarzaniu danych.

W naszym przykładzie nie chcemy by ktoś “z zewnątrz” modyfikował wartość aktualnej prędkości samochodu. Chcemy, by użył do tego odpowiedniej metody, więc samą wartość, którą przechowujemy w instancji obiektu trzymamy w atrybucie “ukrytym”.

Konstrukcja @property to dekorator (w szczegółach omówimy ten fragment składni Pythona w dalszej części modułu). W tej chwili jednak ważne jest, że dodanie go zmieniło zachowanie metody current_speed, nie musi być ona wywoływana jak funkcja. Nawet nie da się tego zrobić:

car.current_speed()
>> TypeError: 'int' object is not callable
Metoda current_speed zachowuje się w tej chwili tak, jakby była zwykłym atrybutem klasy Car.

Następnie, udekorowaliśmy metodę current_speed(self, value) za pomocą @property.setter. Powoduje to, że w momencie, gdy będziemy chcieli przypisać wartość do atrybutu current_speed, zostanie wywołana tak naprawdę metoda udekorowana @property.setter, czyli current_speed(self, value). Dzięki temu zyskaliśmy miejsce, w którym możemy upewnić się, że przypisywane do atrybutu wartości są prawidłowe.

W tym konkretnym przypadku zapewniamy, że wartość current_speed nigdy nie przekroczy prędkości maksymalnej samochodu:

"""