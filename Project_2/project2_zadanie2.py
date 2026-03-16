print('zadanie1')


numbers = [1,2,3,4,5,6,7,8,9,10]
cube = [number ** 3 for number in numbers if number % 2 != 0]
print(cube)


print('zadanie2')

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
only_zero_numbers = [number for number in numbers if number == 0]
print(only_zero_numbers)

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
non_zero_numbers = [number for number in numbers if number != 0]
print(non_zero_numbers)
