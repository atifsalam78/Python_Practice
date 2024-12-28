print("Health Management System")

do = {"1": "Log", "2": "Retrieve"}
opt = {"1": "Diet", "2": "Exercise"}
client_detail = {"1": "Harry", "2": "Rohan", "3": "Hammad"}


def getdate():
    """ Return current date and time """
    import datetime
    return datetime.datetime.now()


def client_log():
    """ Maintain client's log """
    # Client Selection
    global log_file
    print(client_detail)
    client_name = client_detail[input("To whom you want to? ")]
    concat_log = client_name + "_" + opt_sel + ".txt"

    # Writing on client's file
    with open(concat_log, "a") as log_file:

        date_time_str = str(getdate())
        client_write_detail = "\n"+client_name+"\n"+opt_sel+"\n"+"[" + date_time_str + "]"+"\n"+opt_detail
        log_file.write(client_write_detail)
        log_file.write("\n**********")


while True:
    try:
        task = do[input("Do you want to (Log / Retrieve: ): ")]  # Select option for log or retrieve
        if task == "Log":
            print("Log")
            
            opt_sel = opt[input("What you want to (Diet/Exercise)? ")]
            opt_detail = input("Detail: ")
            client_log()

        elif task == "Retrieve":
            opt_retrieve = opt[input("What you want to (Diet/Exercise)? ")]
            print(client_detail)
            client_file = client_detail[input("To whom you want to? ")]
            concat_retrieve = client_file+"_"+opt_retrieve+".txt"

            print("Retrieve")
            with open(concat_retrieve) as log_file:
                for lines in log_file.readlines():
                    print(lines, end="")

        cont = input("Do you want to continue (Y/N): ")
        if cont == "y" or cont == "Y":
            continue

        else:
            print("Thank You for using!")
            break

    except KeyError:
        print("Enter valid key!")
    except FileNotFoundError:
        print("Client file not exist!")
