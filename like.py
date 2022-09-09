print("Face Book Like & Comments\n")
fb_like = []
while True:
    user_dic = {"atif": "1001",
                "faiza": "1002",
                "manahil": "1003",
                "ayesha": "1004"}

    user = input("Enter User Name: ")
    if user in user_dic.keys():
        pin = input("Enter Your Pin: ")
        if pin == user_dic[user]:
            print("Authenticated!")
            # fb_like = []
            fb_like.append(user)
            if len(fb_like) == 1 or len(fb_like) == 2:
                print(fb_like, "Likes You!")
            else:
                print(len(fb_like), "Likes You!")

        else:
            print("Wrong Pin!")
    else:
        print("Wrong User Name!")
    con = input("Do You Want To Continue (Y/N): ")
    if con == "y" or con == "Y":
        continue

    else:
        print("Thanks! Good Bye, See Yaa.....")
        break