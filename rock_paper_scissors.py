import random

user_Wins = 0
Computer_wins =0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quite: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer_picked", computer_pick + ".")

    if user_input =="rock" and computer_pick == "scissors":
        print('You won!')
        user_Wins += 1
        
    elif user_input =="paper" and computer_pick == "rock":
        print('You won!')
        user_Wins += 1

    elif user_input =="scissors" and computer_pick == "paper":
        print('You won!')
        user_Wins += 1
        
    else:
        print(" You lost!")
        Computer_wins += 1

print("You won", user_Wins, "times,")
print("The computer won", Computer_wins, "times")
print("Goodbye!")
