from typing import List, Union


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def find_book(self, title: str) -> Union[Book, str]:
        try:
            return [b for b in self.books if b.title == title][0]
        except IndexError:
            return "Book does not exist"


book1 = Book("Witches abroad", "Terry Pratchett")
book2 = Book("1984", "George Orwell")
book3 = Book("Harry Potter and philosopher stone", "J.K.Rollings")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.find_book("198re4"))