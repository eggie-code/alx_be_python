class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                print(f"Checked out '{book.title}'.")
                return True
            else:
                print(F"'{book.titke}' is already checked out.")
                return False
    print(f"Book title '{title}' not found ")
    return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"Returned '{book.title}'.")
                return True
            else:
                print(F"'{book.title}' is not checked out.")
                return False
        print(f"Book title '{title}' not found.")
        return False

    def list_available_books(self):
        """print all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
        for book in available_books:
            print(str(book))
