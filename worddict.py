# have a python dictionary that has a key/value pair that requests a word and its definition
# collect input from the user inpput is a word
# check if the word is in the dictionary
# print the fefinition

# def main():
#   word_dictionary = {
#     'hi': 'a way of greeting',
#     'eyes': 'an organ to see',
#     'earth': 'a planet in space',
#   }

#   while True:
#     word = input('enter a word: ')
#     if word == "":
#       break
#     if word in word_dictionary:
#       print(word, ":", word_dictionary[word])

# main()

from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
  word = input("enter your word: ")
  if word == "":
    break

  print(dictionary.meaning(word))