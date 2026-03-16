
shopping_A = {"pieczywo", "masło", "ser"}
shopping_B = {"wędlina", "masło", "cytryna"}


sets_sum = shopping_A | shopping_B
print(sets_sum)

sets_sum = shopping_A.union(shopping_B)
print(sets_sum)


sets_multiplication = shopping_B & shopping_A
print(sets_multiplication)

sets_difference = shopping_A - shopping_B
print(sets_difference)

sets_difference = shopping_B - shopping_A
print(sets_difference)

shopping_list = ["buraki", "masło", "chleb"]
# aaa, Tomek nie je glutenu!
shopping_list[2] = "chleb bezglutenowy"
print(shopping_list)


shopping_list = ["buraki", "masło", "chleb"]
# dostajesz SMS
shopping_list.append("tuńczyk")
print(shopping_list)


directions = ["północ", "południe", "wschód", "zachód"]
del directions[3], directions[2]
directions.remove("południe")
print(directions)




shopping_list = ["buraki", "masło", "chleb"]
sorted_shopping_list = sorted(shopping_list)
print(f"Lista po sortowaniu {sorted_shopping_list}")
print(f"Lista pierwotna {shopping_list}")


numbers = [3,6,17,4,0,-20,20,100]
sorted_numbers = sorted(numbers)
numbers.sort()
print(f"Posortowana lista {sorted_numbers}")
print(f"Posortowana lista {numbers}")


week_days_set = {"poniedziałek", "wtorek", "środa", "piątek", "sobota", "niedziela"}
week_days_set.add("czwartek")
print(week_days_set)
week_days_set.update({"czwartek"})
week_days_set = sorted(week_days_set)
print(week_days_set)



salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
}
salads["mięsna"] = ["szynka", "kurczak", "ryż", "ogórek"]
print(salads.keys())

