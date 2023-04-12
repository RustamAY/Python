# Задача 49-1.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os

def AddPerson():
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    phone_number = input('Введите телефон: ')
    data = open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([first_name + ' ' + last_name + ' ' + phone_number, '\n'])
    data.close

def PrintData():
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def Search():
    search_name = input('Введите данные для поиска: ')
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def LoadData():
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read()
        path = input('Введите путь к файлу: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)

def DeleteData():
    delete_data = input('Ввкдите данные для удаления: ')
    with open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i in range(len(d)):
            if delete_data in d[i]:
                del d[i]
    with open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'w', encoding='utf-8') as data:
        print(d)
        for i in d:
            data.write(i)

def ChangeData():
    change_data = input('Какие данные хотите изменить: ')
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    phone_number = input('Введите телефон: ')

    with open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
    for i in range(len(d)):
        if change_data in d[i]:
            d[i] = first_name + ' ' + last_name + ' ' + phone_number + '\n'

    with open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\Files\\phonebook.txt', 'w', encoding='utf-8') as data:
        for line in d:
            data.write(line)



def Ui():
    os.system('cls')
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод консоль
5 - изменить
6 - удалить
7 - Выход''')
    user_input = input('Выберете действие: ')
    while user_input != '7':
        if user_input == '1':
            AddPerson()
        elif user_input == '2':
            Search()
        elif user_input == '3':
            LoadData()
        elif user_input == '4':
            PrintData()
        elif user_input == '5':
            ChangeData()
        elif user_input == '6':
            DeleteData()
        else:
            print('Вы ввели не корректный вариант, попробуйте еще раз!')
        os.system('cls')
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод консоль
5 - изменить
6 - удалить
7 - Выход''')
        user_input = input('Выберете действие: ')

def main():
    Ui()

if __name__ == "__main__":
    main()