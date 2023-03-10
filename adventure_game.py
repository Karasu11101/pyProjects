choices = {
    1: "You wake up in an unfamiliar place. Before you a forked road stretches far in the distance. Where do you go? (left/right) ",
    2: "You walk up the road on the left, until your reach what looks like an abandoned house. Do you enter or move forward? (enter/forward) ",
    3: "You enter the house, and find three chests under a pile of rubble. Which one do you open? (left/middle/right) ",
    4: "You proceed on the path to your right, it leads to the edge of a forest. Do you wish to enter the forest or keep following the road? (forest/road) ",
    5: "You move forward along the path, until you see a crop field stretching in all directions, as far as your eyes can see. Do you enter the field or go back? (field/back) ",
    6: "You open the chest on the left, and find a dusty sheat with a sharp dagger inside. Do you want to open another chest? (middle/right) "
}

save_slot_1 : 1
save_slot_2 : 1

player_name = input("Welcome traveler! What is your name? ")

def save_game():
    pass

def start_game():

    while True:

        choice = input(choices[save_slot_1])

        if choice == "left":
            save_slot_1 = 2
            choice = input(choice[2])
        elif choice == "right":
            save_slot_1 = 4
            choice = input(choice[4])
        else:
            print("Invalid input")
            continue


def load_game():
    pass

def initial_menu():
    option = input("Do you want to start a new game or load a save? (new/load) ")
    if option == "new":
        start_game()
    else:
        load_game()

