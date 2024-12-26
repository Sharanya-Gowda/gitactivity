import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import json
import os

# Library class to manage books
class Library:
    def __init__(self):
        self.books = []
        self.load_books_from_file()

    def add_book(self, title, author):
        """Add a book to the library"""
        book = {"Title": title, "Author": author}
        self.books.append(book)
        self.save_books_to_file()

    def delete_book(self, title):
        """Delete a book from the library"""
        for book in self.books:
            if book["Title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books_to_file()
                return True
        return False

    def display_books(self):
        """Return all books in the library"""
        return self.books

    def save_books_to_file(self):
        """Save the current list of books to a JSON file"""
        if not os.path.exists('data'):
            os.mkdir('data')
        with open("data/books.json", "w") as file:
            json.dump(self.books, file)

    def load_books_from_file(self):
        """Load books from a JSON file"""
        if os.path.exists("data/books.json"):
            with open("data/books.json", "r") as file:
                self.books = json.load(file)
        else:
            self.books = []  # If file doesn't exist, start with an empty list

# Function to handle Add Book
def add_book():
    title = entry_title.get()
    author = entry_author.get()

    if not title or not author:
        messagebox.showwarning("Input Error", "Please fill both title and author fields.")
        return

    library.add_book(title, author)
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    refresh_books_list()
    messagebox.showinfo("Success", f'Book "{title}" by {author} added successfully.')

# Function to handle Delete Book
def delete_book():
    title = entry_title.get()

    if not title:
        messagebox.showwarning("Input Error", "Please enter the title of the book to delete.")
        return

    if library.delete_book(title):
        refresh_books_list()
        messagebox.showinfo("Success", f'Book "{title}" deleted successfully.')
    else:
        messagebox.showwarning("Not Found", f'No book found with title "{title}".')

# Function to refresh the displayed book list
def refresh_books_list():
    books_listbox.delete(0, tk.END)
    books = library.display_books()
    for book in books:
        books_listbox.insert(tk.END, f'{book["Title"]} by {book["Author"]}')

# Function to search books by title
def search_book():
    search_term = entry_search.get().lower()
    if not search_term:
        messagebox.showwarning("Input Error", "Please enter a title to search.")
        return

    books_listbox.delete(0, tk.END)
    books = library.display_books()
    found_books = [book for book in books if search_term in book["Title"].lower()]

    if not found_books:
        messagebox.showinfo("No Results", "No books found matching that title.")
    else:
        for book in found_books:
            books_listbox.insert(tk.END, f'{book["Title"]} by {book["Author"]}')

# Function to view all books
def view_all_books():
    refresh_books_list()

# Set up the main window
window = tk.Tk()
window.title("Library Management System")

# Set the window icon (optional)
window.iconphoto(False, PhotoImage(file="/home/lab1/git/Library_Management_System/assets/icon.png"))

# Set up GUI elements
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

# Title entry
label_title = tk.Label(frame, text="Book Title:")
label_title.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_title = tk.Entry(frame)
entry_title.grid(row=0, column=1, padx=5, pady=5)

# Author entry
label_author = tk.Label(frame, text="Author Name:")
label_author.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_author = tk.Entry(frame)
entry_author.grid(row=1, column=1, padx=5, pady=5)

# Add Book Button
add_button = tk.Button(frame, text="Add Book", command=add_book)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Delete Book Button
delete_button = tk.Button(frame, text="Delete Book", command=delete_book)
delete_button.grid(row=3, column=0, columnspan=2, pady=10)

# Search Book Entry
label_search = tk.Label(window, text="Search Book by Title:")
label_search.pack(pady=5)
entry_search = tk.Entry(window)
entry_search.pack(pady=5)

# Search Button
search_button = tk.Button(window, text="Search", command=search_book)
search_button.pack(pady=5)

# View All Books Button
view_all_button = tk.Button(window, text="View All Books", command=view_all_books)
view_all_button.pack(pady=10)

# Books Listbox
label_books = tk.Label(window, text="Books in Library:")
label_books.pack(pady=5)
books_listbox = tk.Listbox(window, height=10, width=50)
books_listbox.pack(pady=5)

# Display Logo (Optional)
logo = PhotoImage(file="/home/lab1/git/Library_Management_System/assets/logo.png")  # Load the logo image
logo_label = tk.Label(window, image=logo)
logo_label.pack(pady=10)

# Create a Library instance
library = Library()

# Refresh book list initially
refresh_books_list()

# Run the application
window.mainloop()
