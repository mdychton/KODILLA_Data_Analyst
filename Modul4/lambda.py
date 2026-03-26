shopping_items = [
    ("ziemniak", 2.5, 0.51),
    ("cebula", 3, 1.60),
    ("ser", 0.8, 15.50)
]

# lambda to funkcja anonimowa, która może być użyta w miejscu, gdzie potrzebna jest funkcja, ale nie chcemy definiować jej osobno. Jest to szczególnie przydatne w przypadku funkcji, które są używane tylko raz, lub jako argumenty do innych funkcji.


def get_index_1_tuple_element(given_tuple):
    return given_tuple[1]

sorted_items = sorted(shopping_items, key=get_index_1_tuple_element)    # sortowanie po 1 elemencie krotki, czyli po cenie za kilogram, funkcja get_index_1_tuple_element jest przekazywana jako argument do funkcji sorted, która używa jej do porównywania elementów listy shopping_items.
print(sorted_items)

# to samo można osiągnąć za pomocą lambda, bez konieczności definiowania osobnej funkcji get_index_1_tuple_element


sorted_items = sorted(shopping_items, key=lambda given_tuple: given_tuple[1])    # lambda to funkcja anonimowa, sortowanie po ilosci kilogramow, czyli po 2 elemencie krotki, funkcja lambda jest przekazywana jako argument do funkcji sorted, która używa jej do porównywania elementów listy shopping_items.
print(sorted_items)


def customized_hello(first_name, last_name, gender_prefix='Mr'):                    #dobra praktyka to opisac funkcje za pomocą docstring, czyli trzech cudzysłowów, które pozwalają na opisanie funkcji, jej argumentów i tego co robi, jest to szczególnie przydatne w przypadku funkcji, które są używane przez innych programistów, którzy mogą nie znać jej działania.
    """
        Prints hello, based on arguments passed
        Arguments:
        first_name,
        last_name
        Optional arguments:
        gender_prefix:  Mr/Ms based on sex of person
    """
    print("Hello %s %s %s" % (gender_prefix, first_name, last_name))

help(customized_hello)