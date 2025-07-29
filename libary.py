## Create a Book class and a Library class to add books and display all books.

class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

class Library:
    def __init__(self):
        self.books=[]

    def addBook(self, book):
        self.books.append(book)
        print(f"Added {book}")

    def display_books(self):
        for book in self.books:
            print(book)


book1 = Book("The Alchemist", "Paulo Coelho", 1988)
book2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 1997)
book3 = Book("1984", "George Orwell", 1949)

library = Library()

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.display_books()