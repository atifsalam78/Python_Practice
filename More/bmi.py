def bmi():
    # [weight(kg) / height(cm) / height(cm)] x 10,000
    # mass1 = (weight / height)
    # mass2 = (height * 10000)
    # mass3 = float(mass1 / mass2)
    # print("Your BMI is %.2f"%mass3)

    weight = float(input("Weight (kgs): "))
    height = float(input("Height (cm): "))
    mass = (weight / height / height) * 10000
    print("Your BMI is %.2f" %mass)


bmi()