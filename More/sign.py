# sign Up / Sign In

user = {"atif": '1001', "faisal": '1002', "arshad": '1003'}
print(user)

while True:
    confirm = input("""Do you want to "Sign In" or "Sign Up? (I/U)""")
    if confirm == "U":
        print("Sign up!")
        user_name = input("Create user name: ")

        if user_name not in user:
            user_pin = input("Create user PIN: ")
            user[user_name] = user_pin

        elif user_name in user:
            print("User Already Exist")
            user_confirm = input("Do you want try for another user (y/n: ")
            if user_confirm == "y" or "Y": continue

            else:
                print("Better luck next time")
                break

    elif confirm == "I":
        print("Sign In!")
        break

    print(user)