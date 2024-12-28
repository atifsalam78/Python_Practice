import re

txt = "The rain in Spain in 1920! after the world war_I, is this true?"
txt2 = "hello planet"
txt3 = "helllllllo world"
txt4 = "The rain in Spain falls mainly in the plain!"

#Metacharacters

#Search the string to see if it starts with "The" and ends with "Spain":
# x = re.search("^The.*Spain$", txt)

#Find all lower case characters alphabetically between "a" and "m":
# x = re.findall("[a-m]", txt)

#Find all digit characters:
# x = re.findall("\d", txt)

#Search for a sequence that starts with "wo", followed by two (any) characters, and an "d":
# x = re.findall("wo..d", txt)

#Check if the string starts with 'The':
# x = re.findall("^The", txt)

#Check if the string ends with 'war':
# x = re.findall("war$", txt)

#Search for a sequence that starts with "he", followed by 0 or more (any) characters, and an "o":
# x = re.findall("he.*o", txt2)
# x = re.findall("af.*r", txt)
# x = re.findall("3.*o", txt3)

#Search for a sequence that starts with "he", followed by 1 or more (any) characters, and an "o":
# x = re.findall("he.+o", txt2)
# x = re.findall("af.+r", txt)
# x = re.findall("3.+o", txt3)

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
# x = re.findall("he.?o",txt2) #This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# x = re.findall("he.{2}o",txt2)
# x = re.findall("he.{2}o",txt3) # Not matched

#Check if the string contains either "falls" or "stays":
# x = re.findall("falls|stays",txt4)
# x = re.findall("Spain|Mexico",txt)

#Special Sequences

#Check if the string starts with "The":
# x = re.findall("\AThe",txt)

#Check if "ain" is present at the beginning of a WORD:
# x = re.findall(r"\bain",txt)

#Check if "ain" is present at the end of a WORD:
# x = re.findall(r"ain\b", txt)

#Check if "ain" is present, but NOT at the beginning of a word:
# x = re.findall("\Bain", txt)

#Check if "ain" is present, but NOT at the end of a word:
# x = re.findall(r"ain\B", txt)

#Check if the string contains any digits (numbers from 0-9):
# x = re.findall("\d", txt)

#Return a match at every no-digit character:
# x = re.findall(r"\D", txt)

#Return a match at every white-space character:
# x =re.findall("\s",txt)

#Return a match at every NON white-space character:
# x = re.findall("\S", txt)

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
# x = re.findall("\w", txt)

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# x = re.findall("\W", txt)

#Check if the string ends with "Spain":
# x = re.findall("Spain\Z", txt)
# x = re.findall("world\Z", txt3)

#Sets

#Check if the string has any a, r, or n characters:
# x = re.findall("[arn]",txt)

#Check if the string has any characters between a and n:
# x = re.findall("[a-n]", txt2)

#Check if the string has other characters than a, r, or n:
# x = re.findall("[^arn]", txt)

#Check if the string has any 0, 1, 2, or 3 digits:
# x = re.findall("[0123]", txt)

#Check if the string has any digits:
# x = re.findall("[0-9]", txt)

#Check if the string has any two-digit numbers, from 00 to 59:
# x = re.findall("[0-5][0-9]", txt)


#Check if the string has any characters from a to z lower case, and A to Z upper case:
# x = re.findall("[a-z,A-Z]", txt)

#Check if the string has any + characters:
x = re.findall("[+]", txt)

if x:
    print(f"Yes! we have matched {x}")
else:
    print("Not matched")

