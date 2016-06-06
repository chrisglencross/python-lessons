import textwrap

# This dictionary contains the map of the school.
#
# Each entry in the dictionary is a room or other location. The key is the
# room name ("the_office"), and the value is another dictionary containing
# properties of that room, as follows:
#
#   description: the text to be displayed when the player walks into this room.
#
#   north, south, east, west: optional entries specifying the name of the room
#       that the player arrives at when walking out of this room. If not
#       specified, then the player cannot go that way. It is possible to
#       arrive back at the same room; see maze1 and maze2!
#
school_map={
    "the_office": {
        "description": "You are standing outside the school office. You are surrounded by gleaming sofas made of solid gold. Paths lead in all directions.",
        "north": "east_gate",
        "east": "staff_room",
        "west": "corridor",
        "south": "hall"
    },
    "east_gate": {
        "description": "You are standing outside the main door to the school. Your escape to the road is blocked by a deep muddy trench from The Great War. Beyond the trench you can see barbed wire across no-man's land. The door to the school is south.",
        "south": "the_office"
    },
    "staff_room": {
        "description": "You are in the staff room. There is a strong smell of garlic, socks and chocolate digestives. The only door leads west.",
        "west": "the_office"
    },
    "hall": {
        "description": "You are in the Great Viking Hall of Stamford Green. Long oak tables with silver goblets are lie across the room ready for a banquet, and Valkyries soar overhead. A sign on the wall says that the value of the month is 'Pillaging'. The office is north.",
        "north": "the_office"
    },
    "corridor": {
        "description": "You are in a corridor leading towards the West Wing. Cones, sirens, flashing lights and a 'DO NOT ENTER' sign suggest that construction is not quite finished. To the west, where the building should be, there is a currently a deep hole in the ground. You cannot see the bottom of the pit. A path east leads back to the office.",
        "east": "the_office",
        "west": "tunnel"
    },
    "tunnel": {
        "description": "You are in a tunnel at the bottom of a pit, with a dark passage to the north, and a light to the east. Scratched on the wall are the cryptic letters 'AshLEy wiL nvR WIN'.",
        "east": "corridor",
        "north": "maze1"
    },
    "maze1": {
        "description": "You are in an underground maze of twisting passages, all alike.",
        "east": "tunnel",
        "west": "maze2",
        "north": "maze1",
        "south": "maze2"
    },
    "maze2": {
        "description": "You are in an underground maze of twisting passages, all alike. You can feel a warm gentle breeze.",
        "east": "maze1",
        "west": "maze2",
        "north": "maze1",
        "south": "escape"
    },
    "escape": {
        "description": "You emerge into daylight at the top field beside a running track. The West Gate is open."
    }
}

def look():
    '''
    Prints the description of the room named by the global variable 'location'.
    '''
    formatted_description=textwrap.fill(school_map[location]["description"])
    print(formatted_description)

def go(direction):
    '''
    Returns the name of the room in the given direction ('north', 'east', 'south' or 'west')
    from the player's current location, or None if the player cannot go that way.
    '''
    next_location=school_map[location].get(direction)
    if next_location == None:
        print("You can't go that way.")
    return next_location

def help():
    print("Escape From Stamford Green!")
    print("---------------------------")
    print("Instructions:")
    print("1. Use 'north', 'east', 'south' or 'west' (or 'n', 'e', 's' or 'w') to move.")
    print("2. Type 'look' to see what you can see.")
    print("3. Display this message again by typing 'help'.")

# The main part of the program starts here
help()
print()

location="the_office" # Global variable containing the player's current location
look()

while location != "escape":
    
    print()
    command=input("> ").lower()

    move_to_location=None
    if command=="north" or command=='n':
        move_to_location=go("north")
    elif command=="south" or command=='s':
        move_to_location=go("south")
    elif command=="east" or command=='e':
        move_to_location=go("east")
    elif command=="west" or command=='w':
        move_to_location=go("west")
    elif command=="look":
        look()
    elif command=="help":
        help()
    else:
        print("I don't understand that! Try 'north', 'south', 'east' or 'west', or 'help'.")

    if move_to_location != None:
        location=move_to_location
        look()

print()
print("Congratulations, you have escaped from Stamford Green!")
