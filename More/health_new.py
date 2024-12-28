print("Health Management System")

do = {"1": "Log", "2": "Retrieve"}
opt = {"1": "Diet", "2": "Exercise"}
client_detail = {"1": "Harry", "2": "Rohan", "3": "Hammad"}

def getdate():
    """ Return current date and time """
    import datetime
    return datetime.datetime.now()

def write_log(file_name):
    """ Update Log, taking file name as argument """
    time_date = str(getdate())
    f = open(file_name, "a")

    f.write("\n")
    f.write(client_name)
    f.write("\n")

    f.write(choice3)
    f.write("\n")

    time_date_str = "["+time_date+"]"
    f.write(time_date_str)
    f.write("\n")

    if choice3 == "Diet":
        f.write(diet_detail)
    elif choice3 == "Exercise":
        f.write(ex_detail)

    f.write("\n**********")
    f.close()

def client_sel_diet():
    """ Selection of client """
    global client_name
    client_name = client_detail[input("to whom you want to? ")]
    if client_name == "Harry":
        print("Harry")
        write_log("harry_diet.txt")

    elif client_name == "Rohan":
        print("Rohan")
        write_log("rohan_diet.txt")

    elif client_name == "Hammad":
        print("Hammad")
        write_log("hammad_diet.txt")

def client_sel_ex():
    """ Selection of client """
    global client_name
    client_name = client_detail[input("to whom you want to? ")]
    if client_name == "Harry":
        print("Harry")
        write_log("harry_ex.txt")

    elif client_name == "Rohan":
        print("Rohan")
        write_log("rohan_ex.txt")

    elif client_name == "Hammad":
        print("Hammad")
        write_log("hammad_ex.txt")

def retrieve_log(ret_file):
    """ Retrieve log file, taking file name as argument"""
    print("Retrieve")
    f = open(ret_file)
    for lines in f.readlines():
        print(str(lines),end="")

while True:
    choice1 = do[input("Do you want to (Log / Retrieve: ): ")] # Select option for log or retrieve
    if choice1 == "Log":
        print("Log")

        choice3 = opt[input("What you want to (Diet/Exercise)? ")] # Selection between Diet or Exercise
        if choice3 == "Diet":
            diet_detail = input("Diet Detail: ")
            client_sel_diet()

        elif choice3 == "Exercise":
            ex_detail = input("Exercise Detail: ")
            client_sel_ex()

    elif choice1 == "Retrieve":
        ret_opt = opt[input("What you want to (Diet/Exercise)? ")]
        client_file = client_detail[input("to whom you want to? ")]

        if client_file == "Harry" and ret_opt == "Diet":
            retrieve_log("harry_diet.txt")

        elif client_file == "Rohan" and ret_opt == "Diet":
            retrieve_log("rohan_diet.txt")

        elif client_file == "Hammad" and ret_opt == "Diet":
            retrieve_log("hammad_diet.txt")

        elif client_file == "Harry" and ret_opt == "Exercise":
            retrieve_log("harry_ex.txt")

        elif client_file == "Rohan" and ret_opt == "Exercise":
            retrieve_log("rohan_ex.txt")

        elif client_file == "Hammad" and ret_opt == "Exercise":
            retrieve_log("hammad_ex.txt")

    cont = input("Do you want to continue (Y/N): ")
    if cont == "y" or cont == "Y":
        print("Continue")
        continue

    else:
        print("Exit")
        break