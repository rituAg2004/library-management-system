import pytest

from library import Library


def test_add_book():
    lib = Library()
    book = lib.add_book(1, "Python Basics", "Ritu")
    assert len(lib.books) == 1
    assert book.title == "Python Basics"
    assert book.is_issued is False


def test_add_duplicate_id_raises_error():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    with pytest.raises(ValueError, match="Book ID already exists"):
        lib.add_book(1, "Another Book", "Someone")


def test_search_book_finds_match_case_insensitive():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    lib.add_book(2, "Java Guide", "Amit")
    results = lib.search_book("PYTHON")
    assert len(results) == 1
    assert results[0].title == "Python Basics"


def test_search_book_no_match_returns_empty_list():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    assert lib.search_book("xyz") == []


def test_issue_book_marks_book_as_issued():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    book = lib.issue_book(1)
    assert book.is_issued is True


def test_issue_already_issued_book_raises_error():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    lib.issue_book(1)
    with pytest.raises(ValueError, match="Book is already issued"):
        lib.issue_book(1)


def test_issue_nonexistent_book_raises_error():
    lib = Library()
    with pytest.raises(ValueError, match="Book not found"):
        lib.issue_book(99)


def test_return_book_marks_book_as_available():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    lib.issue_book(1)
    book = lib.return_book(1)
    assert book.is_issued is False


def test_return_book_that_was_not_issued_raises_error():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    with pytest.raises(ValueError, match="Book was not issued"):
        lib.return_book(1)


def test_return_nonexistent_book_raises_error():
    lib = Library()
    with pytest.raises(ValueError, match="Book not found"):
        lib.return_book(99)


def test_delete_book_removes_book_from_library():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    lib.delete_book(1)
    assert len(lib.books) == 0


def test_delete_issued_book_raises_error():
    lib = Library()
    lib.add_book(1, "Python Basics", "Ritu")
    lib.issue_book(1)
    with pytest.raises(ValueError, match="Cannot delete an issued book"):
        lib.delete_book(1)
    assert len(lib.books) == 1


def test_delete_nonexistent_book_raises_error():
    lib = Library()
    with pytest.raises(ValueError, match="Book not found"):
        lib.delete_book(99)
