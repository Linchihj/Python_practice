import random

#variables
name = input("Enter your name:")
question = input ("Question:")
print ("")

answer = ""

#question output
if name == "":
  print (question)
else:
  print (name, "asks:", question)

#answer output
random_number = random.randint (1, 12)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "In the near future"
elif random_number == 11:
  answer = "In a few days"
elif random_number == 12:
  answer = "Uncertain outlook"
else:
  print ("ERROR")

if question == "":
  print ("You didn't ask me anything")
else:
  print ("Magic 8-Ball's answer:" + answer)