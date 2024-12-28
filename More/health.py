print("Health Management System")

do = {"1": "Log", "2": "Retreive"}
client = {"1": "Harry", "2": "Rohan", "3": "Hammad"}
opt = {"1": "Diet", "2": "Excercise"}

def getdate(): # Get current date and time
    import datetime
    return datetime.datetime.now()

def signature(): # Create signature
    thank = "Thankyou for using health management system"
    create = "Created by:"
    name = "Atif Salam"
    date = "Dated: 30-08-2022"
    aster = "*" * len(thank)
    print(aster)
    print(thank)
    print(create,name)
    print(date)
    print(aster)

choice1 = do[input("Do you want to (Log / Retreive: ): ")] # Select option for log or retreive
if choice1 == "Log":
    print("Log")

    choice2 = client[input("to whom you want to? ")] # Select Client
    if choice2 == "Harry":
        print("Harry")
    elif choice2 == "Rohan":
        print("Rohan")
    elif choice2 == "Hammad":
        print("Hammad")

    choice3 = opt[input("What you want to (Diet/Excercise)? ")] # Selection between Diet or Excercise
    if choice3 == "Diet":
        print("Diet")
    elif choice3 == "Excercise":
        print("Excercise")
# Write Date on log file
    time_date = str(getdate())
    f = open("C:\Officeup\diet.txt", "a")
    f.write("\n")
    f.write(choice1)
    f.write("\n")
    f.write(time_date)
    f.write("\n")
    f.write(choice2)
    f.write("\n")
    f.write(choice3)
    f.write("\n**********")
    f.close()

elif choice1 == "Retreive":
    print("Retreive")
    f = open("C:\Officeup\diet.txt")
    for lines in f.readlines():
        print(str(lines),end="")

signature()