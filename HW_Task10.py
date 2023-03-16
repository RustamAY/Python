# Задача 10
# Пользователь вводит число n. На следующих строках нужно вводить 1 или 0,
# в ответе вывести количество наименее встречающихся из них
# (т.е либо количество 0 либо 1, в зависимости от того, кого меньше)

from random import randint

number = int(input('Введите натуральное число: '))
if number < 0:
    print('Введено число меньше нуля!')
else:
    zero = 0
    one = 0
    for i in range(number):
        rndNumber = randint(0, 1)
        print(rndNumber, end=' ')
        if rndNumber == 0:
            zero += 1
        else:
            one += 1
print()
if zero < one:
    print(zero)
else:
    print(one)
