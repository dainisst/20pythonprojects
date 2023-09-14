# dictionary that stores question and answers
# have a variable that tracks the score of the palyer
# loop through the dictionary using the key values pairs
# display each question of the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
  "question1": {
    "question": "What is the capital of France?",
    "answer": "Paris"
  },
  "question2": {
    "question": "What is the capital of Germany?",
    "answer": "Berlin"
  },
  "question3": {
    "question": "What is the capital of Italy?",
    "answer": "Rome"
  },
  "question4": {
    "question": "What is the capital of Spain?",
    "answer": "Madrid"
  },
  "question5": {
    "question": "What is the capital of Portugal?",
    "answer": "Lisabon"
  },
  "question6": {
    "question": "What is the capital of Austria?",
    "answer": "Vienna"
  }
}

score = 0

for key, value in quiz.items():
  print(value["question"])
  answer = input("Answer? ")

  if answer.lower() == value["answer"].lower():
    print("Correct")
    score = score + 1
    print(f"Your score is: {str(score)}")

  else:
    print("Wrong")
    print(f"The correct answer is {value['answer']}")
    print(f"Your score is: {str(score)}")

print(f"You got {score} out of 6 questions")
print(f"Your percentage is {str(int(score / 7 * 100))}%")