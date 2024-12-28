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
    
def client():
    """ Selection of client """
    global client_name
    global concatenate
    client_name = client_detail[input("to whom you want to? ")]    
    concatenate = client_file+"_"+choice3+"_"+choice1+".txt"


def client_diet_log():
    """ Maintain client's diet log """
    client()
        
    if client_name == "Harry":
        
        write_log(concatenate)

    elif client_name == "Rohan":
        
        write_log(concatenate)

    elif client_name == "Hammad":
        
        write_log(concatenate)

def client_ex_log():
    """ Maintain client's excercise log """
    client()
    if client_name == "Harry":
        
        write_log(concatenate)

    elif client_name == "Rohan":
        
        write_log(concatenate)

    elif client_name == "Hammad":
        
        write_log(concatenate)

def retrieve_log(ret_file):
    """ Retrieve log file, taking file name as argument"""
    print("Retrieve")
    f = open(ret_file)
    for lines in f.readlines():
        print(str(lines),end="")

def sel_diet_ex():
    global choice3
    choice3 = opt[input("What you want to (Diet/Exercise)? ")]
    
while True:
    try:
        choice1 = do[input("Do you want to (Log / Retrieve: ): ")] # Select option for log or retrieve
        if choice1 == "Log":
            print("Log")
            
            sel_diet_ex()
            if choice3 == "Diet":
                diet_detail = input("Diet Detail: ")
                client_diet_log()

            elif choice3 == "Exercise":
                ex_detail = input("Exercise Detail: ")
                client_ex_log()

        elif choice1 == "Retrieve":
            
            sel_diet_ex()            
            client_file = client_detail[input("to whom you want to? ")]
            
           
            if client_file == "Harry" and choice3 == "Diet":
                retrieve_log("Harry_Diet_Log.txt")

            elif client_file == "Rohan" and choice3 == "Diet":
                retrieve_log("Rohan_Diet_Log.txt")

            elif client_file == "Hammad" and choice3 == "Diet":
                retrieve_log("Hammad_Diet_Log.txt")

            elif client_file == "Harry" and choice3 == "Exercise":
                retrieve_log("Harry_Exercise_Log.txt")

            elif client_file == "Rohan" and choice3 == "Exercise":
                retrieve_log("Rohan_Exercise_Log.txt")

            elif client_file == "Hammad" and choice3 == "Exercise":
                retrieve_log("Hammad_Exercise_Log.txt")

        cont = input("Do you want to continue (Y/N): ")
        if cont == "y" or cont == "Y":
            print("Continue")
            continue

        else:
            print("Exit")
            break
    except KeyError:
            print("Enter Valid Key")