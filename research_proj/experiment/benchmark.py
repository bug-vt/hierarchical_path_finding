#!/usr/bin/env python3

from tile_map import TILE_MAP1
from tile_map import TILE_MAP2
from graph import buildGraph
from graph import printGraph
from astar import noHeuristic
from astar import manhattan
from astar import euclidian
from astar import Astar
from h_path_find import hPathFind
from timeit import default_timer as time
from visualizer import saveGraph2Img 

def main ():
  print ("%s" % ("-" * 50))
  print ("Benchmarking Hierarchical Path Finding")
  print ("%s" % ("-" * 50))

  graph = buildGraph (TILE_MAP1)
  source = (5,35)
  dest = (30, 25)

  print ("\nDijkstra")
  # Running A* with no heuristic is equivalent to running Dijkstra
  heuristic = noHeuristic
  start = time ()
  path, search_count, found = Astar (graph, heuristic, source, dest) 
  duration = time () - start

  saveGraph2Img (graph, "visual/dijkstra.png", path) 
  print ("# of visited nodes: %d" % search_count)
  print ("Path length: %d" % len (path))
  print ("Duration: %f ms" % (duration * 1000))

  print ("\nA*")
  heuristic = euclidian
  #heuristic = manhattan
  start = time ()
  path, search_count, found = Astar (graph, heuristic, source, dest) 
  duration = time () - start

  saveGraph2Img (graph, "visual/Astar.png", path) 
  print ("# of visited nodes: %d" % search_count)
  print ("Path length: %d" % len (path))
  print ("Duration: %f ms" % (duration * 1000))


  print ("\nHierarchical Path Finding")
  heuristic = euclidian
  #heuristic = manhattan
  start = time ()
  path, search_count = hPathFind (graph, heuristic, source, dest, 10) 
  duration = time () - start

  saveGraph2Img (graph, "visual/hierarchical.png", path) 
  print ("# of visited nodes: %d" % search_count)
  print ("Path length: %d" % len (path))
  print ("Duration: %f ms" % (duration * 1000))


if __name__ == "__main__":
  main ()
