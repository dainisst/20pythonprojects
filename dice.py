# import random
# define function to roll the dice
# create dictionary that will have the drawing of the dice
# while loop to ask user to continue

import random

def roll_dice():

  roll = input("roll dice (yes/no)")

  while roll.lower() == "yes".lower():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("dice rolled: {} and {}".format(dice1, dice2))

    roll = input("roll again: (yes/no)")

roll_dice()