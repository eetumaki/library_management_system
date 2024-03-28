#transaction.py

class Transaction:
    def __init__(self, book: str, library_member: str):
        self.book = book
        self.library_member = library_member

    def process_transaction(self):
        if self.book.available_copies > 0:
            self.library_member.borrow_book(self.book)
        else:
            print(f"Sorry, '{self.book.title}' is not available for checkout at the moment.")