#!/usr/bin/python2.7

def print_tile(tile):
    """ Print one tile acccording to TileContent enum """
    content = tile.Content
    padding = ' '
    tileDisplayStr = ''

    # Create the string that will be displayed
    if(content == 0):
        tileDisplayStr = '.'
    elif(content == 1):
        tileDisplayStr = '|'
    elif(content == 2):
        tileDisplayStr = 'H'
    elif(content == 3):
        tileDisplayStr = 'X'
    elif(content == 4):
        tileDisplayStr = '*'
    elif(content == 5):
        tileDisplayStr = 'S'
    elif(content == 6):
        tileDisplayStr = 'P'
    else:
        tileDisplayStr = ' '
    print(padding + tileDisplayStr + padding),
    #print(padding + str(content) + padding), # To use in case of Enum is destroyed

def print_map(deserialized_map) :
    """ Print the whole map """
    print("\n\n ---------- MAP ----------\n\n")

    for y in range(len(deserialized_map)):
        for x in range(len(deserialized_map[0])):
            print_tile(deserialized_map[x][y]),
        print("\n")

    print("\n\n --------------------\n\n")

