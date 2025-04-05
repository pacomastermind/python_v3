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

# Obstacle deinition
OBSTACLE_SYMBOL = "###"
obstacle_definition = """\
                    
##############    ##
                  ##
   ##########     ##
                  ##
##########        ##
                  ##
       #############
       #############
       #############
       #############
       #############
                    
     ######  #######
     ######  #######"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# List SP and OBSTACLE positions
sp_map_positions = []
coordinate_x = 0
coordinate_y = 0
for row in obstacle_definition:
    for column in row:
        if column == " ":
            sp_map_positions.append([coordinate_x,coordinate_y])
        coordinate_x +=1
    coordinate_x = 0
    coordinate_y +=1


# Player
PL_SYMBOL = " @ "
POS_X = 0
POS_Y = 1
# Creating player
sp_position = sp_map_positions[randint(0,len(sp_map_positions))]
player_position = sp_position
sp_map_positions.remove(sp_position)

# Objects
NUM_MAP_OBJECTS = 10
OBJ_SYMBOL = " * "
map_objects = []

# Creating objects
for num in range(NUM_MAP_OBJECTS):
    sp_position = sp_map_positions[randint(0, len(sp_map_positions))]
    map_objects.append(sp_position)
    sp_map_positions.remove(sp_position)


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
            # Check player
            if coordinate_x == player_position[POS_X] and coordinate_y == player_position[POS_Y]:
                symbol_to_draw = PL_SYMBOL
                # Check if  object_in_cell
                if object_in_cell:
                    map_objects.remove(object_in_cell)
            # Check obstacle
            row_obstacle = obstacle_definition[coordinate_y]
            if row_obstacle[coordinate_x] == "#":
                symbol_to_draw = OBSTACLE_SYMBOL
            # Draw symbol
            print(symbol_to_draw, end="")
            # Reset symbol
            symbol_to_draw = SP_SYMBOL
        print(V_WALL_SYMBOL)
    # Bottom wall
    print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)

    # Test player position
    # print(player_position)
    # print(map_objects)

    # Direction control
    print("¿Donde te quieres mover? [W|A|S|D]")
    direction = readchar.readkey().upper()

    if direction == "W":  # UP
        player_position[POS_Y] -= 1
        # player_position[POS_Y] = player_position[POS_Y] % MAP_HEIGHT
        player_position[POS_Y] %= MAP_HEIGHT
        #Check obstacle
        row_obstacle = obstacle_definition[player_position[POS_Y]]
        if row_obstacle[player_position[POS_X]] == "#":
            player_position[POS_Y] += 1
            player_position[POS_Y] %= MAP_HEIGHT
    elif direction == "S":  # DOWN
        player_position[POS_Y] += 1
        player_position[POS_Y] %= MAP_HEIGHT
        #Check obstacle
        row_obstacle = obstacle_definition[player_position[POS_Y]]
        if row_obstacle[player_position[POS_X]] == "#":
            player_position[POS_Y] -= 1
            player_position[POS_Y] %= MAP_HEIGHT
    elif direction == "D":  # RIGHT
        player_position[POS_X] += 1
        player_position[POS_X] %= MAP_WIDTH
        #Check obstacle
        row_obstacle = obstacle_definition[player_position[POS_Y]]
        if row_obstacle[player_position[POS_X]] == "#":
            player_position[POS_X] -= 1
            player_position[POS_X] %= MAP_WIDTH
    elif direction == "A":  # LEFT
        player_position[POS_X] -= 1
        player_position[POS_X] %= MAP_WIDTH
        #Check obstacle
        row_obstacle = obstacle_definition[player_position[POS_Y]]
        if row_obstacle[player_position[POS_X]] == "#":
            player_position[POS_X] += 1
            player_position[POS_X] %= MAP_WIDTH
    elif direction == "Q":  # LEFT
        break
