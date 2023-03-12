# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import math
firstCabinet = int(input('Количество человек в первом классе: '))
secondCabinet = int(input('Количество человек втором классе: '))
thirdCabinet = int(input('Количество человек в третьем классе: '))
# print('Кол-во партв в первом классе', math.ceil(firstCabinet/2))
# print('Кол-во партв во втором классе', math.ceil(secondCabinet/2))
# print('Кол-во партв в третьем классе', math.ceil(thirdCabinet/2))
# print('Общее количество парт - ', (math.ceil(firstCabinet/2) +
#       math.ceil(secondCabinet/2)+math.ceil(thirdCabinet/2)))
print('Кол-во партв в первом классе', (firstCabinet+1)//2)
print('Кол-во партв во втором классе',(secondCabinet+1)//2)
print('Кол-во партв в третьем классе',(thirdCabinet+1)//2)
print('Общее количество парт - ', (firstCabinet+1)//2 +
      (secondCabinet+1)//2+(thirdCabinet+1)//2)