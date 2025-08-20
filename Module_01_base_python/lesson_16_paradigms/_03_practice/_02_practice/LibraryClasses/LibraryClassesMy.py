class LibraryItem:
    def __init__(self, title):
        self.title = title

    def get_info(self):
        return f'Материал: {self.title}'


class Book(LibraryItem):

    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def get_info(self):
        return f'Книга: {self.title}. Автор: {self.author}'


class Journal(LibraryItem):
    def get_info(self):
        return f'Журнал: {self.title}'


class Audiobook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def get_info(self):
        return f'Аудиокнига: {self.title}. Автор: {self.author}. Длительность: {self.duration} минут'


