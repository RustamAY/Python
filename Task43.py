# Задача 43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод:               Вывод:
# 1 2 3 2 3           2

from random import randint

arr_size = randint(5, 9)
print(arr_size)

array = [randint(1, 10) for _ in range(arr_size)]
print(array)

count = 0
for i in range(arr_size-1):
    for j in range(i+1, arr_size):
        if array [i] == array[j]:
            count += 1
print(count)