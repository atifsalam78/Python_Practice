def next_palindrome(n):
    """Calculate next palindrome of given number"""
    n = n+1
    while not ispalindrome(n):
        n +=1
    return n      

def ispalindrome(n):
    """Validate the string is palindrome or not"""
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    n = int(input("Number of test cases:"))
    numbers = []

    for _ in range(n):    
        number = int(input("Enter number to be test: "))
        numbers.append(number)

    for i in range(n):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
    

