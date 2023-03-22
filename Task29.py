# Задача 29
# 1) Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем
# (число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца
# сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились
# к Вам, студентам
# 2) Задача – «На вход программе подаются цифры,как только пользователь введёт 0 ввод прекращается.
# Вывести наибольший элемент получившейся последовательности».
# Есть два кода с ошибками, нужно определить где ошибок меньше.
# Примечание: Программные коды на следующих слайдах

# Петя:
n = int(input())
max_number = -1
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)

# Ваня:
n = int(input())
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)

print("Honey, what's your hurry", end='?')

print("Remember not to get too close to stars", end=="")

print("Remember not to get too close to stars", "They're never gonna give you love like ours", sepp=" ")

print("Told you not to worry", "But maybe that's a lie", sep=' :) ')

print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')
