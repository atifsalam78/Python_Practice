"""
A Simple database
A dictionary with person names as keys. Each person is represented as
another dictionary with the keys 'phone' and 'addr' referring to their phone
number and address, respectively.

"""
people = {
            "atif":   {"phone":"1001","addr":"Shah Faisal No.3"},
            "faisal": {"phone":"1002","addr":"Gulshan-e-Iqbal 13D"},
            "arshad": {"phone":"1003","addr":"Soldier Bazar No.2"},
            "navaid": {"phone":"1004","addr":"Gulistan-e-Johar"}
            }

# Descriptive labels for the phone number and address. These will be used when printing the output.
labels = {
            "phone":"phone number",
            "addr": "address"
         }
name = input("Enter Name: ")

# Are we looking for a phone number or an address?

request = input("Phone Number (p) or Address (a)? ")

# Use the correct key:

if request == "p":
    key = "phone"
if request == "a":
    key = "addr"

# Only try to print information if the name is a valid key in our dictionary:

if name in people:
    print("{}'s {} is {}.".format(name,labels[key],people[name][key]))