from fuzzywuzzy import fuzz
from fuzzywuzzy import process

with open ("cities.csv", "r") as f1, open ("citiesWrong.csv", "r") as f2:
    city1 = f1.read().split("\n")
    city2 = f2.read().split("\n")

def fuzMatches(file2, file1):
    for wrongString, correctString in zip(file2, file1):
        results = fuzz.partial_ratio(wrongString.lower(), correctString.lower())
        print(f"{wrongString}, Fuzz Partial Ratio: {results}% from {correctString}")

if __name__ =="__main__":    
    fuzMatches(city2, city1)