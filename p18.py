# roll the dice
import random 

def roll_dice():
    return random.randint(1,6)

def dice_roll_game():
    player_score = roll_dice()
    computer_score = roll_dice()
    
    if (player_score == computer_score):
        print("it is tie ")
        