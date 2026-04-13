print( "="*30)
print(" ROCK PAPER SCISSORS GAME    ")
print("="*30)
print("INSTRUCTIONS")
print("-choose any one of three - rock, paper or scissors")
import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("What is your choice ? ")
    user_choice = user_choice.strip().lower()

    if user_choice in choices:
        computer = random.choice(choices)

        print("YOUR CHOICE : ", user_choice)
        print("COMPUTER CHOICE : ", computer)

        if user_choice == computer :
            print("TIE")
        elif (user_choice == "rock" and computer=="scissors") or (user_choice == "paper" and computer == "rock") or (user_choice == "scissors" and computer == "paper"):
            print("YOU WIN") 
        else:
            print("COMPUTER WIN")
    else:
        print("INVALID!CCHOOSE ROCK, PAPER OR SCISSORS.")
    user_con = input("\nDO YOU WANT TO CONTINUE YES OR NO ? ")
    user_con = user_con.strip().lower()
    
    if user_con not in ["y","Yes","yes"]:
        print("EXITING GAME")
        break
