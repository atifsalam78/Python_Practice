# Snake, Water, Gun
"""
Snake wins if water
Water wins if Gun
Gun wins if snake
"""
import random

score_human = 0
score_computer = 0
options = ("snake", "water", "gun")
while True:
    try:
        task_human = options[int(input("It's your turn "))]
        task_computer = random.choice(options)
        print("Human Task:", task_human) #To be remove in final phase
        print("Computer Task:", task_computer)#To be remove in final phase
    
        if task_human == "snake" and task_computer == "water":
            print("You Wins\n")
            score_human += 1
    
        elif task_human == "water" and task_computer == "gun":
            print("You Wins\n")
            score_human += 1
    
        elif task_human == "Gun" and task_computer == "snake":
            print("You Wins\n")
            score_human += 1
        
        elif task_human == task_computer:
            print("Tie\n")            
    
        else:
            print(Computer, "Wins\n")
            score_computer += 1
    
        cont = input("Do you want to continue (Y/N)? ")
        if cont == "y" or cont == "Y":
            print("Never Give up, experience more dare!\n")
            continue
        else:
            print("Game Over!\n")
            print("Scored by you:", score_human)
            print("Scored by computer:", score_computer)
            if score_human < score_computer:
                print("You Loose!\n")
                
            elif score_human == score_computer:
                print("It's Tie")
                                
            elif score_human > score_computer:
                print("Computer Wins!\n")
            break
                
    except ValueError:
        print("Value Error\n")

    except IndexError:
        print("Index Error\n")


