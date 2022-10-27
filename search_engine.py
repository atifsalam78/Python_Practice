# First Method, TIme: 64.2 us
# sentences = ["Python is cool", "python is good", "python is not python snake"]
# search = input("Enter to search: ")
# lst = " ".join(sentences).lower()
# ind = 0
# for word in lst.split():
#     if search in word:
#         ind += 1
# print(f"'{search}' found and occurred {ind} times")
# print(sentences)
# print(lst)


# Second Method, Time: 63.4 us
# def contains_word(s, w):
#     return (' ' + w + ' ') in (' ' + s + ' ')

# if __name__ == "__main__":

#     sentences = ["Python is cool", "python is good", "python is not python snake"]
#     search = input("Enter to search: ")
#     lst = " ".join(sentences).lower()
#     ind = 0
#     print(lst)
#     match = contains_word(lst,search)
#     ind += 1
#     if match == True:        
#         print(f"'{search}' found and occurred {ind} times")


# Third Method, Wall time: 65.7 us
import re
sentences = ["Python is cool", "python is good", "python is not python snake"]
search = input("Enter to search: ")
lst = " ".join(sentences).lower()
match =re.findall(search,lst)
print(f"'{search}' - found {len(match)} times in the text")


