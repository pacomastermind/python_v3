# Interactive game based on a two-dimensional map
from os import system
import readchar

# Map Dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15
V_WALL_SYMBOL = "|"  # Vertical Wall
H_WALL_SYMBOL = "-" * 3  # Horizontal Wall
SP_SYMBOL = " " * 3  # Space symbol
CORNER_SYMBOL = "+"

# Player
PL_SYMBOL = " @ "
POS_X = 0
POS_Y = 1
player_position = [3, 1]

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
            if coordinate_x == player_position[POS_X] and coordinate_y == player_position[POS_Y]:
                print(PL_SYMBOL, end="")
            else:
                print(SP_SYMBOL, end="")
        print(V_WALL_SYMBOL)
    # Bottom wall
    print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)

    # Direction control
    print("¿Donde te quieres mover? [W|A|S|D]")
    direction = readchar.readkey().upper()

    if direction == "W":  # UP
        player_position[POS_Y] -= 1
    elif direction == "S":  # DOWN
        player_position[POS_Y] += 1
    elif direction == "D":  # RIGHT
        player_position[POS_X] += 1
    elif direction == "A":  # LEFT
        player_position[POS_X] -= 1
    elif direction == "Q":  # LEFT
        break
