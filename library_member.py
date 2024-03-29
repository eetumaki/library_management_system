#library_member.py
from user import User

class LibraryMember(User):
    def __init__(self, name: str, member_id: str):
        super().__init__(name) # Call the constructor of the parent class
        self.member_id = member_id # Member id of library member
        self.borrowed_books = [] # List of books borrowed by library member

    # Method to borrow a book
    def borrow_book(self, book):
        if book.available_copies > 0: # If there are available books
            self.borrowed_books.append(book) # Add the book to the list of borrowed books
            book.check_out() # Check out the book
            print(f"'{self.name}' has borrowed '{book.title}'.")
        else: # If there is no available books
            print(f"Sorry, '{book.title}' is not available for checkout.")

    # Method to return a book
    def return_book(self, book):
        if book in self.borrowed_books: # If the book is in the list of borrowed books
            self.borrowed_books.remove(book) # Remove the book from the list
            book.return_book() # return the book
            print(f"'{self.name}' has returned '{book.title}'.")
        else: # If the book is not in the list of borrowed books
            print(f"'{self.name}' did not borrow '{book.title}'.")