import random

guesses=0
got_answer=False
value=random.choice(range(0,100))+1

while not got_answer:

   guess_str=input("Make a guess: ")
   try:
       guess=int(guess_str)
   except ValueError:
       print("That's not a number!")
       continue

   guesses = guesses+1
   if guess < value:
       print("Higher!")
   elif guess > value:
       print("Lower!")
   else:
       got_answer=True

print("You got the correct answer in " + str(guesses) + " guesses.")
