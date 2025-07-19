# Mini Project : Library Management System

    # In this mini-project, we’ll simulate a Library Management System where we can:
        # Add new books to the library.
        # Issue books to users.
        # Return books.
        # Track the availability of books.

    # Key Concepts Covered:
        # Classes and objects.
        # Methods for adding, issuing, and returning books.
        # Attributes to represent book details. 
        # Use of class methods to manage the state of the library.

    # Project Structure:
        # Book Class   :  To store book information (title, author, ISBN, availability).
        # Library Class:  To manage the collection of books and actions like adding, issuing, and returning books.
        # User Class   :  To represent a user who can issue and return books.

class Book():
    def __init__(self, title, author, isbn):
        self.title     = title
        self.author    = author
        self.isbn      = isbn
        self.is_issued = False # Assume initially no book is issued.

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
# Define the Library class to manage a collection of books

class library():
    def __init__(self):
        self.books =  []            #  A list to store all books in the library

    def add_book(self, book):
        self.books.append(book)      # Add a new book to the library

    def list_books(self):
        # List all books that are available (not issued)
        available_books = [ book for book in self.books if not book.is_issued ]
        if available_books:
            print("Available books: ")
            for book in available_books:
                print(book)
        else:
            print("No books available at the moment.")
    
    def issue_book(self, book_title):
        # Find the book and issue it (mark it as issued)
        for book in self.books:
            if book.title == book_title and not book.is_issued:
                book.is_issued = True
                print(f"Book {book.title} has been issued.")
                return
        print(f"Sorry, the book {book_title} is either not available or already issued.")

    def return_book(self, book_title):
        # Find the book and mark it as returned (not issued)
        for book in self.books:
            if book.title == book_title and book.is_issued:
                book.is_issued = False
                print(f"Book {book.title} has been issued.")
                return
        print(f"Sorry, the book '{book_title}' is either not available or already issued.")

# Define the User class to represent a library user

class user:
    def __init__(self, name):
        self.name = name
        self.issued_books = []                    # List to track books issued by the user

    def issue_book(self, library, book_title):
        library.issue_book(book_title)            # Call the library's issue_book method

    def return_book(self, library, book_title):
        library.return_book(book_title)           # Call the library's return_book method

if __name__ == "__main__":

    # Add book objects (instances) to the library
    book_1 = Book("Python", "Author-1", 1234)
    book_2 = Book("C++", "Author-2", 5678)
    book_3 = Book("Terraform Basics", "Author-3", 9012)

    # Create a library instance
    my_lib = library()

    my_lib.add_book(book_1)
    my_lib.add_book(book_2)
    my_lib.add_book(book_3)

    # Display available books
    my_lib.list_books()

    # Create user instances
    user_1 = user("Shiv")
    user_2 = user("Divi")

    # User_1 issuing and returning books
    user_1.issue_book(my_lib, "Python")
    # user_1.return_book(my_lib, "Python")

    # User_2 issuing and returning books
    user_2.issue_book(my_lib, "C++")
    user_2.issue_book(my_lib, "Python")

    # List available books again after issuing/returning
    my_lib.list_books()

    # Points to note.

        # Passing an instance: Here in this code, we're passing instances of the book class (like book_1) to add_book, 
        # which the library can then store.