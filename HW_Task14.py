# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите натуральное число: '))
if number < 0:
    print('Ввели отрицательное число!')
else:
    square = 1
    while square < number:
      print(square, end=' ')
      square = square * 2