# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def Exponent(numA, numB):
    if numB == 1:
        return numA
    if numB != 1:
        return (numA * Exponent(numA, numB - 1))

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
exp = Exponent(a, b)
print(exp)