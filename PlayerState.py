from abc import ABCMeta, abstractmethod


def scanNeighbourhood(deserialized_map, player):
    ressourcesTiles = []
    for y in range(len(deserialized_map)):
        for x in range(len(deserialized_map[0])):
            if deserialized_map[y][x].Content == 4:
                tile = deserialized_map[y][x]
                ressourcesTiles.append(Point(tile.X, tile.Y))

    minDistance = sys.maxint
    target = player.Position + Point(0,5)
    for x in ressourcesTiles:
        distance = Point().Distance(x, player.Position)
        if distance < minDistance:
            minDistance = distance
            target = x
    return target

class PlayerState:
    """ Abstract class for player states """
    __metaclass__ = ABCMeta
    
    def __init__(self, playerSession):
        self.player = playerSession

    def actionOneTurn(self):
        raise NotImplementedError()


class Look4Resources(PlayerState):
    """ State Implementation
        look for any resource but none at is side so far """
    def actionOneTurn(self):
        mapView     = self.player.mapView
        newTarget   = scanNeighbourhood(mapView, self.player.playerData)
        player.setTarget(newTarget)
        moves = PathFinder(mapView).getPath(self.player.Position, newTarget)

        if len(moves) == 1:
            actionToDo = create_collect_action(moves[0])
        else:
            actionToDo = create_move_action(moves[0])

    def look4TheClosestResource(self):
        mapView = self.player.mapView
        ressourcesTiles = []
        for y in range(len(mapView)):
            for x in range(len(mapview[0])):
                if deserialized_map[y][x].Content == 4:
                    tile = deserialized_map[y][x]
                    ressourcesTiles.append(Point(tile.X, tile.Y))

        minDistance = sys.maxint
        target = player.Position + Point(0,5)
        for x in ressourcesTiles:
            distance = Point().Distance(x, player.Position)
            if distance < minDistance:
                minDistance = distance
                target = x
        return target


class GatherResource(PlayerState):
    """ State Implementation: has a resource target and go for it """
    def actionOneTurn(self):
        print("TODO")


class BringResourceBack(PlayerState):
    """ State Implementation: has a resource and go back home """
    def actionOneTurn(self):
        print("TODO")

