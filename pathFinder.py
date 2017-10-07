from Queue import PriorityQueue
from structs import *

class Node:

    def __init__(self, tile, goal, sol):
        self.tile = tile
        self.heristic_cost = self.getHeuristicCost(goal)
        self.solution = Solution(sol)
        self.solution.addNode(self)

    def getHeuristicCost(self, goal):
        goalPoint = Point(goal.X, goal.Y)
        self.heuristicCost = Point().Distance(goalPoint, Point(self.tile.X, self.tile.Y))

    def __lt__(self, other):
        return self.heuristicCost + self.solution.cost < other.heuristicCost + other.solution.cost

class Solution:

    def __init__(self, s=None):
        self.cost = 0
        self.visited = []

        if s is not None: 
            self.cost = s.cost
            self.visited = list(s.visited)


    def addNode(self, node):
        self.visited.append(Point(node.tile.X, node.tile.Y))
        self.cost += 1


    def printSolution(self):
        for node in self.visited:
            print node
        print "COST : ",
        print self.cost


class PathFinder:

    def __init__(self, map):
        self.map = map


    def isValid(self,tile):
        return tile.Content not in [TileContent.Lava, TileContent.Wall, TileContent.Shop]

    def getValidNeighbors(self, pos):

        relativePosition = Point(pos.X, pos.Y) - Point(self.map[0][0].X, self.map[0][0].Y)


        neighbors = []

        if relativePosition.X+1 < len(self.map): 
            neighbors.append(self.map[relativePosition.X + 1][relativePosition.Y])
        if relativePosition.X-1 >= 0: 
            neighbors.append(self.map[relativePosition.X - 1][relativePosition.Y])
        if relativePosition.Y+1 < len(self.map[0]):
            neighbors.append(self.map[relativePosition.X][relativePosition.Y + 1])
        if relativePosition.Y-1 >= 0:  
            neighbors.append(self.map[relativePosition.X][relativePosition.Y - 1])

        validNeighbors = []
        for i in range(len(neighbors)):
            if self.isValid(neighbors[i]):
                validNeighbors.append(neighbors[i])
        return validNeighbors
    

    def getPath(self, start, goal):
        
        # minPoint = Point(self.map[0][0].X, self.map[0][0].Y)
        # maxPoint = Point(self.map[len(self.map) - 1][len(self.map[0]) - 1].X, self.map[len(self.map) - 1][len(self.map[0]) - 1].Y)
        # goal = Point(min(max(minPoint.X,goal.X), maxPoint.X), min(max(minPoint.Y, goal.Y),maxPoint.Y))

        current = start
        initialSolution = Solution()
        if current.X == goal.X and current.Y == goal.Y:
            return []

        frontier = PriorityQueue() 

        for x in self.getValidNeighbors(current):
            frontier.put(Node(x, goal, initialSolution))
        
        while not frontier.empty():
            print "Start {}".format(start)
            print "Goal {}".format(goal)
            currentNode = frontier.get()
            #print Point(currentNode.tile.X, currentNode.tile.Y)
            currentNode.solution.printSolution()
            if currentNode.tile.X == goal.X and currentNode.tile.Y == goal.Y:
                return currentNode.solution.visited

            for x in self.getValidNeighbors(currentNode.tile):
                frontier.put(Node(x, goal, currentNode.solution))

        return []


    

