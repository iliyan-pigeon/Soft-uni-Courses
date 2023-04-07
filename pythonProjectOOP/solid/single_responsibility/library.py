from solid.single_responsibility.books import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        return f"The book {title} is not in the library."

    def __repr__(self):
        return f"{self.name} with books: {', '.join([book.title for book in self.books])}"


book_one = Book("abc", "cba")
book_two = Book("cba", "abc")
library = Library("National")
library.add_book(book_one)
print(library.find_book("abc"))
print(library.find_book("asd"))
print(book_one)
print(library)




