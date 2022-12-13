from pqueue import PriorityQueue
from graph import Node
from graph import adjacent
import math

def noHeuristic (current, dest):
  return 0

def manhattan (current, dest):
  return abs(dest.x - current.x) + abs(dest.y - current.y)

def euclidian (current, dest):
  return math.sqrt ((dest.x - current.x)**2 + (dest.y - current.y)**2) 

def Astar (graph, heuristic, source, dest):
  source.dist = 0
  source.cost = 0
  visted = []
  queue = PriorityQueue ()
  
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if not graph[y][x].isWall:
        queue.insert (graph[y][x])

  while not queue.empty ():
    current = queue.extractMin ()
    visted.append (current)
    if current == dest:
      break

    for node in adjacent (graph, current):
      if node.dist > current.dist + 1:
        node.dist = current.dist + 1
        node.cost = node.dist + heuristic (node, dest)
        node.parent = current
        queue.decreaseKey (node)
