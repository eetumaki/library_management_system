#book.py

class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
        self.total_copies = available_copies

    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Succesfully checked out '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available for checkout.")

    def return_book(self):
        self.available_copies += 1
        print(f"Book '{self.title}' has been returned.")