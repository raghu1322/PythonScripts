##My First python code for playing Rock, Scissor and paper with Computer

import random

UserScore = 0
ComputerScore = 0
ComputerList = ["rock","paper","scissor"]

UserConcent = input("Do you want to play game with computer(Yes/No)? ").lower()

if UserConcent != 'yes':
    print("You opted out game")
    quit()

else:

    while True:
        ComputerChoice = random.choice(ComputerList)
       ## print("Computer choose: ", ComputerChoice,"!!")

        while True:
            User_Input = input("Type either Rock, Scissor or paper: ").lower()
            if User_Input == ComputerChoice:
                print("You Got It Correct.")
                UserScore += 1
                break
    
            else:
                print("Try Again")
                ComputerScore += 1
                continue
    
        if UserScore > ComputerScore:
            print("Your Score:", UserScore, "& Computer Score:", ComputerScore, "and you Won!!")
            UserConcent = input("Do you want to play again? ").lower()
            if UserConcent != 'yes':
                print("You opted out game")
                quit()

            else:
                continue
        else:
            print("Your Score:", UserScore, "& Computer Score:", ComputerScore, "and you Lost!!")
            UserConcent = input("Do you want to play again? ").lower()
            if UserConcent != 'yes':
                print("You opted out game")
                quit()

            else:
                continue

