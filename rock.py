import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
  options = ["rock", "paper", "scissors"]
  user_input = input("Choose rock, paper, scissros or exit: ")
  computer_input = random.choice(options)

  if user_input == "exit":
    print("Game ended")
    print("you score: ", str(user_points))
    print("computer scores: ", str(computer_points))
    exit = True

  if user_input == "rock":
    if computer_input == "rock":
      print("your input is rock")
      print("computer input is rock")
      print("its a tie!")
    elif computer_input == "paper":
      print("your input is rock")
      print("computer input is paper")
      print("computer wins")
      computer_points += 1
    elif computer_input == "scissors":
      print("your input is rock")
      print("computer input is scissors")
      print("you win")
      user_points += 1

  elif user_input == "paper":
    if computer_input == "paper":
      print("your input is paper")
      print("computer input is paper")
      print("its a tie!")
    elif computer_input == "rock":
      print("your input is paper")
      print("computer input is rock")
      print("you win")
      user_points += 1
    elif computer_input == "scissors":
      print("your input is paper")
      print("computer input is scissors")
      print("computer wins")
      computer_points += 1

  elif user_input == "scissors":
    if computer_input == "scissors":
      print("your input is scissors")
      print("computer input is scissors")
      print("its a tie!")
    elif computer_input == "rock":
      print("your input is scissors")
      print("computer input is rock")
      print("computer wins")
      computer_points += 1
    elif computer_input == "paper":
      print("your input is scissors")
      print("computer input is paper")
      print("you win")
      user_points += 1

  elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
    print("not valid input")