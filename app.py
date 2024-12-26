from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

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

library = Library()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_book", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400
    library.add_book(title, author)
    return jsonify({"message": f'Book "{title}" by {author} added successfully.'})

@app.route("/delete_book", methods=["POST"])
def delete_book():
    data = request.get_json()
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    if library.delete_book(title):
        return jsonify({"message": f'Book "{title}" deleted successfully.'})
    return jsonify({"error": f'No book found with title "{title}".'}), 404

@app.route("/books")
def get_books():
    return jsonify(library.display_books())

if __name__ == "__main__":
    app.run(debug=True)
