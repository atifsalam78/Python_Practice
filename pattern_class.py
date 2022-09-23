class Pattern:

    def __init__(self, row):
        self.row = row

    def print_ascending_pattern(self):
        for i in range(1,self.row+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
        return "Ascending End"

    def print_descending_pattern(self):
        for k in range(self.row+1):
            for l in range(self.row-k,0,-1):
                print("*",end="")
            print()
        return "Descending End"

option = input("What you want (A/D): ")
if option == "a" or option == "A":
    pt = Pattern(int(input("number: ")))
    print(pt.print_ascending_pattern())

elif option == "d" or option == "D":
    pt = Pattern(int(input("number: ")))
    print(pt.print_descending_pattern())

# ascending = Pattern(10)
# descending = Pattern(5)
# print(ascending.print_ascending_pattern())
# print(descending.print_descending_pattern())

a = Pattern(5)