class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def change_status(self, title, new_status):
        for book in self.books:
            if book.title == title:
                book.status = new_status
                return f"Статус книги '{title}' изменён на '{new_status}'."
        return f"Книга '{title}' не найдена."

    def show_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print(f'Список книг в библиотеке:')
            for book in self.books:
                print(f'{book.title} ({book.author}) - {book.status}')
