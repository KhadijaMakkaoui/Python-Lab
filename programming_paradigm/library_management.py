class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title= title
        self.author=author
        self._is_checked_out=_is_checked_out
    

class Library:
    _books=[]

    def __init__(self) -> None:
        pass
    def add_book(self,book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out=True
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out=False
    
    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out==False:
                print(f"{book.title} by {book.author}")



    def main():
        # Setup a small library
        library = Library()
        library.add_book(Book("Brave New World", "Aldous Huxley"))
        library.add_book(Book("1984", "George Orwell"))

        # Initial list of available books
        print("Available books after setup:")
        library.list_available_books()

        # Simulate checking out a book
        library.check_out_book("1984")
        print("\nAvailable books after checking out '1984':")
        library.list_available_books()

        # Simulate returning a book
        library.return_book("1984")
        print("\nAvailable books after returning '1984':")
        library.list_available_books()

    if __name__ == "__main__":
        main()