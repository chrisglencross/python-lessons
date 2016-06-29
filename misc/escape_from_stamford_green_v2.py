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
        "description": "You are in the Great Viking Hall of Stamford Green. Long oak tables with silver goblets are lie across the room ready for a banquet, and Valkyries soar overhead. A sign on the wall says that the value of the month is 'Pillaging'. The office is north. Another doorway leads east.",
        "north": "the_office",
        "east": "kitchen"
    },
    "kitchen": {
        "description": "You are in a kitchen. Flickering strip lighting illuminates filthy work surfaces. A menu for roast maggots slies next to an overflowing sink. An open doorway leads west.",
        "west": "hall"
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
        "south": "top_field"
    },
    "top_field": {
        "description": "You emerge into daylight at the top field beside a running track. There is a hole to the north.",
        "west": "escape",
        "north": "maze2"
    },
    "escape": {
        "description": "You have left the school by the west gate."
    }
}

objects={
    "meat": {
        "name": "a piece of uncooked meat",
        "synonyms": {"meat", "uncooked meat"},
        "can_take": True,
        "location": "kitchen"
    },
    "key": {
        "name": "a metal key",
        "synonyms": {"key", "metal key"},
        "can_take": True,
        "location": "staff_room"
    },
    "dog_awake": {
        "description": "A black dog with two heads guards the pit.",
        "name": "a dog",
        "synonyms": {"dog"},
        "can_take": False,
        "location": "corridor"
    },
    "dog_asleep": {
        "description": "A black dog is asleep in the corner.",
        "name": "a sleeping dog",
        "synonyms": {"dog"},
        "can_take": False,
        "location": "corridor",
        "hidden": True
    },
    "gate_locked": {
        "description": "You can see the west gate which is locked.",
        "name": "gate",
        "synonyms": {"gate", "west gate"},
        "can_take": False,
        "location": "top_field"
    },
    "gate_open": {
        "description": "The west gate is open.",
        "name": "gate",
        "synonyms": {"gate", "west gate"},
        "can_take": False,
        "location": "top_field",
        "hidden": True
    }
}

def look():
    '''
    Prints the description of the room named by the global variable 'location'.
    '''
    description=school_map[location]["description"]

    objects_with_descriptions=[]
    objects_to_list=[]
    for obj_properties in objects.values():
        if obj_properties.get("location") == location and obj_properties.get("hidden") != True:
            if "description" in obj_properties:
                objects_with_descriptions.append(obj_properties)
            else:
                objects_to_list.append(obj_properties)

    for obj in objects_with_descriptions:
        description = description + " " + obj["description"]

    if len(objects_to_list) > 0:
        description = description + " Lying on the ground you can see"
        if len(objects_to_list) > 1:
            for obj in objects_to_list[0:-1]:
                description = description + " " + obj["name"] + ","
            description = description[0:-1] + " and"    
        description = description + " " + objects_to_list[-1]["name"] + "."
        
    formatted_description=textwrap.fill(description)
    print(formatted_description)

def object_with_name(name):
    for obj_name, obj_properties in objects.items():
        if name in obj_properties["synonyms"] and obj_properties.get("hidden") != True:
            return (obj_name, obj_properties)
    return (None, None)
            
def take(obj_name):
    name, obj=object_with_name(obj_name)
    if obj==None:
        print("I don't understand '" + obj_name + "'.")
        return
    if obj in carried_objects:
        print("You are already holding " + obj["name"] + ".");
        return
    if obj.get("location") != location:
        print("You cannot see " + obj["name"] + ".")
        return
    if obj.get("can_take") == False:
        print("You can't take that!")
        return
    obj["location"] = None
    carried_objects.append(name)
    print("You take " + obj["name"] + ".");

def drop(obj_name):
    name, obj=object_with_name(obj_name)
    if obj==None:
        print("I don't understand '" + obj_name + "'.")
        return
    if not name in carried_objects:
        print("You are not holding " + obj["name"] + ".");
        return
    obj["location"] = location
    carried_objects.remove(name)
    print("You drop " + obj["name"] + ".");

def inventory():
    print("")
    if len(carried_objects) == 0:
        print("You are not carrying anything.")
    else:
        print("You have clutched in your sweaty hands:")
        for obj_name in carried_objects:
            print("    " + objects[obj_name]["name"])
        
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
    print("Instructions:")
    print("The aim of the game is to explore and escape from Stamford Green Primary School.")
    print("  1. Use 'north', 'east', 'south' or 'west' (or 'n', 'e', 's' or 'w') to move.")
    print("  2. Type 'look' to see what you can see.")
    print("  3. Use 'take <object>' and 'drop <object>' to take and drop objects.")
    print("  4. Use 'inventory' (or 'invent' or 'i') to see what you are carrying.")
    print("  5. Display this message again by typing 'help'.")

# The main part of the program starts here
print("Escape From Stamford Green!")
print("---------------------------")
print("Type 'help' for instructions.")

location="the_office" # Global variable containing the player's current location
carried_objects=[]
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
    elif command.startswith("take "):
        take(command[5:])
    elif command.startswith("drop "):
        drop(command[5:])
    elif command=="inventory" or command=="invent" or command=="i":
        inventory()
    elif command=="look":
        look()
    elif command=="help":
        help()
    else:
        print("I don't understand that! Try 'north', 'south', 'east' or 'west', or 'help'.")

    if location=="corridor" and move_to_location=="tunnel" and objects["dog_awake"].get("hidden") != True:
        print("The dog snarls and blocks your way.")
        move_to_location = None

    if location=="top_field" and move_to_location=="escape" and objects["gate_locked"].get("hidden") != True:
        print("The gate is closed and locked. The lock has a key hole.")
        move_to_location = None

    if move_to_location != None:
        location=move_to_location
        look()

    if objects["meat"].get("location") == "corridor":
        print("The dog eats the piece of meat and falls asleep.")
        objects["meat"]["location"] = None
        objects["dog_awake"]["hidden"] = True
        objects["dog_asleep"]["hidden"] = False

    if location=="top_field" and objects["gate_open"].get("hidden") == True and "key" in carried_objects:
        print("You unlock the gate with the key and it swings open.")
        objects["gate_locked"]["hidden"] = True
        objects["gate_open"]["hidden"] = False

print()
print("Congratulations, you have escaped from Stamford Green!")
