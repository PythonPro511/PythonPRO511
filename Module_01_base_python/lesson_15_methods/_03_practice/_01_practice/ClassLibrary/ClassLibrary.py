class LibraryBook:
    total_books = 0
    books = []

    def __init__(self, title, status='доступна'):
        self.title = title
        self.status = status
        LibraryBook.total_books += 1
        LibraryBook.books.append(self)

    @classmethod
    def get_total_books(cls):
        return f'Всего книг в библиотеке: {cls.total_books}'
        # return f'Всего книг в библиотеке: {len(cls.books)}'

    @classmethod
    def display_all_books(cls):
        for book in cls.books:
            print(f'Название: {book.title}/Статус: {book.status}')

    @classmethod
    def remove_book(cls, book_obj):
        if isinstance(book_obj, cls) and book_obj in cls.books:
            LibraryBook.total_books -= 1
            cls.books.remove(book_obj)
            print(f"Книга {book_obj.title} удалена")
        else:
            print(f"Книги {book_obj.title} нет в библиотеке")

    @staticmethod
    def is_available(status):
        # if status == 'доступна':
        #     return True
        return status == 'доступна'

    def change_status(self, new_status):
        self.status = new_status


