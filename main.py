#main.py

from book import Book
from library_member import LibraryMember
from transaction import Transaction

# Dictionaries to store library members and books
library_members = {}
library_inventory = {}

# Function to add a library member
def add_library_member(name, member_id):
    if member_id not in library_members: # If the member id is not already in use
        library_members[member_id] = LibraryMember(name, member_id) # Create a new LibraryMember and add it to the dictionary
        print(f"Library member '{name}' with ID '{member_id}' added successfully.")
    else:
        print("Member with this ID already exists.") # If the member id is already in use, print an error message

# Function to add a book to the library
def add_book(title, author, isbn, available_copies):
    if isbn not in library_inventory: # If the isbn is not already in use
        new_book = Book(title, author, isbn, available_copies) # Create a new Book and add it to the dictionary
        library_inventory[isbn] = new_book
        print(f"Book '{title}' added to the library inventory.")
    else:
        print("Book with this ISBN already exists in the library.") # If the isbn is already in use, print an error message

# Function to display all library members
def display_library_members():
    print("\nLibrary Members:")
    for member_id, member in library_members.items(): # For each member in dictionary
        print(f"ID: {member_id}, Name: {member.name}") # Print members name and id

# Function to display all books
def display_library_inventory():
    print("\nLibrary Inventory:")
    for isbn, book in library_inventory.items(): # For each book in dictionary
        print(f"ISBN: {isbn}, Title: {book.title}, Available Copies: {book.available_copies}") # print books isbn, title and number of available copies

# Main function
def main():
    while True: # Loop until user chooses to exit
        print("\nMenu:") # Print the menu
        print("1. Add Library Member")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Library Members")
        print("6. Display Library Inventory")
        print("7. Check Borrowed Books By Member")
        print("8. Exit")

        choice = input("Enter your choice: ") # Get users choice

        """ Depending on the users choice, call the appropriate function or print an error message """

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
            if isbn in library_inventory and member_id in library_members: # If book and member exist
                transaction = Transaction(library_inventory[isbn], library_members[member_id]) # Create new Transaction
                transaction.process_transaction() # process transaction
            else:
                print("Book or member not found.") # If book or member don't exist, print an error message

        elif choice == '4':
            isbn = input("Enter ISBN of the book to return: ")
            member_id = input("Enter member ID: ")
            if isbn in library_inventory and member_id in library_members: # If book and member exist
                library_members[member_id].return_book(library_inventory[isbn]) # Member returns the book
            else:
                print("Book or member not found.")

        elif choice == '5':
            display_library_members() # Display all library members

        elif choice == '6':
            display_library_inventory() # Display all books


        elif choice == '7':
            member_id = input("Enter member ID to check borrowed books: ")
            if member_id in library_members: # If the member exists
                borrowed_books = library_members[member_id].borrowed_books # Get list of books borrowed by member
                if borrowed_books: # If member has borrowed any books
                    print(f"\nBooks borrowed by '{library_members[member_id].name}':")
                    for book in borrowed_books: # For each book borrowed
                        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}") # Print the books title, author and isbn
                else:
                    print("No books currently borrowed by this member.") # If member hasn't borrowed any books, print an error message
            else:
                print("Member not found.") # If the member doesn't exist, print an error message

        elif choice == '8':
            print("Exiting program.") # Exit the program
            break

        else:
            print("Invalid choice. Please try again.") # If the users choice is invalid, print an error message


# If the file is being run directly, call the main function
if __name__ == "__main__":
    main()
