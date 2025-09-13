class DBConnection:

    def __enter__(self):
        print(f'Открываем соединение с базой данных')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с базой данных')
        if exc_type:
            print(f'Произошла ошибка: {exc_val}')


class FileWriter:
    def __enter__(self):
        self.file = open(r'example_files\log.txt', 'a', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f'Ошибка в файле: {exc_val}')
        return True


if __name__ == '__main__':
    with DBConnection() as db, FileWriter() as file:
        file.file.write('Запись в лог файл\n')
        print('Работаем с базой данных.')
        print('Еще, работаем с базой данных.')
