def age_calculator(name, age):
    future_age = (1978-1) + 100
    return "Hello Mr. {}, you will turn 100 in the year {}".format(name, future_age)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(age_calculator(name, age))