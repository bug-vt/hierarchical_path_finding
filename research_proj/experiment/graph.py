class Node:
  def __init__ (self, x, y, isWall=False):
    self.x = x
    self.y = y
    self.dist = 100000000
    self.parent = None
    self.isWall = isWall


def buildGraph (tile_map):
  graph = []  
  rows = tile_map.splitlines ()
  for y in range (len (rows)):
    graph.append([])
    for x in range (len (rows[y])):
      isWall = False
      if (rows[y][x] == "#"):
        isWall = True

      node = Node (x, y, isWall)
      graph[y].append (node)    

  return graph

def adjacent (graph, node):
  neighbors = []
  x = node.x
  y = node.y

  if not graph[y - 1][x].isWall:
    neighbors.append (graph[y - 1][x])
  if not graph[y][x + 1].isWall:
    neighbors.append (graph[y][x + 1])
  if not graph[y + 1][x].isWall:
    neighbors.append (graph[y + 1][x])
  if not graph[y][x - 1].isWall:
    neighbors.append (graph[y][x - 1])

  return neighbors

def printGraph (graph, path=None):
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if graph[y][x].isWall:
        print ("#", end="")
        continue

      if path:
        if (graph[y][x] in path):
          print (".", end="")
        else:
          print (" ", end="")
        continue

      print (" ", end="")
    print ()
 
def shortestPath (graph, x, y):
  current = graph[y][x]
  path = [current]
  while current.parent != None:
    path.append (current.parent)
    current = current.parent

  return path

def visitedNodesCount (graph):
  node_count = 0 
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if not graph[y][x].isWall and graph[y][x].parent != None:
        node_count += 1

  return node_count
