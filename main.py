#main.py
from book import Book
from library_member import LibraryMember
from transaction import Transaction

from book import Book
from library_member import LibraryMember
from transaction import Transaction

# Create some books
book1 = Book("Python Programming", "John Smith", "978-0134465679", 5)
book2 = Book("Introduction to Data Science", "Jane Doe", "978-0596520990", 3)

# Create a library member
member1 = LibraryMember("Alice", "M001")

# Test borrowing and returning books
transaction1 = Transaction(book1, member1)
transaction1.process_transaction()

transaction2 = Transaction(book2, member1)
transaction2.process_transaction()

member1.return_book(book1)
member1.return_book(book2)