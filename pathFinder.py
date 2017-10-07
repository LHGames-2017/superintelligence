from queue import PriorityQueue
from structs import *

class PathFinder:
	
	class Node:

		def __init__(self, tile, goal, cost):
			self.heristic_cost = getHeuristicCost(goal)
			self.tile = tile

		def getHeuristicCost(self, goal):
			goalPoint = Point(goal.x, goal.y)
			self.heuristicCost = Point.Distance(goalPoint, Point(self.tile.x, self.tile.y))

		def __gt__(self, other):
			return self.heuristicCost < other.heuristicCost


	def __init__(self, map):
		self.map = map

	def getPath(self, goal,start):
		
		current = start
		
		frontier = PriorityQueue() 
		frontier.put(Node(x,goal) for x in getValidNeighbors(current))
		
		while len(frontier) > 0:
			current = frontier.pop()

	def getValidNeighbors(self, pos):
		midPoint = len(map)/2
		neighbors = [map[midPoint][midPoint+1], map[midPoint][midPoint-1], map[midPoint-1][midPoint], map[midPoint+1][midPoint]]
		for x in neighbors:
			if not isValid(x):
				del x
		return neighbors

	def isValid(self,tile):
		return tile.content not in [TileContent.Lava, TileContent.Wall, TileContent.Shop]
