# num1 = 0
# num2 = 1
#
# for x in range(10):
#     print(num1,end=",")
#     ser = num1 + num2
#     num1 = num2
#     num2 = ser


def fibonacci(fib):
    "To Print Fibonnaci Numbers"
    fibs = [0,1]
    for i in range(fib):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

print(fibonacci(10))
print(fibonacci.__doc__)