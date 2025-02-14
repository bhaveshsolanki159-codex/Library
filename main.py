class Library:
    TotalBooks=0
    def __init__(self):
        self.books =[]
    
    def add_book(self,book):
        # no0fBooks+=1
        self.TotalBooks+=1
        self.books.append(book)

    # def TotalBooks(self):
    #     return no0fBooks

    def display_books(self):
        for book in self.books:
            print(book)

    def no0fBooks(self):
        return len(self.books)
    
    def remove_book(self,book):
        self.books.remove(book)

# class ScienceFrictionBooks(Library):
#     def __init__(self):
#         super().__init__()
#         self.ScienceFrictionBooks = []

#     def add_book(self, book):
#         self.books.append(book)
#         return super().add_book(book)

#     def display_books(self):
#         return super().display_books()
    
#     def no0fBooks(self):
#         return super().no0fBooks()
    
#     def remove_book(self, book):
#         return super().remove_book(book)



if __name__ == "__main__":
    ScienceFrictionBooks = Library()

    ScienceFrictionBooks.add_book("Physics")
    ScienceFrictionBooks.add_book("Chemistry")
    ScienceFrictionBooks.add_book("Biology")
    ScienceFrictionBooks.add_book("Mathematics")

    ScienceFrictionBooks.display_books()
    print(ScienceFrictionBooks.no0fBooks())

    PhylosophyBooks = Library()

    PhylosophyBooks.add_book("The Republic")
    PhylosophyBooks.add_book("The Prince")
    PhylosophyBooks.add_book("The Art of War")
    PhylosophyBooks.add_book("The Wealth of Nations")

    PhylosophyBooks.display_books()
    print(PhylosophyBooks.no0fBooks())

    print(Library.Books())

    