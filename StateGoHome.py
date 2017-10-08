from PlayerState import *
from pathFinder import PathFinder

from StateLook4Resources import *

class StateGoHome(PlayerState):
    """ State Implementation: has a resource and go back home """

    def __init__(self, player):
        self.player = player
        self.player.setTarget(self.player.playerData.HouseLocation)

    def doAction(self):
        origin = self.player.playerData.Position
        target = self.player.target
        moves = PathFinder(self.player.mapView).getPath(origin, target)

        # If player just gave the resource home, look 4 resources again
        if(not self.player.hasResources()):
            self.player.state = StateLook4Resources(self.player)
            return self.player.state.doAction()
        return create_move_action(moves[0])

    def toString():
        return "StateGoHome"
