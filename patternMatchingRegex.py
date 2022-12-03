import re

if __name__=="__main__":
    # phoneNumberRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")

    phoneNumberRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
    # mo = phoneNumberRegex.search("My number is 415-555-4242.")
    mo = phoneNumberRegex.search("My Number is (415) 555-5462. ")
    # print(mo.group(0))
    # print(mo.group(1))
    # print(mo.group(2))
    # print(mo.group())
    # print(mo.groups())

    areaCode, mainNumber = mo.groups()
    print("Area Code: " + areaCode)
    print("Main Number: " + mainNumber)