from pqueue import PriorityQueue
from graph import Node
from graph import adjacent
from graph import shortestPath 
import math

def noHeuristic (current, dest):
  return 0

def manhattan (current, dest):
  return abs(dest.x - current.x) + abs(dest.y - current.y)

def euclidian (current, dest):
  return math.sqrt ((dest.x - current.x)**2 + (dest.y - current.y)**2) 

def Astar (graph, heuristic, source, dest, search_lim=100000):
  found = False
  search_count = 0
  source.dist = 0
  source.cost = 0
  visited = []
  queue = PriorityQueue ()
  
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if not graph[y][x].isWall:
        queue.insert (graph[y][x])

  while not queue.empty ():
    search_count += 1
    current = queue.extractMin ()
    visited.append (current)
    if search_count > search_lim:
      break
    if current == dest:
      found = True
      break

    for node in adjacent (graph, current):
      if node.dist > current.dist + 1:
        node.dist = current.dist + 1
        node.cost = node.dist + heuristic (node, dest)
        node.parent = current
        queue.decreaseKey (node)

  return found, shortestPath (graph, dest.x, dest.y)
