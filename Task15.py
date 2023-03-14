# Задача 15
# Пользователь вводит одно число N. Далее идут N чисел, записанных на новой строчке каждое.
# Вывести максимальное и минимальное (циклы)
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

num = int(input('Введите натуральное число: '))
if num <0:
    print('Введите натуральное число!')
else:
    min = 20
    max = 0
    for _ in range(num):
        rndNum=randint(1,20)
        print(rndNum)
        if max<rndNum:
            max = rndNum
        if min>rndNum:
            min = rndNum
print(f'min = {min} max={max}')