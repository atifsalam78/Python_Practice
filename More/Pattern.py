row = 5
num = 5
bol = {"T": True, "F": False}
print(""" "T" For Asscending Order and "F" For Descending Order """)
selection = bol[input("Enter Selection (T/F): ")]

if selection == True:
    print("***Ascending Order Pattern***")
    for a in range(1,row+1,1):
        for b in range(1,a+1,1):
            print("*",end="")
        print()

elif selection == False:

    print("***Descending Order Pattern***")
    for c in range(0,row+1):
        for d in range(num-c,0,-1):
            print("*",end="")
        print()
