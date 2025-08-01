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
        self.books = []

    def add_Book(self, book):
        """Add a book to the library."""
        self.books.append(book)

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
