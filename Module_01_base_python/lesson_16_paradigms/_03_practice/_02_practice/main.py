from LibraryClasses.LibraryClasses import Book, Journal, Audiobook

if __name__ == '__main__':
    library = [
        Book("Мастер и Маргарита"),
        Journal("National Geographic"),
        Audiobook("Война и мир", 1200)
    ]

    for item in library:
        print(item.get_info())
