while True:
    try:
        apples = int(input("Enter the number of apple I got: "))
        min_no = int(input("Enter the minimum number in range: "))
        max_no = int(input("Enter the maximum number in range: "))
    except ValueError:
        print("Numbers Only!")
        continue
    if min_no >= max_no:
        print(f"This is not a range {apples / max_no}, minimum should be less than maximum")
    else:
        for x in range(min_no, max_no+1):
            if apples % x == 0:
                print(f"{x} is the divisor of {apples}")
            else:
                print(f"{x} is not divisor by {apples}")
        exit()
