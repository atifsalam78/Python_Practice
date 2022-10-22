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
        numbers.append(int(input("Enter number to be test: ")))

    # If number is greater than 10
    new_list = []
    for element in numbers:
        if element > 10:
            n = next_palindrome(element)
            new_list.append(n)
        else:
            new_list.append(element)

    print(f"Your output list: {new_list}")

    # print(f"Output list: {[numbers[i] if numbers[i] < 10 else next_palindrome(numbers[i]) for i in range(n)]} ")
