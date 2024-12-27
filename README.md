## 📚 Library Management System

A web-based Library Management System that allows users to manage book information, including title, author, and description. Users can add, edit, delete, search, and sort books in the library.

## 🌟 Features

- **Add Books**: Add new books to the library by providing a title, author name, and an optional description.
- **Edit Books**: Modify the details of existing books in the library.
- **Delete Books**: Remove books from the library.
- **Search Books**: Find books by their title.
- **Sort Books**: Organize the book list by title or author name.
- **View All Books**: Display the complete list of books in the library.

## 🖼️ User Interface

The application features a clean and vibrant UI with:
- A responsive design
- Dropdown menus for sorting
- Interactive buttons for various actions

![Screenshot 2024-12-27 132240](https://github.com/user-attachments/assets/196fb379-6945-4725-a9bc-07e429b368b0)


## 🚀 Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Database**: SQLite (or other backend-supported database)

## 🛠️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   
2. **Set up a Virtual Environment (Optional but recommended)**:
   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   ```bash
    pip install -r requirements.txt
   
4. **Run the Application:**
    ```bash
    flask run

5. **Access the Application: Open your browser and navigate to http://127.0.0.1:5000.**


## 💾 Usage

Fill in the book details (Title, Author, Description) in the respective input fields.
Use the buttons for various actions:
**Add Book:** Adds the entered book to the library.
**Edit Book:** Updates details for the selected book.
**Delete Book:** Removes a book from the list.
**Clear Fields:** Clears all input fields.
**Search:** Finds books by their title.
**Sort by Title/Author:** Arranges the book list by the selected criteria.
**View All Books:** Displays all the books in the library.

## 📂 Project Structure
      
        library-management-system/
        ├── static/
        │   ├── css/
        │   │   └── style.css
        │   ├── js/
        │   │   └── app.js
        ├── templates/
        │   ├── index.html
        │   └── base.html
        ├── app.py
        ├── requirements.txt
        ├── README.md


## 🤝 Contribution Guidelines
1. Fork the repository and create your branch:
   ```bash
    git checkout -b feature/your-feature-name
2. Commit your changes:
    ```bash
    git commit -m "Add your feature description"
3. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
4. Create a pull request.
   

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.








