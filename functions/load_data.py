

def LoadData():
    with open ('C:\\Users\\RustamYunusov\\Desktop\\GB Course\\analytics\\Python\\functions\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read()
        path = input('Введите путь к файлу: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line not in text_data:
                    data.write(line)