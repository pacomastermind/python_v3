# Interactive game based on a two-dimensional map

# Map Dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15
V_WALL_SYMBOL = "|"  # Vertical Wall
H_WALL_SYMBOL = "-" * 3  # Horizontal Wall
SP_SYMBOL = " " * 3  # Space symbol
CORNER_SYMBOL = "+"

# Upper wall
print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)
# Map
for coordinate_y in range(MAP_HEIGHT):
    print(V_WALL_SYMBOL, end="")
    for coordinate_x in range(MAP_WIDTH):
        print(SP_SYMBOL, end="")
    print(V_WALL_SYMBOL)
# Bottom wall
print(CORNER_SYMBOL + H_WALL_SYMBOL * MAP_WIDTH + CORNER_SYMBOL)
