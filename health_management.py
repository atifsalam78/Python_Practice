print("Health Management System")

do = {"1": "Log", "2": "Retrieve"}
opt = {"1": "Diet", "2": "Exercise"}
client_detail = {"1": "Harry", "2": "Rohan", "3": "Hammad"}


def getdate():
    """ Return current date and time """
    import datetime
    return datetime.datetime.now()


def option_ask():
    global concat_log, client_name, opt_sel

    print(client_detail)
    client_name = client_detail[input("Whom you want? ")]
    print(opt)
    opt_sel = opt[input("What you want to (Diet/Exercise)? ")]
    concat_log = client_name + "_" + opt_sel + ".txt"


while True:
    try:
        print(do)
        task = do[input("Do you want to (Log / Retrieve: ): ")]  # Select option for log or retrieve
        if task == "Log":

            option_ask()
            opt_detail = input("Detail: ")
            with open(concat_log, "a") as log_file:
                date_time_str = str(getdate())
                client_write_detail = "\n"+client_name+"\n"+opt_sel+"\n"+"[" + date_time_str + "]"+"\n"+opt_detail
                log_file.write(client_write_detail)
                log_file.write("\n**********")

        elif task == "Retrieve":
            option_ask()

            with open(concat_log) as log_file:
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
