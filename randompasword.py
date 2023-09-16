# as user if they want to generate pasword or not
# if yes, ask for password length
# generate password
# print pasword
# initial response is no the exit the program

import string 
import random

characters = list(string.ascii_letters + string.digits + "@!@#$%^&*()")

def generate_password():
  password_length = int(input("How long would you liek your password? "))

  random.shuffle(characters)

  password = []

  for x in range(password_length):
    password.append(random.choice(characters))

  random.shuffle(password)

  password = "".join(password)

  print(password)

option = input("Do yo want to generate a password? (Yes/No)")

if option == "yes":
  generate_password()
elif option == "no":
  print("program ended")
  quit()
else:
  print("invalid input, please enter yes or no")
  quit()