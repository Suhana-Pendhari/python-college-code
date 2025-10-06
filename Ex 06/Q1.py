# Q1) Library Management System:
# •	Design a system to manage books, patrons, and library transactions. 
# Implement classes for books, patrons (members), transactions (checkouts, returns), 
# and a library inventory

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"{self.book_id} - {self.title} by {self.author} ({'Available' if self.is_available else 'Checked Out'})"


class Patron:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member {self.member_id}: {self.name}, Books borrowed: {len(self.borrowed_books)}"


class Transaction:
    def __init__(self, patron, book, action):
        self.patron = patron
        self.book = book
        self.action = action

    def __str__(self):
        return f"{self.patron.name} {self.action} -> {self.book.title}"


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def checkout_book(self, book_id, member_id):
        book = self.find_book(book_id)
        patron = self.find_patron(member_id)
        if book and patron and book.is_available:
            book.is_available = False
            patron.borrowed_books.append(book)
            transaction = Transaction(patron, book, "Checked Out")
            self.transactions.append(transaction)
            print(transaction)
        else:
            print("Checkout failed! Book not available or patron not found.")

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        patron = self.find_patron(member_id)
        if book and patron and book in patron.borrowed_books:
            book.is_available = True
            patron.borrowed_books.remove(book)
            transaction = Transaction(patron, book, "Returned")
            self.transactions.append(transaction)
            print(transaction)
        else:
            print("Return failed! Check details again.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_patron(self, member_id):
        for patron in self.patrons:
            if patron.member_id == member_id:
                return patron
        return None

    def show_inventory(self):
        print("\nLibrary Inventory:")
        for book in self.books:
            print(book)


library = Library()

#Add books
library.add_book(Book("Python Basics", "Guido", 1))
library.add_book(Book("C++ Fundamentals", "Bjarne", 2))
library.add_book(Book("Data Structures", "Suhana", 3))

#Add patrons
library.add_patron(Patron("Suhana", 101))
library.add_patron(Patron("Aman", 102))

#Show inventory
library.show_inventory()

#Checkout and Return
library.checkout_book(1, 101)
library.checkout_book(2, 102)
library.return_book(1, 101)

#Show inventory again
library.show_inventory()
