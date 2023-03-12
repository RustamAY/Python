# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите число: '))
sum = 0
while number > 0:
    i = number % 10
    number = number//10
    sum = sum + i
print(f"Сумма чисел = {sum}")