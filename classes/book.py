class Book:

    total_books = 0

    def __init__(self, book_name, authors_name, copies) -> None:
        
        if copies < 1:
            raise ValueError("copies must be at least 1")
        
        self.book_name = book_name
        self.authors_name = authors_name
        self.__copies = copies
        self.__available_books = copies
        Book.total_books += 1

    def __str__(self) -> str:
        return f"{self.book_name} by {self.authors_name} ({self.__available_books}/{self.__copies} available)"

    def borrow(self):
        if self.__available_books < 1:
            raise ValueError("no copies available")
        self.__available_books -= 1

    def return_book(self):
        if self.__available_books ==  self.__copies:
            raise ValueError("all copies are already in")
        self.__available_books += 1
    
    def is_available(self):
        if self.__available_books > 0:
            return True
        else:
            return False
