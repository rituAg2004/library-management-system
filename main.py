from library import Library

DATA_FILE = "books.json"


def print_menu():
    print()
    print("=== Library Management System ===")
    print("1. Add book")
    print("2. Search book")
    print("3. Issue book")
    print("4. Return book")
    print("5. Delete book")
    print("6. List all books")
    print("7. Exit")


def add_book_flow(library):
    try:
        book_id = int(input("Book ID: ").strip())
    except ValueError:
        print("Book ID must be a number.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        library.add_book(book_id, title, author)
        print("Book added.")
    except ValueError as e:
        print(f"Error: {e}")


def format_book(book):
    status = "Issued" if book.is_issued else "Available"
    return f"[{book.book_id}] {book.title} by {book.author} ({status})"


def search_book_flow(library):
    keyword = input("Search keyword: ").strip()
    results = library.search_book(keyword)
    if not results:
        print("No books found.")
        return
    for book in results:
        print(format_book(book))


def read_book_id():
    try:
        return int(input("Book ID: ").strip())
    except ValueError:
        print("Book ID must be a number.")
        return None


def issue_book_flow(library):
    book_id = read_book_id()
    if book_id is None:
        return
    try:
        library.issue_book(book_id)
        print("Book issued.")
    except ValueError as e:
        print(f"Error: {e}")


def return_book_flow(library):
    book_id = read_book_id()
    if book_id is None:
        return
    try:
        library.return_book(book_id)
        print("Book returned.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_book_flow(library):
    book_id = read_book_id()
    if book_id is None:
        return
    try:
        library.delete_book(book_id)
        print("Book deleted.")
    except ValueError as e:
        print(f"Error: {e}")


def list_books_flow(library):
    if not library.books:
        print("Library is empty.")
        return
    for book in library.books:
        print(format_book(book))


def main():
    library = Library()
    library.load_from_file(DATA_FILE)
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_book_flow(library)
        elif choice == "2":
            search_book_flow(library)
        elif choice == "3":
            issue_book_flow(library)
        elif choice == "4":
            return_book_flow(library)
        elif choice == "5":
            delete_book_flow(library)
        elif choice == "6":
            list_books_flow(library)
        elif choice == "7":
            library.save_to_file(DATA_FILE)
            print("Books saved.")
            print("Goodbye!")
            break
        else:
            print("Option not implemented yet.")


if __name__ == "__main__":
    main()
