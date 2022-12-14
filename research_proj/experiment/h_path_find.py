from pqueue import PriorityQueue
from astar import noHeuristic
from astar import manhattan
from astar import euclidian
from astar import Astar
from graph import Node
from graph import path 
from graph import haveVisited
from graph import printGraph


def adjacentRegion (graph, node, size, local_lim, heuristic):
  local_visit_count = 0
  neighbors = []
  x = node.x 
  y = node.y

  offsets = [(-size,0), (0, size), (size, 0), (0, -size)]
  for off_y, off_x in offsets:

    if x + off_x < 0 or x + off_x >= 42 or \
       y + off_y < 0 or y + off_y >= 42:

      continue

    path, visit_count, found = Astar (graph, heuristic, (x,y), (x+off_x, y+off_y), search_lim=local_lim)
    local_visit_count += visit_count 

    if found:
      #printGraph (graph, path)
      neighbors.append ((Node (x + off_x, y + off_y, node), len (path)))

  return neighbors, local_visit_count


def hPathFind (graph, heuristic, source, dest, local_lim):
  region_size = 10
  total_visit_count = 0
  start = Node (source[0], source[1])
  start.dist = 0
  end = Node (dest[0], dest[1])
  visited = []
  queue = PriorityQueue ()

  queue.insert (start)

  while not queue.empty ():
    current = queue.extractMin ()
    visited.append (current)
    if current.equal (end):
      break
    
    neighbors, visit_count = adjacentRegion (graph, current, region_size, local_lim*2, heuristic)
    total_visit_count += visit_count
    for neighbor, weight in neighbors:
      if haveVisited (visited, neighbor):
        continue

      if neighbor.dist > current.dist + weight:
        neighbor.dist = current.dist + weight
        neighbor.cost = neighbor.dist + heuristic (neighbor, end)
        queue.decreaseKey (neighbor)

  return path (current), total_visit_count
