class LibraryManagement:
    from datetime import datetime

    def __init__(self):
        self.books = {"001": {"Book Name": "Poor Dad Rich Son", "Author": "Mario Quintero", "Status": None, "Lender": None},
                      "002": {"Book Name": "The 7 Habits of Highly Effective People", "Author": "Stephen Covey", "Status": None, "Lender": None}}

    def add_book(self):
        while True:
            sr = input("Enter Book ID(Add): ")
            if sr not in self.books:
                self.books[sr] = {}
                name = input("Book Name: ")
                auth = input("Author Name: ")
                self.books[sr]["Book Name"] = name
                self.books[sr]["Author"] = auth
                self.books[sr]["Status"] = "Available"
                self.books[sr]["Lender"] = ""
                break

    def lend_book(self):
        while True:
            b_id = input("Enter Book ID(Lender): ")
            if b_id in self.books:
                l_name = input("Enter Name: ")
                self.books[b_id]["Lender"] = l_name
                self.books[b_id]["Status"] = f"Lended by {l_name}"
                self.books[b_id]["Lended Dated"] = self.datetime.now()
                self.books[b_id]["Issued By"] = "Librarian Name"
                break

    def book_detail(self):
        for book_id, book_info in self.books.items():
            print("\nBook Id: ", book_id)
            for key in book_info:
                print(key + ":", book_info[key])

    def book_return(self):
        while True:
            b_id = input("Enter Book ID(Return): ")
            if b_id in self.books:
                print(self.books[b_id])
                self.books[b_id]["Lender"] = ""
                self.books[b_id]["Status"] = ""
                self.books[b_id]["Return Dated"] = self.datetime.now()
                self.books[b_id]["Collected By"] = "Collector Name"
                break


a = LibraryManagement()
# a.add_book()
a.lend_book()
# a.book_return()
a.book_detail()
