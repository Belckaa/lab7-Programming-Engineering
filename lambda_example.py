from functools import reduce

input_str = input("Введіть числа через пробіл: ")
numbers = list(map(int, input_str.split()))

squares = list(map(lambda x: x ** 2, numbers))
print("Квадрати чисел:", squares)

paired_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Парні числа:", paired_numbers)

total = reduce(lambda x, y: x + y, numbers)
print("Сума всіх чисел:", total)
