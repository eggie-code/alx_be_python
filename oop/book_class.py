class Book:  # creatingb an instance of book
    def_init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):  # delete a book instance
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
