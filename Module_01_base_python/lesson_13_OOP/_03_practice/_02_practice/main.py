from classes.ClassBook import Book
from classes.ClassLibrary import Library

if __name__ == '__main__':
    library = Library()
    while True:
        command = input("Введите команду (1 - add book, 2 - change status, 3 - show, 0 - exit): ").strip().lower()
        if command == "1":
            title = input('Введите название книги: ').strip()
            author = input('Введите автора книги: ').strip()
            book = Book(title, author)
            library.add_book(book)
            print(f"Книга '{title}' добавлена в библиотеку.")
        elif command == '2':
            title = input('Введите название книги: ').strip()
            new_status = input("Введите новый статус (например, 'в наличии' или 'выдана'): ").strip()
            print(library.change_status(title, new_status))
        elif command == '3':
            library.show_books()
        elif command == '0':
            print(f'Программа завершена.')
            break
        else:
            print('Неизвестная команда. Попробуйте снова.')