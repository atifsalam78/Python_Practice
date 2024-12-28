predict_year = 2090
current_year = 2022


def age_cal(age):
    """Identify realistic age"""
    if age >= current_year:
        print("You are not yet born")
    elif age < 1890:
        print(f"Definitely you were not in the year {user_input}")
    elif age >= 1930:
        print(f"You will turn {predict_year - age} in the year {predict_year}")
    elif age >= 1890 and age <= 1929:
        print(f"You are the most oldest person alive in the year {current_year}")
    else:
        print(f"No one is alive from {age}")


try:
    user_input = input("""Enter your "Age" or "Year" of birth: """)
    if len(user_input) <= 2 or int(user_input) <= 132:
        age = current_year - int(user_input)
        age_cal(age)
    elif len(user_input) == 4 and int(user_input) > 130:
        age = int(user_input)
        age_cal(age)
    else:
        print(f"No one is alive from the year {current_year - int(user_input) }")
except ValueError as e:
    print(e)
try:
    user_input = input("""Enter "Year" optional: """)
    if user_input != "":
        if len(user_input) <= 2 or int(user_input) <= 130:
            print("This is not a year")
        else:
            age = int(user_input)
            age_cal(age)
except ValueError as e:
    print(e)
