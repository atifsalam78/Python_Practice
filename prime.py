def is_prime(start,end):
    """To check the range of prime numbers"""
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):

        if num > 1: # all prime numbers are greater than 1, if number is less than or equal to 1, it is not prime
            for i in range(2, num):  # check for factors
                if (num % i) == 0: # not a prime number so break inner loop and, look for next number
                    break
            else:
                print(num)

print(is_prime(1,10))
print(is_prime.__doc__)