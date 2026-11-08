from classes.book import Book

        
books = [
    Book("Clean Code", "Martin", 3),
    Book("Python Basics", "Cohen", 1),
]
 
books[0].borrow()
books[1].borrow()
 
try:
    books[1].borrow()
except ValueError as error:
    print("Python Basics ->", error)
 
try:
    Book("Empty", "Nobody", 0)
except ValueError as error:
    print("Empty ->", error)
 
for book in books:
    print(book, "| available:", book.is_available())
 
print("Books in the library:", Book.total_books)
