class Library:
    TotalBook = 0
    TotalLibrary = 0
    
    def __init__(self):
        self.books = []
        Library.TotalLibrary += 1


    
    def add_book(self, book: str) -> None:
        """Adds a book to the library"""
        self.books.append(book)
        Library.TotalBook += 1


    # def TotalBooks(self):
    #     return no0fBooks

    def display_books(self) -> None:
        """Displays all books in the library"""
        if self.books:
            print("Books in library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library is empty")


    def number_of_books(self) -> int:
        """Returns the number of books in the library"""
        return len(self.books)


    
    def remove_book(self, book: str) -> None:
        """Removes a book from the library"""
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Book '{book}' not found in library")






if __name__ == "__main__":
    science_books = Library()

    science_books.add_book("Physics")
    science_books.add_book("Chemistry")
    science_books.add_book("Biology")
    science_books.add_book("Mathematics")

    science_books.display_books()
    print(science_books.number_of_books())

    philosophy_books = Library()

    philosophy_books.add_book("The Republic")
    philosophy_books.add_book("The Prince")
    philosophy_books.add_book("The Art of War")
    philosophy_books.add_book("The Wealth of Nations")

    philosophy_books.display_books()
    print(philosophy_books.number_of_books())


    print(f"Total libraries created: {Library.TotalLibrary}")
    print(f"Total book added in all libraries: {Library.TotalBook}")
