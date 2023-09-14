# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# whil loop to continue the program until the user want to exit

def add(a, b):
  answer = a + b
  print(f"{str(a)} + {str(b)} = {str(answer)}\n")

def sub(a, b):
  answer = a - b
  print(f"{str(a)} - {str(b)} = {str(answer)}\n")

def mul(a, b):
  answer = a * b
  print(f"{str(a)} * {str(b)} = {str(answer)}\n")

def div(a, b):
  answer = a / b
  print(f"{str(a)} / {str(b)} = {str(answer)}\n")

while True:
  print("A. Addition")
  print("B. Subtraction")
  print("C. Multiplication")
  print("D. Division")
  print("E. Exit")

  choice = input("input choice: ")

  if choice == "a" or choice == "A":
    print("Addition")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a, b)
  elif choice == "b" or choice == "B":
    print("Subtraction")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    sub(a, b)
  elif choice == "c" or choice == "C":
    print("Multiplication")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    mul(a, b)
  elif choice == "d" or choice == "D":
    print("Division")
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    div(a, b)
  elif choice == "e" or choice == "E":
    exit()
