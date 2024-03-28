#main.py
from book import Book
from library_member import LibraryMember
from transaction import Transaction

library_inventory = {}

def add_book_to_inventory(title, author, isbn, available_copies):
    if isbn in library_inventory:
        print("Book already exists. Updating existing entry...")
        library_inventory[isbn].available_copies += available_copies
    else:
        print("Adding new book to inventory...")
        new_book = Book(title, author, isbn, available_copies)
        library_inventory[isbn] = new_book

add_book_to_inventory("Python Programming", "John Smith", "978-0134465679", 5)
add_book_to_inventory("Introduction to Data Science", "Jane Doe", "978-0596520990", 3)

# Display library inventory
print("Library Inventory:")
for isbn, book in library_inventory.items():
    print(f"ISBN: {isbn}, Title: {book.title}, Available Copies: {book.available_copies}")

# Continue with the rest of the logic...