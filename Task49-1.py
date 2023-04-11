# Задача 49-1.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

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
        text_data = data.read().splitlines()
        path = input('Введите путь к файлу: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in text_data:
                    data.write(line)

def Ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод консоль''')
    user_input = input('Выберете действие: ')
    if user_input == '1':
        AddPerson()
    elif user_input == '2':
        Search()
    elif user_input == '3':
        LoadData()
    elif user_input == '4':
        PrintData()

def main():
    Ui()

if __name__ == "__main__":
    main()