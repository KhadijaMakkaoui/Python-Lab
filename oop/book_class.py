class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        print("Deleting "+self.title)

    def __str__(self):
        return self.title+ " by "+self.author + ", published in " + str(self.year)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
#main----------------------------------------------------------------
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()