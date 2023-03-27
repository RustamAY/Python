# Задача 37.
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def numRevers(num):
    if num <= 0:
        return
    num_sequen = int(input('Ведите последовательность: '))
    numRevers(num-1)
    print(num_sequen, end=" ")


num = int(input('Ведите число: '))
num_revers = numRevers(num)
print(num_revers)