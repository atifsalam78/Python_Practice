import Levenshtein as lev

with open ("cities.csv", "r") as f1, open ("citiesWrong.csv", "r") as f2:
    city1 = f1.read().split("\n")
    city2 = f2.read().split("\n")

def levMatches(file2, file1):
    for wrongString, correctString in zip(file2, file1):
        results = lev.ratio(wrongString.lower(), correctString.lower())
        print(f"{wrongString}, Levenshtein Ratio: {results*100}% from {correctString}")

if __name__ =="__main__":    
    levMatches(city2, city1)