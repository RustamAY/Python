# Задача 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

from random import randint

# listOfNumber = []
# for _ in range(randint(5,10)):
#     number = randint(-10, 10)
#     print(number, end=' ')
#     listOfNumber.append(number)

listOfNumber = [randint(-10, 10) for _ in range(randint(5,10))]
set_1 = set(listOfNumber)
print(listOfNumber, end =' ')
print()
print(len(set_1))
# print(len(set(input().split()))) - # решение задачи в одну строку
