def jumbleName(friends_list):
    """Return jumbled name from list"""
    split_name = [i.split() for i in friends_list]
    for index in range(len(split_name)):
        split_name[index-(len(split_name)-(len(split_name)-1))][1] = split_name[index-(len(split_name)-(len(split_name)))][1]

    return split_name

num_friends = int(input("Enter number of friends: "))
count = 0
friends_list =[]
while count != num_friends:
    name_friends = input("Enter the name of your friends: ")
    friends_list.append(name_friends)
    count += 1

print(jumbleName(friends_list))