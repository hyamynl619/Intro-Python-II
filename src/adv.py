from room import Room
from player import Player
from item import Item
import textwrap
import sys
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'stick': Item("stick", "This piece of wood seems sturdy enough to scare something away..."),
    'rock': Item("rock", "Hopefully you have good aim?"),
    'torch': Item("torch", "Ahh...fire. You can see!"),
    'knife': Item("pocket knife", "Finally, some sort of real weapon...I think"),
    'water': Item("water", "You must be thirsty"),
    'sword': Item("sword", "A sword comes with many enemies"),
    'gold': Item("gold", "You're rich!")

    
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Storing items in rooms for player
room['outside'].contents = [item['stick'], item['rock'], item['torch']]
room['foyer'].contents= [item['water']]
room['overlook'].contents = [item['knife']]
room['narrow'].contents = [item['sword']]
room['treasure'].contents = [item['gold']]



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


### Player Setup ###
new_player = input('What is your name?')
player = Player(new_player, room['outside'])

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f"{player.name}, Welcome to your first adventure!")
print(f"Shall we enter the cave?")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



def choose_item(player, item_name):
    try:
        if item[item_name] in player.current_room.contents:
            player.inventory.append(item[item_name])
            player.current_room.contents.remove(item[item_name])
            print(item[item_name].on_take())
        
        else:
            print(f"There's no items here")
    except:
        print(f"'{item_name}' is not a valid item")

def drop_item(player, item_name):
    try:
        if item[item_name] in player.inventory:
            player.current_room.contentsappend(item[item_name])
            player.inventory.remove(item[item_name])
            print(item[item_name].on_drop())
        
        else:
            print(f"This '{item_name}'' is not in your inventory")
    except:
        print(f"'{item_name}' is not a valid item")

### Title Screen ###
while True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"\n{player.name} is currently in the {player.current_room.name}")
    print(f"{player.current_room.description}\n")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    user_choice = input(f" - Command:")

    command = user_choice.split()

    if len(command) <= 1:
        if user_choice == "q":
            sys.exit()
        elif user_choice == "i":
            print(f"Inventory:")
            if len(player.inventory) == 0:
                print(f"There are no items")
            else:
                print(f"{player.name} has:\n{player.inventory}")
        elif user_choice == "l":
            print(f"\n{player.name} looks around {player.current_room.name}")
            if len(player.current_room.contents) == 0:
                print(f"This room is empty")
            else:
                print(f"{player.current_room.name} contains {player.current_room.contents}")
        elif user_choice == "a":
            print(f"\n{player.name} added {player.current_room.contents} to inventory")
            if len(player.current_room.contents) == 0:
                print(f"This room is empty")
        elif user_choice == 'd':
            print(f"\n{player.name} dropped {player.current_room.contents}")
        elif user_choice == 'p':
            print(f"\n{player.name} attacked!")
        
        

        #Movements
        elif user_choice == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
            else:
                print(f"\n - Can't go here")
        elif user_choice == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
            else:
                print(f"\n - Can't go here")
        elif user_choice == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
            else:
                print(f"\n - Can't go here")
        elif user_choice == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
            else:
                print(f"\n - Can't go here")

        elif user_choice == 'help':
            print('########################')
            print('### Let me help you! ###')
            print('#   Valid commands:    #')
            print('#    Directions        #')
            print('# -[n] = move north  - #')
            print('# -[e] = move east   - #')
            print('# -[s] = move south  - #')
            print('# -[w] = move west   - #')
            print('########################')
            print('#     Actions          #')
            print('# -[i] = inventory   - #')
            print('# -[g] = equip item  - #')
            print('# -[a] = add item    - #')
            print('# -[d] = drop item   - #')
            print('# -[l] = look around - #')
            print('# -[p] = attack      - #')
            print('########################')
            print('#     Main Menu        #')
            print('# -[q] = quit game   - #')
            print('# -[h] = help menu   - #')
        else:
            print(f"\n - {user_choice} can not be used.\n - Try help command")


        


        
        

        

