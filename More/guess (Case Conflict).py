# Guess The Number - Code with Harry
guess_count = 0
counter = 0
while True:

    num = 18
    guess = int(input("Guess the Number: "))
    if guess == num:
        counter += 1
        print("Hurrah! You Won!")
        break

    else:
        guess_count += 1
        if guess < num:
            print("You have entered less than the actual number")
        if guess > num:
            print("You have entered greater than the actual Number")

        print("Wrong! Keep Trying")
        print(5 - guess_count, "Guesses Left to Try\n")

        if guess_count == 5:
            print("Game Over!\n")
            break

print(counter + guess_count, "Times You Have Tried to Win")