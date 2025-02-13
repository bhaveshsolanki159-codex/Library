class Library:
    def __init__(self):
        self.books =[]
    
    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def no0fBooks(self):
        return len(self.books)
    
    def remove_book(self,book):
        self.books.remove(book)

if __name__ == "__main__":
    library = Library()
    library.add_book("Book1")
    library.add_book("Book2")
    library.display_books()
    print(library.no0fBooks())