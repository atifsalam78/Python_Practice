print("Atif Salam Library Management System")
class LibraryManagement:

    from datetime import datetime

    def __init__(self):
        self.books = {1001: {"Book Name": "Poor Dad Rich Son", "Author": "Mario Quintero", "Status": None,
                              "Lender": None},
                      1002: {"Book Name": "The 7 Habits of Highly Effective People", "Author": "Stephen Covey",
                              "Status": None, "Lender": None},
                      1003: {"Book Name": "Beginning Python", "Author": "Magnus Lie Hetland", "Status": None,
                              "Lender": None}}

    def add_book(self, b_id, bname, bauth):
        if b_id in self.books:
            print(f"""Book Serial Number "{b_id}" already in the database""")
        else:
            self.books[b_id] = {}
            self.books[b_id]["Book Name"] = bname
            self.books[b_id]["Author"] = bauth
            self.books[b_id]["Status"] = "Available"
            self.books[b_id]["Lender"] = ""
            print(f"""Book Serial Number "{b_id}" successfully added in the database""")
            
    def particular_book_details(self, b_id):
        if b_id not in self.books:
            print(f"""Book Serial Number "{b_id}" not in the database""")
        else:
            for ki, val in self.books[b_id].items():
                print(ki + ":", val)
            
    def lend_book(self,b_id,l_name):
        if b_id in self.books:
            self.books[b_id]["Lender"] = l_name
            self.books[b_id]["Status"] = f"Lended by {l_name}"
            self.books[b_id]["Lended Date"] = self.datetime.now()
            self.books[b_id]["Issued By"] = "Librarian Name"
            for ky, va in self.books[b_id].items():
                print(ky + ":", va)            
        else:
            print("Required book not available in database")

    def all_books_detail(self):
        for book_id, book_info in self.books.items():
            print("\nBook Id: ", book_id)
            for key in book_info:
                print(key + ":", book_info[key])

    def book_return(self,b_id):
        if b_id not in self.books:
            print(f"""Book Serial Number "{b_id}" not in the database""")
        else:
            self.books[b_id]["Lender"] = ""
            self.books[b_id]["Status"] = ""
            self.books[b_id]["Return Dated"] = self.datetime.now()
            self.books[b_id]["Collected By"] = "Collector Name"
            print(f"""Book Serial Number "{b_id}" collected """)


a = LibraryManagement()
while True:
    option ={"a":"Add Book", "l": "Lend Book", "r": "Return Book","d": "Complete Books Detail",
             "p": "Particular Book Details"}
    for x, y in option.items(): print(f"""Press "{x}" for "{y}" """)
    opt = option.get(input("Enter the required option: "))

    if opt == "Add Book":
        b_id = int(input("Boook Id: "))
        bname = input("Book Name: ")
        bauth = input("Book Author Name: ")
        a.add_book(b_id, bname, bauth)

    elif opt == "Lend Book":
        for book_id in a.books.keys():
            print(f""" {book_id} - {a.books[book_id]["Book Name"]} - Status: {a.books[book_id]["Status"]} """)
        b_id = input("Book Id: ")
        l_name = input("Lender Name: ")
        a.lend_book(b_id, l_name)

    elif opt == "Return Book":
        for book_id in a.books.keys():
            print(f""" {book_id} - {a.books[book_id]["Book Name"]} """)
        b_id = input("Book Id: ")
        a.book_return(b_id)

    elif opt == "Complete Books Detail":
        a.all_books_detail()

    elif opt == "Particular Book Details":
        for book_id in a.books.keys():
            print(f""" {book_id} - {a.books[book_id]["Book Name"]} """)
        b_id = input("Book Id: ")
        a.particular_book_details(b_id)

    cont = input("Do you want to continue (Y/N): ")
    if cont == "y" or cont == "Y":
        continue
    else:
        print("Thank you, Good Bye!")
        break
