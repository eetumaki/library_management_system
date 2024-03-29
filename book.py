#book.py

class Book:
    def __init__(self, title: str, author: str, isbn: str, available_copies: int):
        self.title = title
        self.author = author
        self.isbn = isbn # id of the book
        self.available_copies = available_copies # Number of available copies of the book
        self.total_copies = available_copies # Total number of copies of the book

    # Method to check out a book
    def check_out(self):
        if self.available_copies > 0: # If there are available copies
            self.available_copies -= 1 # Decrease the number of available copies by 1
            print(f"Succesfully checked out '{self.title}'.")
            return True
        else: # If no available copies
            print(f"Sorry, '{self.title}' is not available for checkout.")
            return False

    # Method to return a book
    def return_book(self):
        self.available_copies += 1 # Increase number of available copies by 1
        print(f"Book '{self.title}' has been returned.")