#!/usr/bin/python2.7

def print_tile(tile, player):
    """ Print one tile acccording to TileContent enum """
    content = tile.Content
    padding = ' '
    tileDisplayStr = ''

    # IF the player itself of his house, special display
    if(tile.X == player.Position.X and tile.Y == player.Position.Y):
        tileDisplayStr = 'P'
    elif(tile.X == player.HouseLocation.X 
            and tile.Y == player.HouseLocation.Y):
        tileDisplayStr = 'H'
    # Create the string that will be displayed
    elif(content == 0):
        tileDisplayStr = '.'
    elif(content == 1):
        tileDisplayStr = '|'
    elif(content == 2):
        tileDisplayStr = 'h'
    elif(content == 3):
        tileDisplayStr = 'X'
    elif(content == 4):
        tileDisplayStr = '*'
    elif(content == 5):
        tileDisplayStr = 'S'
    elif(content == 6):
        tileDisplayStr = 'E'
    else:
        tileDisplayStr = ' '
    print(padding + tileDisplayStr + padding),
    #print(padding + str(content) + padding), # To use in case of Enum is destroyed

def print_game(deserialized_map, player) :
    """ Print the whole map """
    print("\n\n ----------------------------------- MAP -----------------------------------\n\n")

    for y in range(len(deserialized_map)):
        for x in range(len(deserialized_map[0])):
            print_tile(deserialized_map[x][y], player),
        print("\n")

    print("--------------------------------------------------------------------------------")
    print("Player health: " + str(player.Health))
    print("--------------------------------------------------------------------------------\n\n")

