#library_member.py

class LibraryMember:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book)
            book.check_out()
            print(f"'{self.name}' has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available for checkout.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"'{self.name}' has returned '{book.title}'.")
        else:
            print(f"'{self.name}' did not borrow '{book.title}'.")