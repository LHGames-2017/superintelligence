import sys

from PlayerState import *
from structs import *
from StateGatherResource import *
from StateGoHome import *

class StateLook4Resources(PlayerState):
    """ State Implementation
        look for any resource but none at is side so far """

    def __init__(self, playerSession):
        self.player = playerSession

    def doAction(self):
        # If is already full, go back home
        if(self.player.isFull()):
            self.player.state = StateGoHome(self.player)
            return self.player.state.doAction()


        mapView         = self.player.mapView
        allResources    = self.getAllResources()

        if(allResources == []):
            #If no resource is find, keep going to our tmp target
            TargetPos = self.getNewTarget()
            return create_move_action(targetPos)
        else:
            resource = self.getClosestResource(allResources)
            self.player.state = StateGatherResource(self.player, resource)
            return self.player.state.doAction()

    def getAllResources(self):
        """ Returns all resources in range """
        mapView = self.player.mapView
        listResources = []
        # Create a list of resources
        for y in range(len(mapView)):
            for x in range(len(mapView[0])):
                if mapView[y][x].Content == 4: #Resource
                    tile = mapView[y][x]
                    listResources.append(Point(tile.X, tile.Y))
        return listResources

    def getClosestResource(self, listResources):
        playerPosition = self.player.playerData.Position
        minDistance = sys.maxint
        resource = listResources[0]
        for x in listResources:
            distance = Point().Distance(x, playerPosition)
            if distance < minDistance:
                minDistance = distance
                resource = x
        return resource

    def getRandomTarget():
        #TODO
        return Point(0,5)

