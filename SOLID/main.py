import logging
from abc import ABC, abstractmethod
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Принцип SRP - Клас Book відповідає лише за зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип ISP - Інтерфейс для бібліотеки визначає тільки необхідні методи
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


# Принцип OCP та LSP - Клас Library можна розширювати, не змінюючи його реалізацію
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]

    def get_books(self) -> List[Book]:
        return self.books


# Принцип DIP - Клас LibraryManager залежить від абстракції LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if not books:
            logger.info("No books in the library.")
        else:
            for book in books:
                logger.info(str(book))


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter book year: ").strip()
            try:
                manager.add_book(title, author, int(year))
            except ValueError:
                logger.info("Year must be an integer. Please try again.")
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
