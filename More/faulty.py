space = " " * 40
print('%s*******************' % space)
print('%s Faulty Calculator' % space)
print('%s*******************' % space)
while True:

    op = {"+": "addition", "-": "subtraction", "*": "multiplication", "/": "division"}
    num1 = float(input("Enter First Number: "))
    choice = op[input("Enter Your choice: ")]
    num2 = float(input("Enter Second Number: "))

    # except (45*3 = 555, 56+9 = 77, 56/6 = 4)

    if choice == "multiplication" and num1 == 45 and num2 == 3:
        print(555)

    elif choice == "addition" and num1 == 56 and num2 == 9:
        print(77)

    elif choice == "division" and num1 == 56 and num2 == 6:
        print(4)

    elif choice == "addition":
        print(num1 + num2)

    elif choice == "subtraction":
        print(num1 - num2)

    elif choice == "multiplication":
        print(num1 * num2)

    elif choice == "division":
        print(num1 / num2)

    con = input("Do You Want To Continue (Y/N): ")

    if con == "y" or con == "Y":
        continue

    else:
        print("Good Bye!\nThanks for using")
        break