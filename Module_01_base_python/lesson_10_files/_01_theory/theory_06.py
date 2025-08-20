def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('Файл не найден!')
    except IOError:
        print("Ошибка ввода-вывода.")


if __name__ == '__main__':
    my_filepath = r'files\example.txt'
    read_file(my_filepath)
