from LibraryClasses.LibraryClassesMy import Book, Journal, Audiobook

if __name__ == '__main__':
    library = [
        Book("Мастер и Маргарита", "М.А.Булгаков"),
        Journal("National Geographic"),
        Audiobook("Война и мир", "Л.Н.Толстой", 1200)
    ]

    for item in library:
        print(item.get_info())
