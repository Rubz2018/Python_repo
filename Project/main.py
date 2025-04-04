from librarian import Librarian
from user import Member
from library import Library

# Initialize Library System
lib = Library()
librarian = Librarian(1, "Alice")

# Librarian adds books
librarian.add_book(101, "Python Basics", "John Doe", 3)
librarian.add_book(102, "AI with Python", "Jane Smith", 2)

# Member borrows a book
member = Member(201, "Bob")
book = lib.find_book(101)
if book:
    member.borrow_book(book)

# Display books
librarian.display_books()
