def add_book(library, title, author):
    if title in library:
        return "Книга уже существует"
    library[title] = author
    return f'Книга {title}, автора {author} успешно добавлена'


def remove_book(library, title):
    if title in library:
        del library[title]
        return f'Книга {title} успешно удалена.'
    return f'Книга не найдена.'


def list_books(library):
    if not library:
        return "Библиотека пуста"
    return '\n'.join([f'{title} - {author}' for title, author in library.items()])
