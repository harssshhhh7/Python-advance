class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully")
        else:
            print("Book is already available")

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(self.book_id, self.title, status)


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name

    def display(self):
        print("Patron ID:", self.patron_id)
        print("Patron Name:", self.name)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")

        book = Book(book_id, title)
        self.books.append(book)

        print("Book added successfully")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                book.display()

    def borrow_book(self):
        book_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book.book_id == book_id:
                book.borrow_book()
                return

        print("Book not found")

    def return_book(self):
        book_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                return

        print("Book not found")

    def add_patron(self):
        patron_id = int(input("Enter Patron ID: "))
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron added successfully")

    def display_patron(self):
        patron_id = int(input("Enter Patron ID: "))

        for patron in self.patrons:
            if patron.patron_id == patron_id:
                patron.display()
                return

        print("Patron not found")

    def display_all_patrons(self):
        if len(self.patrons) == 0:
            print("No patrons found")
        else:
            for patron in self.patrons:
                patron.display()
                print()


library = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Add Patron")
    print("6. Display Patron")
    print("7. Display All Patrons")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.borrow_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        library.add_patron()

    elif choice == 6:
        library.display_patron()

    elif choice == 7:
        library.display_all_patrons()

    elif choice == 8:
        print("Exiting Library Management System")
        break

    else:
        print("Invalid choice")