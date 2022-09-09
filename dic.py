dic = {"abandon": "surrender",
       "mutable": "liable to change",
       "endure": "remain in existence",
       "novice": "inexperienced",
       "iterate": "perform or utter repeatedly"}

count = ""

try:
    value = dic[input("Word: ")]
    print("meaning is:-", value)
    count = input("Want to Search Another (Y/N) ?")

except KeyError:
    print("Word not exist!")

while count == "y":
    continue