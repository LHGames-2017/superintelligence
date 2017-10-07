from queue import PriorityQueue

class PathFinder:
	
	def __init__(self, map):
		self.map = map

	def getPath(self, goal,start):
		
		current = start
		
		frontier = PriorityQueue() 
		frontier.put((x.node, x.cost) for x in getValidNeighbors(current))
		
		while len(frontier) > 0:
			current = frontier.pop()

	def getValidNeighbors(self, pos):
		for i in range(-1,2):
			for j in range(-1,2):
