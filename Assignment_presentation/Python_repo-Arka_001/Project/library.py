import json
from book import Book
from user import Member
from librarian import Librarian

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            with open("database.json", "r") as file:
                data = json.load(file)
                for book in data:
                    self.books.append(Book(**book))
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("database.json", "w") as file:
            json.dump([book.__dict__ for book in self.books], file)

    def find_book(self, book_id):
        return next((book for book in self.books if book.book_id == book_id), None)
