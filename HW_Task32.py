# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# low_point = int(input())
# top_point = int(input())
# list_2 = []
# for i in range(len(list_1)):
#     if low_point <= list_1[i] <= top_point:
#         list_2.append(i)
# print(list_2)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split()
    syllable_counts = [count_vowels(phrase.replace('-', '')) for phrase in phrases]
    if len(set(syllable_counts)) == 1:
        print("Param pam pam")
    else:
        print("Rhythm is not all right")

poem = input("Enter the poem: ")
check_rhythm(poem)