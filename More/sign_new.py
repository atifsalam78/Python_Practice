# sign Up / Sign In

user = {"atif": "1001", "faisal": "1002", "arshad": "1003"}
print(user)

while True:
    try:
        confirm = input("""Do you want to "Sign In" or "Sign Up? (I/U)""")
        if confirm == "U":
            print("Sign up!")
            user_name = input("Create user name: ")
            if user_name not in user:
                user_pin = input("Create user PIN: ")
                user[user_name] = user_pin
                print("User successfully added")
                print(user)
                continue
            elif user_name in user:
                print("User Already Exist")
                user_confirm = input("Do you want try for another user (y/n: ")
                if user_confirm == "y" or "Y":
                    print("Continue")
                    continue
                else:
                    print("Better luck next time")
                    break

        elif confirm == "I":
            print("Sign In!")
            user_name = user[input("User Name: ")]
            user_pin = input("Pin: ")
            user[user_name] = user_pin

            if user_pin in user:
                print("Great")
                continue
            else:
                print("Break")
                user_confirm = input("Do you want try for another user (y/n: ")
                if user_confirm == "y" or "Y":
                    print("Continue")
                    continue
                else:
                    break

    except KeyError:
        print("Enter Valid Key")
    else:
        break



