# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNum = int(input('Введите номер билета: '))
if ticketNum < 99999 or ticketNum > 999999:
    print('Билет должен иметь 6 цифр')
else:
    firstThreeNum = ticketNum//1000
    secondThreeNum = ticketNum % 1000

    sum = 0
    while firstThreeNum > 0:
        i = firstThreeNum % 10
        firstThreeNum = firstThreeNum//10
        sum = sum + i

    sum2 = 0
    while secondThreeNum > 0:
        i = secondThreeNum % 10
        secondThreeNum = secondThreeNum//10
        sum2 = sum2 + i

    if sum == sum2:
        print(f'{ticketNum} -> yes')
    else:
        print(f'{ticketNum} -> no')
