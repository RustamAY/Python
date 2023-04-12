from data_create import*

def AddPerson():
    first_name = first_name_data()
    last_name = last_name_data()
    phone_number = phone_number_data()

    data = open('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\functions\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([first_name + ' ' + last_name + ' ' + phone_number, '\n'])
    data.close

def PrintData():
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\functions\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def Search():
    search_name = input('Введите данные для поиска: ')
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\functions\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)