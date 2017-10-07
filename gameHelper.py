#!/usr/bin/python2.7

def print_tile(tile, player, gameSession):
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

    # Special display for targeted position
    if(gameSession.playerSession.target != None
            and tile.X == gameSession.playerSession.target.X
            and tile.Y == gameSession.playerSession.target.Y):
        print("(" + tileDisplayStr + ")"),
    else:
        print(padding + tileDisplayStr + padding),
    #print(padding + str(content) + padding), # To use in case of Enum is destroyed

def print_game(gameSession) :
    """ Print the whole map """
    gameViewMap = gameSession.gameViewMap
    player = gameSession.playerSession.playerData
    print("\n\n ----------------------------------- MAP -----------------------------------\n\n")

    for y in range(len(gameViewMap)):
        for x in range(len(gameViewMap[0])):
            print_tile(gameViewMap[x][y], player, gameSession),
        print("\n")

    print("--------------------------------------------------------------------------------")
    print("Player health: " + str(player.Health))
    print("")
    print("Turn counter: " + str(gameSession.turnCounter))
    print("--------------------------------------------------------------------------------\n\n")

