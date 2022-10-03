from datetime import datetime
from multiprocessing.sharedctypes import Value
import os
class LibraryManagement:

    import datetime

    def __init__(self):
        self.books = {1001: {"Book Name": "Poor Dad Rich Son", "Author": "Mario Quintero", "Status": "Available",
                              "Lender": ""},
                      1002: {"Book Name": "The 7 Habits of Highly Effective People", "Author": "Stephen Covey",
                              "Status": "Available", "Lender": ""},
                      1003: {"Book Name": "Beginning Python", "Author": "Magnus Lie Hetland", "Status": "Available",
                              "Lender": ""}}

    def add_book(self, b_id, bname, bauth):
        self.books[b_id] = {}
        self.books[b_id]["Book Name"] = bname
        self.books[b_id]["Author"] = bauth
        self.books[b_id]["Status"] = "Available"
        self.books[b_id]["Lender"] = ""
        print(f"Book Serial Number '{b_id}' successfully added in the database")

    def issue_book(self,b_id,l_name):
        if b_id not in self.books:
            print("Required book not available in database")
            
        else:
            self.books[b_id]["Lender"] = l_name
            self.books[b_id]["Status"] = "Not Available"
            self.books[b_id]["Issued Date"] = datetime.now().strftime('%Y-%m-%d')
            self.books[b_id]["Issued By"] = "Issuer Name"
            for ky, va in self.books[b_id].items():
                print(ky + ":", va)
    
    def return_book(self,b_id):
        if b_id not in self.books:
            print(f"Book Serial Number '{b_id}' not in the database")
        else:
            self.books[b_id]["Lender"] = ""
            self.books[b_id]["Status"] = "Available"
            self.books[b_id]["Return Dated"] = datetime.now().strftime('%Y-%m-%d')
            self.books[b_id]["Collected By"] = "Collector Name"
            print(f"Book Serial Number '{b_id}' collected")
    
    def all_books_detail(self):
        for book_id, book_info in self.books.items():
            print("\nBook Id: ", book_id)
            for key in book_info:
                print(key + ":", book_info[key])

    def particular_book_details(self, b_id):
        if b_id not in self.books:
            print(f"Book Serial Number '{b_id}' not in the database")
        else:
            for ki, val in self.books[b_id].items():
                print(ki + ":", val)

    @staticmethod
    def input_id():
        book_id_in = int(input("\nBoook ID: "))
        return book_id_in

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name=='nt' else 'clear')
    
a = LibraryManagement()
while True:    
    a.clear_screen()   
    print("\tSalam's Library Management System\n") 
    try:   
        option ={"a":"Add Book", "i": "Issue Book", "r": "Return Book","c": "Complete Books",
                 "p": "Particular Book"}
        for x, y in option.items(): print(f"Press '{x}' for '{y}'")
        opt = option.get(input("Enter the required option: "))

        if opt == "Add Book":
            b_id = a.input_id()
            if b_id in a.books:
                print(f"Book Serial Number '{b_id}' already in the database")
            
            else:
                bname = input("Book Name: ")
                bauth = input("Book Author Name: ")
                a.add_book(b_id, bname, bauth)

        elif opt == "Issue Book":
            for book_id in a.books.keys():
                if a.books[book_id]['Status'] == 'Available':
                    print(f"{book_id} - {a.books[book_id]['Book Name']} - Status: {a.books[book_id]['Status']}")
                
            book_id = a.input_id()
            try:
                if a.books[book_id]['Status'] == 'Available':
                    l_name = input("Lender Name: ")
                    a.issue_book(book_id, l_name)
                else:
                    print("Boook Not available for issuance")
            except KeyError:
                print(f"Book ID '{book_id}' not avilable for issuance")

        elif opt == "Return Book":
            for book_id in a.books.keys():                
                if a.books[book_id]['Status'] == 'Not Available':
                    print(f"{book_id} - {a.books[book_id]['Book Name']} - Status: {a.books[book_id]['Status']}")
                      
            book_id = a.input_id()
            try:
                if a.books[book_id]['Status'] == 'Not Available':
                    a.return_book(book_id)
                else:
                    print("Book not avilable for return")
            except KeyError:
                print(f"Book ID '{book_id}' not avilable for return")

        elif opt == "Complete Books":
            a.all_books_detail()

        elif opt == "Particular Book":
            for book_id in a.books.keys():
                print(f"{book_id} - {a.books[book_id]['Book Name']}")
            b_id = a.input_id()
            a.particular_book_details(b_id)

        cont = input("Do you want to continue (Y/N): ")
        if cont == "n" or cont == "N":
            print("Thank you, Good Bye!")
            break
        else:
            continue
    except ValueError:
        input("Inappropriate Value")

    
