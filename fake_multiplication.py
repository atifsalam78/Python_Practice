import random


def multiPlication(num):
    """Return list of table having a random index wrong multiplication"""
    random_num = random.randint(1,9)
    lst_multi = [i * num for i in range(1,11)]
    lst_multi[random_num] = lst_multi[random_num] + random.randint(0,10)
    return lst_multi


def isCorrect(table, num):
    """Identify and return the index value of wrong multiplication"""
    for i in range(1,11):
        if table[i-1] != i * num:
            return i -1
    # If all values are correctly multiplied than return none
    return None


if __name__ == '__main__':
    num = int(input("Enter Number: "))
    myTable = multiPlication(num)
    print(myTable)
    wrongIndex = isCorrect(myTable, num)
    print(f"The table has wrong value at index {wrongIndex}")
