#### Concepts of OOP ####

    # Class: A blueprint that defines attributes (data) and methods (functions).
    # Object: An instance of a class that holds real data and can perform actions.
    # Methods: Functions inside a class that define the behavior of the objects.
    # Inheritance: Creating new classes that inherit from existing ones to reuse code.
    # Encapsulation: Controlling access to attributes using public, protected, and private attributes.
   
   <!-- 

   The Main Idea:
        -- One class can have instances (objects) of another class as attributes or parameters.
        -- An instance of a class holds its own values for the variables (attributes) defined in that class.
        -- These attributes (like is_issued in the book class) can be accessed by other functions or methods in another class by using objects of the first class.

        How Classes Work Together:

           - When we create a book object, like book_1 = book("Python", "Author-1", 1234), it will have its own is_issued attribute.

            - When we add that book to the library using my_lib.add_book(book_1), the library class gets a reference to the book_1 object. This means it can access all the attributes of book_1, including is_issued.

            Key Points to Remember:

                -- Attributes are part of objects: is_issued is an attribute of each individual book object.
                -- When you create a book, you can access its is_issued attribute.
                -- Accessing attributes in other classes: You can access an object's attributes (like is_issued) in other classes when you have a reference to that object.
                -- In the library class, we have a list of book objects (self.books), and each book object has its own is_issued attribute.
                -- Objects inside a list: The library class has a list of book objects. The method list_books() loops over this list and checks each book's is_issued attribute.
    -->