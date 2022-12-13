from pqueue import PriorityQueue
from graph import Node
from graph import adjacent

def dijkstra (graph, source):
  source.dist = 0
  visted = []
  queue = PriorityQueue ()
  
  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if not graph[y][x].isWall:
        queue.insert (graph[y][x])

  while not queue.empty ():
    current = queue.extractMin ()
    visted.append (current)

    for node in adjacent (graph, current):
      if node.dist > current.dist + 1:
        node.dist = current.dist + 1
        node.parent = current
        queue.decreaseKey (node)
