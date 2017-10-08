from PlayerState import *
from pathFinder import PathFinder
from StateGoHome import *

class StateGatherResource(PlayerState):
    """ State Implementation: has a resource target and go for it """

    def __init__(self, playerSession, resource):
        self.player = playerSession
        self.target = resource
        self.player.setTarget(resource)

    def doAction(self):
        # TODO Add check if resource has gone
        origin = self.player.playerData.Position;
        target = self.player.target
        moves = PathFinder(self.player.mapView).getPath(origin, target)
        if len(moves) == 1:
            # If as reached the resource
            return create_collect_action(moves[0])
        else:
            # Go back home buddy
            self.player.state = StateGoHome(self.player)
            return self.player.state.doAction()

    def toString():
        return "StateGatherResource"
