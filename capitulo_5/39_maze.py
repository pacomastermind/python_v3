# Interactive game based on a two-dimensional map
from os import system
import readchar
from random import randint

# Map Dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15
V_WALL_SYMBOL = "|"  # Vertical Wall
H_WALL_SYMBOL = "-" * 3  # Horizontal Wall
SP_SYMBOL = " " * 3  # Space symbol
CORNER_SYMBOL = "+"
symbol_to_draw = SP_SYMBOL

# Player
PL_SYMBOL = " @ "
POS_X = 0
POS_Y = 1
tail_length = 0
player_position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
tail = []

# Objects
NUM_MAP_OBJECTS = 10
OBJ_SYMBOL = " * "
map_objects = []

# Creating objects
while len(map_objects) < NUM_MAP_OBJECTS:
    new_object = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]

    # Check player position and in object list
    if new_object != player_position and new_object not in map_objects:
        map_objects.append(new_object)

# Game Start
while True:
    # Clear screen
    system("cls")
    # Upper wall
    print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)
    # Map
    for coordinate_y in range(MAP_HEIGHT):
        print(V_WALL_SYMBOL, end="")
        for coordinate_x in range(MAP_WIDTH):
            # Reset object in cell
            object_in_cell = None
            # Check objects
            for map_object in map_objects:
                if coordinate_x == map_object[POS_X] and coordinate_y == map_object[POS_Y]:
                    symbol_to_draw = OBJ_SYMBOL
                    # Object in cell
                    object_in_cell = map_object
            # Check tail
            for tail_piece in tail:
                if coordinate_x == tail_piece[POS_X] and coordinate_y == tail_piece[POS_Y]:
                    symbol_to_draw = PL_SYMBOL
            # Check player
            if coordinate_x == player_position[POS_X] and coordinate_y == player_position[POS_Y]:
                symbol_to_draw = PL_SYMBOL
                # Check if  object_in_cell
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
            # Draw symbol
            print(symbol_to_draw, end="")
            # Reset symbol
            symbol_to_draw = SP_SYMBOL
        print(V_WALL_SYMBOL)
    # Bottom wall
    print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)
    # Test tail prints
    print(f"La cola mide: {tail_length}")
    print(f"{tail}")

    # Direction control
    print("¿Donde te quieres mover? [W|A|S|D]")
    direction = readchar.readkey().upper()

    if direction == "W":  # UP
        tail.insert(0, player_position.copy())
        tail = tail[:tail_length]
        player_position[POS_Y] -= 1
        # player_position[POS_Y] = player_position[POS_Y] % MAP_HEIGHT
        player_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S":  # DOWN
        tail.insert(0, player_position.copy())
        tail = tail[:tail_length]
        player_position[POS_Y] += 1
        player_position[POS_Y] %= MAP_HEIGHT
    elif direction == "D":  # RIGHT
        tail.insert(0, player_position.copy())
        tail = tail[:tail_length]
        player_position[POS_X] += 1
        player_position[POS_X] %= MAP_WIDTH
    elif direction == "A":  # LEFT
        tail.insert(0, player_position.copy())
        tail = tail[:tail_length]
        player_position[POS_X] -= 1
        player_position[POS_X] %= MAP_WIDTH
    elif direction == "Q":  # LEFT
        break
