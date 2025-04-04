class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.copies > 0:
            self.borrowed_books.append(book.title)
            book.copies -= 1
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available.")

    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.copies += 1
            print(f"{self.name} returned {book.title}")
        else:
            print("Book not borrowed.")
