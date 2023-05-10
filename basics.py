# define the function with def
# than name the function, in this example we used get_choices
# a function always needs () as well as a : to work

import random

def get_choices():
    #than indent the below to make it apart of the function
    player_choice = input("Enter a choice (rock, paper, scissors)")

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
    #putting a blank line as a choice, just to make it easier to read, the computer does not care
    #indentations do matter, they do care

    return choices
choices = get_choices()

print(choices)

#if statements
#concatanation
#else and elif statements

def check_win(player, computer):
    #below is an fstring
    print(f"You chose {player} and the computer chose {computer}")
    if player == computer:
    elif player == "rock":
        if computer == "scissors":
            return "ROCK SMASHES SCISSORS! YOU WIN BABY"
    else:
        return "paper covers rock! you lose!"
        
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! YOU WIN BABY"
        else:
            return "scissors cuts paper! you lose!"

    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! YOU WIN BABY"
        else:
    return "rock crushes scissors! you lose!"

choices = get_choices()

    

    
 






