from ClassLibrary.ClassLibrary import LibraryBook

if __name__ == '__main__':
    book1 = LibraryBook("Мастер и Маргарита")
    book2 = LibraryBook("1984")

    if LibraryBook.is_available(book1.status):
        print("Доступна")
    else:
        print("Недоступна")
    book1.change_status("в аренде")
    if LibraryBook.is_available(book1.status):
        print("Доступна")
    else:
        print("Недоступна")
    print()
    print(LibraryBook.get_total_books())
    LibraryBook.display_all_books()
    LibraryBook.remove_book(book1)
    print()
    LibraryBook.display_all_books()
    print(LibraryBook.get_total_books())

