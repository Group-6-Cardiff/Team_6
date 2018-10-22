#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
import random

def list_of_items(items):

    string = ""
    for item in items:
        string = string + str(item["name"]) + ", "
        
    return(string[:-2])


def print_room_items(room):

    items = list_of_items(room["items"])
    if len(items) == 0:
        pass
    else: 
        print("There is " + items + " here.")
        print("")



def print_inventory_items(items):

    items = list_of_items(inventory)
    print("You have " + items + ".")
    print("")


def print_room(room):

    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ". This will take " + str(int(current_room["travel"][direction] * 60)) + " minutes")


def print_menu(exits, room_items, inv_items):

    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"])
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"])
    print("MAP to view the map")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

    return chosen_exit in exits

def execute_go(direction):

    global current_room
    if is_valid_exit(current_room["exits"],direction) is True:
       if (is_room_open(current_room["exits"],direction)) is True:
        game_clock(current_room["travel"][direction])
        current_room =(move(current_room["exits"],direction))
       else:
           print("This room is locked find a key")
    else:
        print("You cannot go there")
        
        
def execute_take(item_id):

    for item in current_room["items"]:
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            return
    print("You cannot take that.")

def execute_drop(item_id):

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("You cannot drop that.")

def execute_map():
    #when called this function displays the world map for the user

    print("""
        N
      W + E
        S

                                                        ---------                               
                                         ---------------|Student|--------------|                                
                                         |              |Union  |              |                      
                                         |              ---------              |                             
                                    ------------            |                  |    
                                    | Police   |        -------------      ---------
                   -----------------| Station  |--------|Accomadtion|------| Pub   |
                   |                |          |        -------------      ---------                                                                                                                                 
                   |                ------------              |                |                                                                                                                                     
                   |                     |                    |                | 
                   |                     |                    |                | 
             ------------                |               ----------        -----------
             | Castle   |----------------+---------------| Bar    |--------| Comp Sci|                    
             |          |                |               ----------        -----------                     
             ------------                |                   | 
                   |                  -------                |  
                   |------------------|Club |----------------|
                                      ------- 
        """)


def execute_use(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item) #this assumes items can only be used once....
            #add specific usage data here
            print (str(item) + " has been used")
            return
    print("You cannot use that.")
        
def execute_command(command):


    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "map":
            execute_map()
            
    #executes use command:
    elif command[0] == "use":
        execute_use(command[1])
            
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    setup()

    # Main game loop
    while True:  ################## Needs changing when game victory conditions made######
        # Display game status (room description, inventory etc.)
        print("")
        mins = ((count_down * 60)%60)
        print(str(int(count_down)) + " hours " + str(int(mins)) + " minutes remaining" )
        print_room(current_room)
        print_inventory_items(inventory)
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        win_check()

def game_clock(traveltime):
    
    global count_down
    count_down = count_down - traveltime
    
def is_room_open(exits,direction):

    return rooms[exits[direction]]["open"]

def win_check():
    if count_down <= 0:
        print("out of time")

def setup():

    item_randomiser()

def item_randomiser():
    '''first run through these items are allowed to be randomly placed anywhere'''
    item_list =   (item_handbook, item_laptop, item_money, item_pen)
    for item in item_list:
        x = random.randint(0,len(rooms))
        room_to_add_to =(list(rooms.keys())[x])
        rooms[room_to_add_to]["items"].append(item)

    '''these new items cannot be place in bedroom or the student union'''
    item_list = (item_id,item_biscuits)
    safe_rooms = (list(rooms.keys()))
    safe_rooms.remove("Bedroom")
    safe_rooms.remove("Student Union")
    print(safe_rooms)
    for item in item_list:
        x = random.randint(0,len(rooms))#
        room_to_add_to = safe_rooms[x]
        rooms[room_to_add_to]["items"].append(item)


if __name__ == "__main__":
    main()

