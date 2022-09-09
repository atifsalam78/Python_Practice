# Snake, Water, Gun
import random
score_human = 0
score_computer = 0
opt_human = {"s": "Snake", "w": "Water", "g": "Gun"}
opt_comp = ("Snake", "Water", "Gun")

while True:
    try:
        for key, value in opt_human.items():
            print(f"Press {key} (in small letter) for {value} ")
        task_human = opt_human[input("\nIt's your turn ")]
        task_computer = random.choice(opt_comp)

        if task_human == "Snake" and task_computer == "Water":
            print("You Wins\n")
            score_human += 1
    
        elif task_human == "Water" and task_computer == "Gun":
            print("You Wins\n")
            score_human += 1
    
        elif task_human == "Gun" and task_computer == "Snake":
            print("You Wins\n")
            score_human += 1
        
        elif task_human == task_computer:
            print("Tie\n")            

        else:
            print("Computer Wins\n")
            score_computer += 1
    
        cont = input("Do you want to continue (Y/N)? ")
        if cont == "y" or cont == "Y":
            print("Never Give up, experience more dare!\n")
            continue
        else:
            print("Game Over!\n")
            print("You Scored:", score_human)
            print("Computer Scored:", score_computer)
            if score_human < score_computer:
                print("Computer Wins!\n")
                
            elif score_human == score_computer:
                print("It's a Tie")
                                
            elif score_human > score_computer:
                print("You Wins!\n")
            break
                
    except ValueError:
        print("Enter Correct Value\n")
    except IndexError:
        print("Enter Correct Index Value\n")
