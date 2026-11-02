class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False




class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        for book in self.books:
            if book.book_id == book_id:
                raise ValueError("Book ID already exists")
        book = Book(book_id, title, author)
        self.books.append(book)
        return book

    
    def search_book(self, keyword):
        keyword = keyword.lower()
        results = []
        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        return results

    
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    raise ValueError("Book is already issued")
                book.is_issued = True
                return book
        raise ValueError("Book not found")


    
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    raise ValueError("Book was not issued")
                book.is_issued = False
                return book
        raise ValueError("Book not found")

    
    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    raise ValueError("Cannot delete an issued book")
                self.books.remove(book)
                return book
        raise ValueError("Book not found")