import random

name = "John"
question = ""
answer = ""
random_number = random.randint(1, 11)
#print(random_number)

#Control flow
if (random_number == 1) and (question != ""):
  answer = "Yes - definitely."
elif (random_number == 2) and (question != ""):
  answer = "It is decidedly so."
elif (random_number == 3) and (question != ""):
  answer = "Without a doubt."
elif (random_number == 4) and (question != ""):
  answer = "Reply hazy, try again."
elif (random_number == 5) and (question != ""):
  answer = "Ask again later."
elif (random_number == 6) and (question != ""):
  answer = "Better not tell you now."
elif (random_number == 7) and (question != ""):
  answer = "My sources say no."
elif (random_number == 8) and (question != ""):
  answer = "Outlook not so good."
elif (random_number == 9) and (question != ""):
  answer = "Very doubtful."
elif (random_number == 10) and (question != ""):
  answer = "Not so sure."
elif (random_number == 11) and (question != ""):
  answer = "Definitely not."
else:
  answer = "Error"

#Seeing the result
if (answer != "Error"):
  if (name == ""):
    print("Question:", question)
    print("Magic 8-Ball's answer:", answer)
  else:
    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)
else:
  print("There is an error in your inputs. Try to check the question variable.")