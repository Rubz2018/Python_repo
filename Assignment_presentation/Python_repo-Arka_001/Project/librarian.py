from book import Book
from user import User

class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.books = []

    def add_book(self, book_id, title, author, copies):
        new_book = Book(book_id, title, author, copies)
        self.books.append(new_book)
        print(f"Added book: {title}")

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]
        print(f"Removed book ID {book_id}")

    def display_books(self):
        for book in self.books:
            print(book.display_info())
