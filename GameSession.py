from PlayerSession import *

class GameSession:

    def __init__(self):
        self.turnCounter        = 0
        self.playerSession      = PlayerSession(None)
        self.gameViewMap        = None

    def updateTurnData(self, player, gamemap):
        """ Called once a turn """
        self.playerSession.playerData = player
        self.gameViewMap = gamemap
        self.turnCounter += 1
