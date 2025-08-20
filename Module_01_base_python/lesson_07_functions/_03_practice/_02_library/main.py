from library_utils.library_utils import add_book, remove_book, list_books

if __name__ == '__main__':
    library = {}
    while True:
        command = input('Введите команду (1 - add, 2 - remove, 3 - list, 0 - exit): ').strip()

        if command == '0':
            print(f'Выход из программы')
            break
        elif command == '1':
            title = input('Введите название книги: ').strip()
            author = input('Введите автора книги: ').strip()
            print(add_book(library, title, author))
        elif command == '2':
            title = input('Введите название книги для удаления: ').strip()
            print(remove_book(library, title))

        elif command == '3':
            print('Список книг: ')
            print(list_books(library))

        else:
            print('Неизвестная команда!')
