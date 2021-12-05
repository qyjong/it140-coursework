
"""
Jon Hoover
Introduction to Scripting
IT-140-X2971
21EW2
December 4, 2021
"""


def change_room(working_room):
    # Initialize variables
    # Calls the global variable end_game to modify it.
    global end_game
    this_room = ""
    room_options = {}
    valid_choice = False

    # Unpack the various rooms from dictionary value for current room
    for key, value in working_room.items():
        this_room = key
        room_options = working_room[key]
    # Tell the player what room they are in.
    print("You are currently in", this_room)

    # Tell the player what rooms they can travel to.
    for key, value in room_options.items():
        print("To the", key, "is the room:", room_options[key])

    # As long as player enters a valid direction or the word 'quit'
    # They will either travel to the selected room or end the game.
    # Otherwise, they will have to enter a valid choice.
    while not valid_choice:
        print("\nPlease type the direction you wish to travel (North, South, East, West).")
        player_choice = (input("To quit, type 'quit': ")).lower()
        if player_choice == "quit":
            end_game = True
            return working_room
        else:
            for key, value in room_options.items():
                if player_choice == key.lower():
                    next_room = {value: dragon_rooms[value]}
                    # At this point, as long as the player entered a valid direction,
                    # the next room will be returned to original function call.
                    return next_room
                else:
                    pass
            # If, after comparing player's input to all room options,
            # the input does not match any of the room options, we give the player
            # an error and remind them where they are and which options they need
            # to choose from.
            print("\nInput is not valid! You are currently in", this_room)

            for key, value in room_options.items():
                print("To the", key, "is the room:", room_options[key])


# Initialize variables
# Sets end_game to False to force while loop below to run at least once.
end_game = False
# Player will start in the Bedroom.
current_room = {'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'}}
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
dragon_rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# While loop to call the function to change rooms
while not end_game:
    current_room = change_room(current_room)

# If the player types 'quit', then their game will end below.
if end_game:
    quit()
