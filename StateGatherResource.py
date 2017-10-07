from PlayerState import *
from pathFinder import PathFinder

class GatherResource(PlayerState):
    """ State Implementation: has a resource target and go for it """

    def __init__(self, playerSession, resource):
        self.player = playerSession
        self.target = resource
        self.player.target(resource)

    def doAction(self):
        origin = player.Position;
        target = self.player.target
        moves = PathFinder(deserialized_map).getPath(origin, target)
        # If as reached the resource
        if len(moves) == 1:
            return create_collect_action(moves[0])
        else:
            return create_move_action(moves[0])

