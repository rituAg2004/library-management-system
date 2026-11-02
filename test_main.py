from library import Book
from main import format_book


def test_format_book_available():
    book = Book(1, "Python Basics", "Ritu")
    assert format_book(book) == "[1] Python Basics by Ritu (Available)"


def test_format_book_issued():
    book = Book(2, "Java Guide", "Amit")
    book.is_issued = True
    assert format_book(book) == "[2] Java Guide by Amit (Issued)"
