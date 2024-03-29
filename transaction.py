#transaction.py

class Transaction:
    def __init__(self, book: str, library_member: str):
        self.book = book # The book involved in the transaction
        self.library_member = library_member # The library member involved in the transaction

    # Method to process the transaction
    def process_transaction(self):
        if self.book.available_copies > 0: # If there are available copies of the book
            self.library_member.borrow_book(self.book) # Library member borows the book
        else: # If no available copies of book
            print(f"Sorry, '{self.book.title}' is not available for checkout at the moment.")