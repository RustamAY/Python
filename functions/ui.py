import os
from logger import *
from load_data import LoadData

def UserInterface():
    os.system('cls')
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод консоль
5 - Выход''')
    user_input = input('Выберете действие: ')
    while user_input != '5':
        if user_input == '1':
            AddPerson()
        elif user_input == '2':
            Search()
        elif user_input == '3':
            LoadData()
        elif user_input == '4':
            PrintData()
        else:
            print('Вы ввели не корректный вариант, попробуйте еще раз!')
        os.system('cls')
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод консоль
5 - Выход''')
        user_input = input('Выберете действие: ')