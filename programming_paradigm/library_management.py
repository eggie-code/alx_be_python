class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def Check_out_Book(self):
        """Check out the book."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def Return_Book(self):
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

    def remove_Book(self, book):
        """Remove a book from the library."""
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def find_Book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title == title:
                return book
        return None
