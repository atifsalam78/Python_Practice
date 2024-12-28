import re

def isPhoneNumber(text):
    '''Identify the american pattern phone number in text'''
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != "-":
        return False
        for i in range(4,7):
            if not text[i].isdecimal():
                return False
    
    if text[7] != "-":
        return False
        for i in range(8,12):
            if not text[i].isdecimal():
                return False
    return True

if __name__=="__main__":
    message = 'Call me at 415-555-1011 tomorrow. 012-345-6789 is my office.'
    # for i in range(len(message)):
    #     chunk = message[i:i+12]
    #     if isPhoneNumber(chunk):
    #         print("Phone Number Found: " + chunk)
    # print("Done")

    """Creating REGEX object"""
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumberRegex.search(message)
    print("Phone Number Found: " + mo.group())