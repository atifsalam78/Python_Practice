import Levenshtein as lev

with open ("plagCorrect.txt", "r") as f1, open ("plagWrong.txt", "r") as f2:
    plagOne = f1.readlines()
    plagTwo = f2.readlines()

def plagiarism(file2, file1):
    for wrongString, correctString in zip(file2, file1):
        plagResults = lev.ratio(wrongString.lower(), correctString.lower())
        plagRatio = round(plagResults*100, 2)
    if plagRatio >= 50:
        print(f"Significant plagiarism ratio found: {plagRatio}%")
    
    elif plagRatio < 50:
        print(f"Minimal significant plagiarism ratio found: {plagRatio}%")

    elif plagRatio == 0:
        print(f"No plagiarism ratio found: {plagRatio}%")


if __name__ =="__main__":    
    plagiarism(plagTwo, plagOne)