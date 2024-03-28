#main.py

from book import Book
from library_member import LibraryMember
from transaction import Transaction

library_members = {}

library_inventory = {}

def add_library_member(name, member_id):
    if member_id not in library_members:
        library_members[member_id] = LibraryMember(name, member_id)
        print(f"Library member '{name}' with ID '{member_id}' added successfully.")
    else:
        print("Member with this ID already exists.")

def add_book(title, author, isbn, available_copies):
    if isbn not in library_inventory:
        new_book = Book(title, author, isbn, available_copies)
        library_inventory[isbn] = new_book
        print(f"Book '{title}' added to the library inventory.")
    else:
        print("Book with this ISBN already exists in the library.")

def display_library_members():
    print("\nLibrary Members:")
    for member_id, member in library_members.items():
        print(f"ID: {member_id}, Name: {member.name}")

def display_library_inventory():
    print("\nLibrary Inventory:")
    for isbn, book in library_inventory.items():
        print(f"ISBN: {isbn}, Title: {book.title}, Available Copies: {book.available_copies}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Library Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Library Members")
        print("6. Display Library Inventory")
        print("7. Check Borrowed Books By Member")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name of the library member: ")
            member_id = input("Enter member ID: ")
            add_library_member(name, member_id)

        elif choice == '2':
            title = input("Enter title of the book: ")
            author = input("Enter author of the book: ")
            isbn = input("Enter ISBN of the book: ")
            available_copies = int(input("Enter available copies of the book: "))
            add_book(title, author, isbn, available_copies)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to borrow: ")
            member_id = input("Enter member ID: ")
            if isbn in library_inventory and member_id in library_members:
                transaction = Transaction(library_inventory[isbn], library_members[member_id])
                transaction.process_transaction()
            else:
                print("Book or member not found.")

        elif choice == '4':
            isbn = input("Enter ISBN of the book to return: ")
            member_id = input("Enter member ID: ")
            if isbn in library_inventory and member_id in library_members:
                library_members[member_id].return_book(library_inventory[isbn])
            else:
                print("Book or member not found.")

        elif choice == '5':
            display_library_members()

        elif choice == '6':
            display_library_inventory()
        elif choice == '7':
            member_id = input("Enter member ID to check borrowed books: ")
            if member_id in library_members:
                borrowed_books = library_members[member_id].borrowed_books
                if borrowed_books:
                    print(f"\nBooks borrowed by '{library_members[member_id].name}':")
                    for book in borrowed_books:
                        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                else:
                    print("No books currently borrowed by this member.")
            else:
                print("Member not found.")

        elif choice == '8':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
