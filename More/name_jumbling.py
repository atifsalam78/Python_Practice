"""
The task you have to perform is “Jumbled Funny Names”. This task consists of a total of 20 points
to evaluate your performance.

Problem Statement:-
It's result day at school and not everyone is happy. You decided to make your friends laugh by jumbling their names
to come up with some funny names.

Your program should take the number of names and the names separated by space as input. Output should be funny names
in the same order.

Input:
Enter number of friends:

3

Enter the name of your 3 friends:

Rohan Das

Shubham Agarwal

Ritesh Arora

Output:
Ritesh Das

Shubham Arora

Rohan Agarwal

"""

num_friends = int(input("Enter number of friends: "))
count = 0
friends_list =[]
while count != num_friends:
    name_friends = input("Enter the name of your friends: ")
    friends_list.append(name_friends)
    count += 1

split_name = [i.split() for i in friends_list]
# print(friends_list)
print(split_name)
for index in range(len(split_name)):
    split_name[index-(len(split_name)-(len(split_name)-1))][1] = split_name[index-(len(split_name)-(len(split_name)))][1]


# # split_name[0][1] = split_name[1][1]
# # split_name[1][1] = split_name[2][1]
# # split_name[2][1] = split_name[0][1]

print(split_name)