# class Vehicle:
#     "Parent class for vehicle"
#     make = "Honda" # Class variable, sole property of class
#
#     def __init__(self, vname, vmodel, vcc, vcolor): # Constructor
#         self.name = vname # vname is argument and slef.name is instance variable
#         self.model = vmodel
#         self.cc = vcc
#         self.color = vcolor
#
#     def print_details(self): # Method
#         return f"This is {self.name} and model is {self.model} having {self.cc} engine in {self.color} color from {self.make}"
#
#     @classmethod
#     def change_make(cls, new_make):
#         cls.make = new_make
#
#     @classmethod # class method as an alternative constructor
#     def from_dash(cls, string):
#         params = string.split("-")
#         print(params)
#         return cls(params[0], params[1], params[2], params[3])
#
#     @staticmethod
#     def show_room_detail():
#         return "Shara-e-Faisal"
#
#
# bus = Vehicle("Mazda", 2018, 1600, "Black") # Instance or Object of class
# car = Vehicle("Audi", 2019, 1000, "Purple")
# bike = Vehicle.from_dash("Hero-2020-70-Red")
#
# # print(bus.print_details())
# # bus.change_make("Toyota")
# # print(bus.print_details())
# # Vehicle.change_make("Suzuki")
# # print(bus.print_details(), bus.show_room_detail())
#
# print(bike.print_details())
#
#
#
#
#

class A:
    classvar1 = "I am a class variable in class A" # Public
    _age = 10 # Protected
    __income = 1000 # Private

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance Variable in class A"
        self.special = "Special"


class B(A):
    classvar1 = "I am a class variable in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance Variable in class B"

a = A()
b = B()
print(b.var1, b.classvar1, b.special)
print(a.classvar1)
print(a._age)
print(a._A__income)