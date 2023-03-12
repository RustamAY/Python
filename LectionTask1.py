# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
# Input:
# n = 700км/д
# s= 750км
# Output:
# 2


# import math
# n = int (input ('Количество км в день: '))
# s = int (input ('Количество км: '))
# print(math.ceil(s/n))

#решение без math
n = int (input ('Количество км в день: '))
s = int (input ('Количество км: '))
day = (s+(n-1))//n
print(f"{day} - столько дней будет ехать машина")