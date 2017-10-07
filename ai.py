from flask import Flask, request
from structs import *
from pathFinder import PathFinder
import json
import numpy
import sys

from gameHelper import *

from GameSession import *

app = Flask(__name__)
gameSession = GameSession()

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = [[Tile() for x in range(20)] for y in range(20)]
    for i in range(len(rows) - 1):
        column = rows[i + 1].split('{')

        for j in range(len(column) - 1):
            infos = column[j + 1].split(',')
            end_index = infos[2].find('}')
            content = int(infos[0])
            x = int(infos[1])
            y = int(infos[2][:end_index])
            deserialized_map[i][j] = Tile(content, x, y)

    return deserialized_map

def bot():
    """
    Main de votre bot.
    """
    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map)
    p = map_json["Player"]
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    player = Player(p["Health"],
                    p["MaxHealth"],
                    Point(x,y),
                    Point(house["X"], house["Y"]),
                    p["Score"],
                    p["CarriedResources"],
                    p["CarryingCapacity"])

    # Map
    serialized_map = map_json["CustomSerializedMap"]
    deserialized_map = deserialize_map(serialized_map)

    otherPlayers = []

    for players in map_json["OtherPlayers"]:
            player_info = players["Value"]
            p_pos = player_info["Position"]
            player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append(player_info)

    # Update Game session
    gameSession.updateTurnData(player, deserialized_map)

    # Return decision
    coco = gameSession.playerSession

    #TODO To change by states
    #actionToDo = coco.state.actionOneTurn()
    #print_game(gameSession)
    #return actionToDo

    actionToDo = create_move_action(coco.playerData.Position)


    if(coco.isFull()):
        # If coco is full of resources, go back home
        coco.setTarget(coco.playerData.HouseLocation)
        moves = PathFinder(deserialized_map).getPath(player.Position, coco.target)
        actionToDo = create_move_action(moves[0])

    elif(coco.isAtHome() and coco.hasResources()):
        # Is giving back resource to home
        actionToDo = create_move_action(coco.playerData.HouseLocation)

    else:
        coco.setTarget(scanNeighbourhood(deserialized_map, player))
        moves = PathFinder(deserialized_map).getPath(player.Position, coco.target)

        if len(moves) == 1:
            actionToDo = create_collect_action(moves[0])
        else:
            actionToDo = create_move_action(moves[0])

    # Print all
    print_game(gameSession)
    return actionToDo

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
