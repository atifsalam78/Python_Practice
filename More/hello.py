import random, string
guess_count = 0
score_win = 0
score_fail = 0
while True:
    ran_num = "".join(random.sample(string.digits,5))
    print(ran_num)
    guess_num = input("Guess The number:")
    if guess_num == ran_num:
        print("Great")
        score_win += 1
        break
    else:
        print("Fail!")
        score_fail += 1
        continue
print("Total Wins",score_win)
print("Total Fails",score_fail)
print("Total Guess",score_win+score_fail)