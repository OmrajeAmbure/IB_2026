"""
9>libary book managment crete a book class with bookid ,title,auther,is_issue("book store")
1)add book
2)display all book
3)sersch book id
4)issue book
5)return book
6)display available show status 
7)exit
"""
class Book:
    libraryName = "My Library"
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

books = []
print(f"=========================== Welcome to {Book.libraryName} =========================== ")
while True:
    print("""
        1. Add Book
        2. Display All Books
        3. Search Book by ID
        4. Issue Book
        5. Return Book
        6. Display Available Books
        7. Exit
    """)
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            books.append(Book(book_id, title, author))
        case 2:
            print("=================== All Books ===================")
            for book in books:
                book.display()
        case 3:
            search_id = input("Enter Book ID to search: ")
            for book in books:
                if book.book_id == search_id:
                    print("Book Found!")
                    book.display()
                    break
            else:
                print("Book not found")
        case 4:
            issue_id = input("Enter Book ID to issue: ")
            for book in books:
                if book.book_id == issue_id and not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' has been issued.")
                    break
            else:
                print("Book not available for issue or not found.")
        case 5:
            return_id = input("Enter Book ID to return: ")
            for book in books:
                if book.book_id == return_id and book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' has been returned.")
                    break
            else:
                print("Book not found or was not issued.")
        case 6:
            print("=================== Available Books ===================")
            for book in books:
                if not book.is_issued:
                    book.display()
        case 7:
            print("Thank you for using the library management system. Goodbye!")
            break
