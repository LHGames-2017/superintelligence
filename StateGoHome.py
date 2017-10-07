from PlayerState import *
from pathFinder import PathFinder

class BringResourceBack(PlayerState):
    """ State Implementation: has a resource and go back home """

    def __init__(self):
        self.player = playerSession
        selt.player.target(self.player.playerData.HouseLocaltion)

    def doAction(self):
        origin = self.playerSession.player.Position
        target = self.player.target
        moves = PathFinder(deserialized_map).getPath(origin, target)

        # If player just gave the resource home, look 4 resources again
        if(not self.player.hasResources()):
            self.player.state = StateLook4Resources(self.player)
            return self.player.state.doAction()
        return create_move_action(moves[0])
