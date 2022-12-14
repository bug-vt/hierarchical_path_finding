from pqueue import PriorityQueue
from graph import Node
from graph import adjacent
from graph import path 
from graph import haveVisited
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
  start = Node (source[0], source[1])
  start.dist = 0
  end = Node (dest[0], dest[1])
  visited = []
  queue = PriorityQueue ()
  
  queue.insert (start)
  
  while not queue.empty ():
    search_count += 1
    current = queue.extractMin ()
    visited.append (current)
    if search_count > search_lim:
      break
    if current.equal (end):
      found = True
      break

    for neighbor in adjacent (graph, current):
      if haveVisited (visited, neighbor):
        continue
      
      if neighbor.dist > current.dist + 1:
        neighbor.dist = current.dist + 1
        neighbor.cost = neighbor.dist + heuristic (neighbor, end)
        queue.decreaseKey (neighbor)

  return path (current), search_count, found

        
