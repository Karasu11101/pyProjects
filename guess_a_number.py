import random

player_score = 0
attempts = 0

def show_score():
    print(f"Thanks for playing. Your score is {player_score}. You made {attempts} attempts. ")

def gen_rnd_num():
    rnd = random.randint(0, 10)
    return rnd

print("Welcome to the game! \n")
random_number = gen_rnd_num()

while True:

    player_number = input("Type your guess to begin or press q to quit: ").lower()

    if player_number.isdigit():
    
        if int(player_number) == random_number:
            print("You guessed right!")
            attempts += 1
            player_score += 1

            restart_game = input("Do you want to play another round? Y/N ").lower()
            if restart_game == "y":
                random_number = gen_rnd_num()
                continue
            else:
                show_score()
                break

        elif int(player_number) > random_number:
            print("Your guess is above the number. \n" )
            attempts += 1
            continue

        elif int(player_number) < random_number:
            print("Your guess is below the number. \n")
            attempts += 1
            continue

    elif player_number == "q":
        break

    else:
        print("Invalid input. Please, type a number. \n")
        continue
