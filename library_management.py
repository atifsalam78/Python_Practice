class LibraryManagement:
    from datetime import datetime

    def __init__(self):

        self.books = {"001": {"Book Name": "Poor Dad Rich Son", "Author": "Mario Quintero", "Status": None,
                              "Lender": None},
                      "002": {"Book Name": "The 7 Habits of Highly Effective People", "Author": "Stephen Covey",
                              "Status": None, "Lender": None},
                      "003": {"Book Name": "Beginning Python", "Author": "Magnus Lie Hetland", "Status": None,
                              "Lender": None}}

    def add_book(self,b_id, name, auth):
        if b_id in self.books:
            print(f"""Book Serial Number "{b_id}" already in the database""")
            
        else:
            self.books[b_id] = {}
            self.books[b_id]["Book Name"] = name
            self.books[b_id]["Author"] = auth
            self.books[b_id]["Status"] = "Available"
            self.books[b_id]["Lender"] = ""
            print(f"""Book Serial Number "{b_id}" successfully added in the database""")
            
    def particular_book_details(self, b_id):
        if b_id not in self.books:
            print(f"""Book Serial Number "{b_id}" not in the database""")
        
        else:
            print(f"Book Id: {b_id}")
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

print("Atif Salam Library Management System")
a = LibraryManagement()
while True:
    option ={"a":"Add Book", "l": "Lend Book", "r": "Return Book","d": "Complete Books Detail",
         "p": "Particular Book Details", "e": "Exit"}
    opt = option.get(input("Enter the required option: "))
    if opt == "Add Book":
        b_id = input("Book Id: ")
        name = input("Book Name: ")
        auth = input("Book Author Name: ")
        a.add_book(b_id, name, auth)
    elif opt == "Lend Book":
        b_id = input("Book Id: ")
        l_name = input("Lender Name: ")
        a.lend_book(b_id, l_name)
    elif opt == "Return Book":
        b_id = input("Book Id: ")
        a.book_return(b_id)
    elif opt == "Complete Books Detail":
        a.all_books_detail()
    elif opt == "Particular Book Details":
        b_id = input("Book Id: ")
        a.particular_book_details(b_id)
    elif opt == "Exit":
        print("Exit")
        break


