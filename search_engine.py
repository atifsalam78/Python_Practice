"""
The task you have to perform is “Search Engine”. This task consists of a total of 20 points to evaluate your performance.

Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. The most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
3 results found:

python is not python snake
python is good
Python is cool
Solving challenges will make you a great problem solver and will improve your coding skills.
"""

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


