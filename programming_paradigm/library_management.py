class book:
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

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def remove_book(self, book):
        """Remove a book from the library."""
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def find_book(self, title):
        """Find a book by title."""
        for book in self.books:
            if book.title == title:
                return book
        return None
