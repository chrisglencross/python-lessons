import random
import time

def input_number(prompt):
    while True:
        try:
            print(prompt)
            number=int(input("> "))
            break
        except ValueError:
            print("Oops! That wasn't a valid number. Try again.")
    return number

def ask_times_table(num1, num2):
    answer=input_number("What is " + str(num1) + " x " + str(num2) + "?")
    if answer==num1*num2:
        print("Correct!")
        return True
    else:
        print("Wrong, the answer is", num1*num2)
        return False

def do_times_table_test(table):
    questions=list(range(1, 13))
    random.shuffle(questions)

    correct=0
    start_time=time.time()

    for question in questions:
        print()
        if ask_times_table(table, question):
            correct=correct+1

    end_time=time.time()
    
    duration=end_time-start_time

    # Bonus score if you took less than 60 seconds
    if duration<60:
        score_multiplier=1+3*(60-duration)/60
    else:
        score_multiplier=1
    score=correct*score_multiplier

    print()
    print("You got", correct, "sums correct in", int(duration), "seconds")
    print("This means you scored", int(score), "points!")
    print()

# Main game loop
while True:
    table=input_number("Which times table do you want to try?")
    do_times_table_test(table)
