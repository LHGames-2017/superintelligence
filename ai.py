from flask import Flask, request
from structs import *
from pathFinder import PathFinder
import json
import numpy

from gameHelper import *
from PlayerSession import *
from GameSession import *

app = Flask(__name__)
gameSession = GameSession()
gameSession.playerSession = PlayerSession(None)

def create_action(action_type, target):
    actionContent = ActionContent(action_type, target.__dict__)
    return json.dumps(actionContent.__dict__)

def create_move_action(target):
    return create_action("MoveAction", target)

def create_attack_action(target):
    return create_action("AttackAction", target)

def create_collect_action(target):
    return create_action("CollectAction", target)

def create_steal_action(target):
    return create_action("StealAction", target)

def create_heal_action():
    return create_action("HealAction", "")

def create_purchase_action(item):
    return create_action("PurchaseAction", item)

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

    # Print
    print_game(deserialized_map, player)

    otherPlayers = []

    for player_dict in map_json["OtherPlayers"]:
        for player_name in player_dict.keys():
            player_info = player_dict[player_name]
            p_pos = player_info["Position"]
            player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

            otherPlayers.append({player_name: player_info })


    # return decision
    target = scanNeighbourhood(deserialized_map, player)
    pos = PathFinder(deserialized_map).getPath(player.Position, target)[0]

    gameSession.frameCounter += 1
    print(gameSession.frameCounter)
    return create_move_action(Point(0,1))

def scanNeighbourhood(deserialized_map, player):
    for y in range(len(deserialized_map)):
        for x in range(len(deserialized_map[0])):
            if deserialized_map[y][x].Content == 4:
                tile = deserialized_map[y][x]
                return Point(tile.X, tile.Y)
                #return player.Position + Point(0,1)
    return Point(25, 25)

def carryHome(player):

    if player.CarriedRessources == player.CarryingCapacity:
        return create_move_action(player.HouseLocation)  # TODO use playerSession to pass the path


@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
