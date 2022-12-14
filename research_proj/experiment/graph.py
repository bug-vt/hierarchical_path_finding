import numpy as np

WALL = 1

class Node:
  def __init__ (self, x, y, parent=None):
    self.x = x
    self.y = y
    self.cost = 100000000
    self.dist = 100000000
    self.parent = parent 

  def equal (self, node):
    return self.x == node.x and self.y == node.y



def buildGraph (tile_map):
  graph = []  
  rows = tile_map.splitlines ()
  graph = np.empty ([len (rows), len (rows[0])], dtype=np.int32)
  for y in range (len (rows)):
    for x in range (len (rows[y])):
      if (rows[y][x] == "#"):
        graph[y][x] = WALL
      else:
        graph[y][x] = 0

  return graph

def adjacent (graph, node):
  neighbors = []
  x = node.x
  y = node.y

  offsets = [(-1,0), (0, 1), (1, 0), (0, -1)]
  for off_y, off_x in offsets:
    if graph[y + off_y][x + off_x] != WALL:
      neighbors.append (Node (x + off_x, y + off_y, node))

  return neighbors

def haveVisited (visited, current):
  for node in visited:
    if node.equal (current):
      return True

  return False

def printGraph (graph, path=[]):
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if graph[y][x] == WALL:
        print ("#", end="")
        continue
      
      in_route = False
      for node in path:
        if x == node.x and y == node.y:
          print (".", end="")
          in_route = True
          break

      if not in_route: 
        print (" ", end="")

    print ()
 
def path (node):
  current = node
  path = []
  while current != None:
    path.append (current)
    current = current.parent

  return path

