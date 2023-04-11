# Задача 49-1.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def AddPerson():
    first_name = input('Ввкдите фамилию: ')
    last_name = input('Ввкдите имя: ')
    phone_number = input('Введите телефон: ')
    data = open('phonebook.txt', 'w', encoding='utf-8')
    data.writelines([first_name + ' ' + last_name + ' ' + phone_number])
    data.close

AddPerson()

def PrintData():
    with open ('phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

PrintData()

def search():
    search_name = input('Введите данные для поиска: ')
    with open ('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

search()

def load_data():
    with open ('phonebook.txt', 'r', encoding='utf-8') as data:
        path = input()