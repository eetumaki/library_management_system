from tkinter import *
from tkinter import ttk
import sys
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
        print("Book with this ISBN already exists in the library.")

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


class StoudtRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, output):
        self.text_widget.config(text=self.text_widget.cget('text') + output)


root = Tk()
root.configure(bg="light blue")  # Set background color for root window
root.title("Library Management System")
frm = ttk.Frame(root, padding=150)
frm.pack(fill="none", expand=True)
frm.grid()

# Set background color for the frame
frm.configure(style="My.TFrame")
root.style = ttk.Style()
root.style.configure("My.TFrame", background="light blue")
root.style.configure("My.TLabel", background='light blue')
root.style.configure("My.TButton", background='light cyan')


def button_press():
    input_data = input_field.get()
    if input_data == '1':
        open_choice_1()


def open_choice_1():

   top= Toplevel(frm)
   top.geometry("750x250")
   top.title("Add Library Member")
   Label(top, text= "Add a library member!", font=('Mistral 14 bold')).grid(column=0,row=0, pady=105, padx=50)
   data = Entry(top, width=25)
   data.grid(column=1, row=0)
   user_id = str(len(library_members) + 1)
   Button(top, width=3, text="ok", command=lambda: [add_library_member(data.get(), user_id), top.destroy()] ).grid(column=2, row=0)
   
   


ttk.Label(frm, text="Menu", style="My.TLabel").grid(column=0, row=0)
input_field = ttk.Entry(frm, width=7)
input_field.grid(column=1, row=0)
input_button = ttk.Button(frm, text="ok",width=3, style="My.TButton", command=button_press).grid(column=2, row=0)

ttk.Label(frm, text=' ', style="My.TLabel").grid(column=0, row=1)

ttk.Label(frm, text="1. Add Library Member", style="My.TLabel").grid(column=0, row=2, sticky=W)
ttk.Label(frm, text="2. Add Book", style="My.TLabel").grid(column=0, row=3, sticky=W)
ttk.Label(frm, text="3. Borrow Book", style="My.TLabel").grid(column=0, row=4, sticky=W)
ttk.Label(frm, text="4. Return Book", style="My.TLabel").grid(column=0, row=5, sticky=W)
ttk.Label(frm, text="5. Display Library Members", style="My.TLabel").grid(column=0, row=6, sticky=W)
ttk.Label(frm, text="7. Check Borrowed Books By Member", style="My.TLabel").grid(column=0, row=7, sticky=W)
ttk.Label(frm, text="7. Borrow Book", style="My.TLabel").grid(column=0, row=8, sticky=W)

ttk.Label(frm, text=' ', style="My.TLabel").grid(column=0, row=9)

output_field = ttk.Label(frm, text='', wraplength=600)
output_field.grid(column=0, row=10)


sys.stdout = StoudtRedirector(output_field)


root.mainloop()
