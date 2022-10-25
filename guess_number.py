import random
import os


def clear_screen():
    """Clear screen for all MAC, Linux and Windows"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_in_box(sentence):
    """Prints a sentence in a centered "box" of correct width"""
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) // 2
    print()
    print(' ' * left_margin + '+'  + '-' * (box_width - 2)  +     '+')
    print(' ' * left_margin + '| ' + ' ' * text_width       +  '   |')
    print(' ' * left_margin + '| ' +       sentence         +  '   |')
    print(' ' * left_margin + '| ' + ' ' * text_width       +  '   |')
    print(' ' * left_margin + '+'  + '-' * (box_width - 2)  +     '+')
    print()


if __name__ == '__main__':

    guess_chance = 0
    cont = ""
    while cont != "y" or cont != "Y":
        clear_screen()
        print_in_box("Guess The Number")

        def player(player):
            """Get input from user and show the result on the basis of user input"""
            global guess_chance
            guess_chance = 5
            while guess_chance != 0:
                try:
                    guess = int(input(f"{player} guess the number between (1-100): "))
                except ValueError:
                    print("Only Numbers!")
                    continue

                guess_chance = guess_chance - 1
                if guess == rand_number:
                    print(f"{player} great you have guessed exactly the same")
                    break

                elif guess < rand_number:
                    print(f"{player} you have guessed less and remained {guess_chance} chances")
                    if guess_chance <= 1:
                        print(f"{player} this is your last chance to guess: ")

                elif guess > rand_number:
                    print(f"{player} you have guessed greater and remained {guess_chance} chances")
                    if guess_chance <= 1:
                        print(f"{player} this is your last chance to guess: ")
                        continue

        rand_number = random.randint(1, 100)
        print(rand_number)

        player1 = input("Player 1 enter Your Name: ")
        player1 = player1.capitalize()
        guess_chance_p1 = 5
        player(player1)
        guess_chance_p1 = guess_chance

        player2 = input("Player 2 enter Your Name: ")
        player2 = player2.capitalize()
        guess_chance_p2 = 5
        player(player2)
        guess_chance_p2 = guess_chance

        if guess_chance_p1 == guess_chance_p2:
            print(f"""It's a "Tie" between {player1} and {player2}""")

        elif guess_chance_p1 > guess_chance_p2:
            print(f"Congratulations {player1} you guessed in {guess_chance_p1} chances and wins!")
            print(f"{player2} better luck next time")

        elif guess_chance_p1 < guess_chance_p2:
            print(f"Congratulations {player2} you guessed in {guess_chance_p2} chances and wins!")
            print(f"{player1} better luck next time")

        
        cont = input("Do you want to continue (Y/N): ")
        if cont == "y" or cont == "Y":
            print("Great you want to dare more....")
            input("")

        else:
            print("Game Over!")
            break