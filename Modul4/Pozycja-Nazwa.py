def fun_default(a,b):
    pass


fun_default(1, 2)        # pozycyjne
fun_default(a=1, b=2)    # nazwane
fun_default(1, b=2)      # mieszane


def fun_positional(a, b,/):    # OK
    pass

fun_positional(1, 2)      # OK
fun_positional(a=1, b=2)  #  Błąd!



def fun_keyword(*, a, b):
    pass

fun_keyword(a=1, b=2)  # OK
fun_keyword(1, 2)      #  Błąd!


"""
Argumenty między / a * → pozycja lub nazwa

Przykład:

def fun(a, b, /, c, d, *, e, f):
    pass
Argument	Jak można podać?
a	tylko pozycyjne
b	tylko pozycyjne
c	pozycyjne lub nazwane
d	pozycyjne lub nazwane
e	tylko nazwane
f	tylko nazwane

💡 Podsumowanie w jednym zdaniu:

Wszystko przed / → pozycyjne
Wszystko po * → nazwane
Wszystko pomiędzy → dowolnie

"""