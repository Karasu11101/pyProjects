import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:

    computer_choice = options[random.randint(0, 2)]
    ask_choice = input("Make your choice: 1. rock, 2. paper, 3. scissors (input number). Press Q to quit ").lower()
    
    if ask_choice not in ["1", "2", "3", "q"]:
        print("Invalid input. Please use only input a number from 1 to 3. ")
        continue
    else:
        player_choice = options[int(ask_choice)-1]

    if player_choice == computer_choice:
        restart_game = input("It's a draw! Do you want to play another round? Y/N ").lower()
        if restart_game == "y":
            continue
        else:
            break

    else:
        if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
            player_score += 1
            restart_game = input("You win! Do you want to play another round? Y/N ").lower()
            if restart_game == "y":
                continue
            else:
                break
        else:
            computer_score += 1
            restart_game = input("You lose! Do you want to play another round? Y/N ").lower()
            if restart_game == "y":
                continue
            else:
                break

print(f"Thank you for playing! Your score is {player_score}, while the computer scored {computer_score}.")
