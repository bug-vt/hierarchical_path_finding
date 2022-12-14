from pqueue import PriorityQueue
from astar import noHeuristic
from astar import manhattan
from astar import euclidian
from astar import Astar
from graph import shortestPath 
from graph import printGraph
from graph import visitedNodesCount
from tile_map import TILE_MAP1
from tile_map import TILE_MAP2
from graph import buildGraph


def adjacentRegion (lv2_graph, graph, node, size, local_lim, heuristic):
  visit_count = 0
  neighbors = []
  x = node.x 
  y = node.y

  offsets = [(-size,0), (0, size), (size, 0), (0, -size)]
  for off_y, off_x in offsets:
    if x + off_x >= 0 and x + off_x < 42 and y + off_y >= 0 and y + off_y < 42:
      graph = buildGraph (TILE_MAP1)
      found, path = Astar (graph, heuristic, graph[y][x], graph[y+off_y][x+off_x]\
                           ,search_lim = local_lim)

      if found:
        #printGraph (graph, path)
        neighbors.append ((lv2_graph[y + off_y][x + off_x], len (path)))
        visit_count += visitedNodesCount (graph)

  return neighbors, visit_count


def hPathFind (lv2_graph, graph, heuristic, source, dest, local_lim):
  found = False
  total_visit_count = 0
  source.dist = 0
  source.cost = heuristic (source, dest)
  visited = []
  queue = PriorityQueue ()

  region_size = 10
  for y in range (1, len (lv2_graph), region_size):
    for x in range (1, len (lv2_graph[y]), region_size):
      if not lv2_graph[y][x].isWall:
        queue.insert (lv2_graph[y][x])

  while not queue.empty ():
    current = queue.extractMin ()
    visited.append (current)
    if current == dest:
      found = True
      break
    
    neighbors, local_visit_count = adjacentRegion (lv2_graph, graph, current, region_size, local_lim*2, heuristic)
    total_visit_count += local_visit_count
    for node, weight in neighbors:
      if node.dist > current.dist + weight:
        node.dist = current.dist + weight
        node.cost = node.dist + heuristic (node, dest)
        node.parent = current
        queue.decreaseKey (node)

  return found, shortestPath (lv2_graph, dest.x, dest.y), total_visit_count
