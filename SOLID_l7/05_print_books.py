from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass



class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.title}\n{book.author}\n{book.content[:4]}"


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formater: BaseFormatter):
        self.formater = formater
    def get_book(self, book: Book):
        return self.formater.format(book)


book = Book("a", "a", "some_content")
pa = Printer(PaperFormatter())
pb = Printer(WebFormatter())
print(pa.get_book(book))
print(pb.get_book(book))
