class Person:
    def __init__(self,name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    # return ("Hi my name is",person.name, "and i am",person.gender)
    print("Hi my name is {} and I am {}".format(person.name,person.gender))
    p1 = Person("Faiza", "Female")
    return p1 # A function return and object of a class

p = Person("Atif", "Male")
x = greet(p)
greet(p) # Pass class object as an input to a function
print(x.name)
print(x.gender)
        