import math
from PlayerState import *
from StateLook4Resources import *

class PlayerSession:
    def __init__(self):
        self.playerData = None
        self.mapView    = None
        self.target     = None
        self.state      = StateLook4Resources(self)

    def updateServerData(self, player, mapView):
        self.playerData = player
        self.mapView    = mapView

    def setTarget(self, position):
        self.target = position

    def isFull(self):
        carried = self.playerData.CarriedRessources
        capacity = self.playerData.CarryingCapacity
        return carried >= capacity

    def hasResources(self):
        carried = self.playerData.CarriedRessources
        capacity = self.playerData.CarryingCapacity
        return carried > 0

    def isAtHome(self):
        coco = self.playerData.Position
        home = self.playerData.HouseLocation
        return coco.X == home.X and coco.Y == home.Y

