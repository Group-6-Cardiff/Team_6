#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
import random
import webbrowser
global plane_flag
global evidence_flag
plane_flag = False
evidence_flag = False

def list_of_items(items):
    string = ""
    for item in items:
        string = string + str(item["name"]) + ", "

    return (string[:-2])

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
    print("GO " + direction.upper() + " to " + leads_to + ". This will take " + str(
        int(current_room["travel"][direction] * 60)) + " minutes")

def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"])
    '''for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop " + item["name"])'''
    for item in inv_items:
        print("USE " + item["id"].upper() + " to use " + item["name"])
    for item in inv_items:
        print("INSPECT " + item["id"].upper() + " to inspect " + item["name"])
    print("MAP to view the map")

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    global current_room
    if is_valid_exit(current_room["exits"], direction) is True:
        if (is_room_open(current_room["exits"], direction)) is True:
            game_clock(current_room["travel"][direction])
            current_room = (move(current_room["exits"], direction))
        else:
            print("This room is locked find a key")
    else:
        print("You cannot go there")

def execute_inspect(item_id):
    for item in inventory:
        if item["id"] == item_id:
            print(item["description"])
            return
    print("You cannot inspect that that.")

def execute_take(item_id):
    for item in current_room["items"]:
        if item["id"] == item_id:
            if item_lock_check(item) is True:
                return
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
    # when called this function displays the world map for the user

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
        if item["id"] == item_id and item in current_room["useable"]:
            inventory.remove(item)  # this assumes items can only be used once....
            item_use(item)# add specific usage data here
            print(str(item["id"]) + " has been used")
            return

    # statement whether item cannot be used or if used up due to wrong place?
    print("You cannot use that here.")

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
    # executes use command:
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what")
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

    print("""

 .d8888b.                    d8b                         888    d8P          d8b 888 888 
d88P  Y88b                   Y8P                         888   d8P           Y8P 888 888 
Y88b.                                                    888  d8P                888 888 
 "Y888b.    8888b.  888  888 888 88888b.   .d88b.        888d88K     888d888 888 888 888 
    "Y88b.     "88b 888  888 888 888 "88b d88P"88b       8888888b    888P"   888 888 888 
      "888 .d888888 Y88  88P 888 888  888 888  888       888  Y88b   888     888 888 888 
Y88b  d88P 888  888  Y8bd8P  888 888  888 Y88b 888       888   Y88b  888     888 888 888 
 "Y8888P"  "Y888888   Y88P   888 888  888  "Y88888       888    Y88b 888     888 888 888 
                                               888                                       
                                          Y8b d88P                                       
                                           "Y88P"                                        
            """)
    'Colossal'
    setup()
    x = True
    # Main game loop
    while x is True:
        '''webbrowser.open("D:\Game06\Music.mp3")  '''
        '''A soundtrack might need more work.....definatly needs more work'''
        # Display game status (room description, inventory etc.)
        print("")
        mins = ((count_down * 60) % 60)
        print(str(int(count_down)) + " hours " + str(int(mins)) + " minutes remaining")
        print_room(current_room)
        print_inventory_items(inventory)
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)
        print("")
        # Execute the player's command
        execute_command(command)

        x = win_check()

def game_clock(traveltime):
    global count_down
    count_down = count_down - traveltime

def is_room_open(exits, direction):
    return rooms[exits[direction]]["open"]

def win_check():
    global plane_flag
    global evidence_flag
    '''Contains the victory conditions and also the losing conditions'''
    if count_down <= 0:
        print("you are out of time kirll and you are going to spend the rest of your days in a cell")
        print("game over")
        return False

    if plane_flag is True:
        print("Well you done it you've escaped leaving kirll behind to his fate")
        return False

    if evidence_flag is True:
        print("You've proven Kirll innoccent well done")
        return False
    
    return True

def setup():
    '''setups up the random items and makes other useable'''
    item_random_setup()
    make_useable()

def make_useable():
    '''this function makes items useable'''
    item_list = [item_evidence,item_plane_ticket]

    for room in rooms:
        '''This makes wallet and bike useable everywhere as I was to lazy to enter them manually into map.py'''
        rooms[room]["useable"].append(item_bike)
        rooms[room]["useable"].append(item_wallet)
        rooms[room]["useable"].append(item_plane_ticket)
        for item in item_list:
            if item in rooms[room]["items"]:
                '''This makes the bribe useable in the rooms with the win needing items '''
                rooms[room]["useable"].append(item_gold_bar)

                '''This makes the receipt a clue to where the evidence is being held'''
                if item["id"] == "evidence":
                    item_receipt["description"] = "A receipt from " + rooms[room]["name"]

def item_random_setup():

    '''first run through these items are allowed to be randomly placed anywhere'''
    item_list = [item_gold_bar]
    basic_rooms = list(rooms.keys())
    item_randomiser(item_list,basic_rooms)

    '''these new items cannot be place in bedroom or the student union'''
    item_list = [item_room_keys, item_id]
    safe_rooms = list(rooms.keys())
    safe_rooms.remove("Bedroom")
    safe_rooms.remove("Student Union")
    item_randomiser(item_list,safe_rooms)

    '''This item randomiser splits the victory items between the 3 win locations'''
    item_list = [item_evidence,item_plane_ticket]
    victory_rooms = ["Pub","Bar","Club"]

    item_randomiser(item_list,victory_rooms)

def item_randomiser(item_list,rooms_in_use):
    '''Function to place items in rooms'''
    for item in item_list:
        x = random.randint(0, (len(rooms_in_use) - 1))
        room_to_add_to = rooms_in_use[x]
        rooms[room_to_add_to]["items"].append(item)
        rooms_in_use.remove(room_to_add_to)

def item_use(item):
    '''Function containing all the useable items affects when used'''
    if item["id"] == "wallet":
        inventory.append(item_receipt)
        inventory.append(item_money)
        print("Gained money and a receipt")

    if item["id"] == "bikekey":
        item_bike["lock"] = False
        print("bike unlocked")

    if item["id"] == "roomkeys":
        rooms["Bedroom"]["open"] = True
        print("Your Bedroom is now open")

    if item["id"] == "bike":
        for room in rooms:
            for direction in rooms[room]["travel"]:
                rooms[room]["travel"][direction] = rooms[room]["travel"][direction]/2
        print("You'll now travel twice as fast")

    if item["id"] == "id":
        rooms["Staff room"]["open"]=True
        print("You jammed open the doors")

    if item["id"] == "safe":
        pin=int(input(""))
        if pin==("1234"):
            current_room["items"].append(item_coins)
        else:
            print("Invalid pin")

    if item["id"] == "phone_box":
       if input("For emergeny only")=="999":
           rooms["Secret room"]["open"]=True

    if item["id"] == "planeticket":
        global plane_flag
        plane_flag = True

    if item["id"] == "evidence":
        global evidence_flag
        evidence_flag = True

    if item["id"] == "goldbar":
        for room_item in current_room["items"]:
            if room_item == item_plane_ticket:
                '''Unlocks the plane ticket'''
                item_plane_ticket["lock"] = False
                print("The Bartender's eyes light up ,'it's a done deal' he says taking the goldbar out your hands "
                      "and disappering into the back room leaving the ticket on the side ")
            if room_item == item_evidence:
                '''Unlocks the Evidence'''
                item_evidence["lock"] = False
                print("The Bartender looks hungrily at it, looking left and right quickly he takes it from you and "
                      "slowly goes into the staff leaving the evidence behind him")



def item_lock_check(item):
    '''checks only the items that actually have the lock dict'''
    if item["id"] == "bike":
        if item["lock"] is True:
            print("Your bike is locked up find your key")
            return True
    elif item["id"] == "evidence":
        if item["lock"] is True:
            print("The bartender stops you taking it claiming something about store policy. Maybe a hefty bribe would work on him?")
            return True
    elif item["id"] == "planeticket":
        if item["lock"] is True:
            print("The bartender stops you taking it saying he found it first but he's willing to sell it for the right price.")
            return True

    return False
''' 
Deadly Roulette Kevin MacLeod (incompetech.com) 
Licensed under Creative Commons: By Attribution 3.0
http://creativecommons.org/licenses/by/3.0/
'''

if __name__ == "__main__":
    main()
