# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

arrayLen = int(input('Введите длину масива: '))
searchNum = int(input('Введите искомеое число: '))
counter = 0
array = [randint(-10, 10) for _ in range(arrayLen)]
print(array)
for i in array:
    if searchNum == i:
        counter += 1
print(counter)