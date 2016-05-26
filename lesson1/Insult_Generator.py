import random

people=["Harry", "Ron", "Hermione", "Ginny", "Fred", "George"]
adjectives=["hot", "cold", "smelly", "green", "wet", "damp", "cool", "nice"]
things=["toad", "rat", "cat", "monkey", "owl", "banana", "muggle"]

print("Here are your insults:")

count=1
while count <= 20:

    person=random.choice(people)
    adjective=random.choice(adjectives)
    thing=random.choice(things)
    insult=person + " is a " + adjective + " " + thing  + "."
    print(count, insult)

    count=count+1
