from pqueue import PriorityQueue
from astar import noHeuristic
from astar import manhattan
from astar import euclidian
from astar import Astar
from graph import Node
from graph import path 
from graph import haveVisited
from graph import printGraph
from graph import WALL


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

    if graph[y + off_y][x + off_x] == WALL:
      continue

    path, visit_count, found = Astar (graph, heuristic, (x,y), (x+off_x, y+off_y), search_lim=local_lim)
    local_visit_count += visit_count 

    if found:
      path[len (path) - 1].parent = node
      neighbors.append ((Node (x + off_x, y + off_y, path[0].parent), len (path)))

  return neighbors, local_visit_count


def regionalAstar (graph, heuristic, source, dest, local_lim):
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


def hPathFind (graph, heuristic, source, dest, local_lim):
  total_visit_count = 0
  source_region = ((source[0] // 10) * 10 + 1, (source[1] // 10) * 10 + 1)
  dest_region = ((dest[0] // 10) * 10 + 1, (dest[1] // 10) * 10 + 1)

  src2region, search_count1, found = Astar (graph, heuristic, source, source_region)
  region_path, search_count2 = regionalAstar (graph, heuristic, source_region, dest_region, 10) 
  region2dst, search_count3, found = Astar (graph, heuristic, dest_region, dest)

  path = region2dst + region_path + src2region 
  search_cost = search_count1 + search_count2 + search_count3
  return path, search_cost 
