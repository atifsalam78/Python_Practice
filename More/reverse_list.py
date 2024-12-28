size_list = int(input("Enter the size of the list: "))
lst = []
for _ in range(size_list):
    lst.append(int(input("Enter the element of the list: ")))
print(f"{lst} is the original list")

# First Method
reverse1 = lst[:]
reverse1.reverse()
print(f"The original list{lst} after reversed {reverse1}")

# Second Method
reverse2 = lst[::-1]
print(f"The original list{lst} after reversed {reverse2}")


# Third Method(Swap)
reverse3 = lst[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i -1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse4}")

print(f"The original list{lst} after reversed {reverse3}")


if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result!")

# Fourth Method
# reverse4 = lst[:]
# print(f"the original list{lst} after reversed {list(reversed(reverse4))}")

# Fifth Method(Swap) This is gives error, it works with hardcode means without input
# reverse5 = lst[:]
# reverse5[0] = lst[-1]
# reverse5[1] = lst[-2]
# reverse5[2] = lst[-3]
# reverse5[3] = lst[-4]
# reverse5[4] = lst[-5]
# print(reverse5)