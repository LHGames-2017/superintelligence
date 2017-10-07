import math

class PlayerSession:
    def __init__(self, player):
        self.playerData = player
        self.target = None

    def setTarget(self, position):
        self.target = position
