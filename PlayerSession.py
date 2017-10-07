import math

class PlayerSession:
    def __init__(self, player):
        self.playerData = player
        self.target = None

    def setTarget(self, position):
        self.target = position

    def isFull(self):
        carried = self.playerData.CarriedRessources
        capacity = self.playerData.CarryingCapacity
        return carried >= capacity
