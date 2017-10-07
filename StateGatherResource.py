from PlayerState import *

class GatherResource(PlayerState):
    """ State Implementation: has a resource target and go for it """

    def __init__(self, playerSession, resource):
        self.player = playerSession
        self.target = resource
        self.player.target(resource)

    def doAction(self):
        print("TODO")

