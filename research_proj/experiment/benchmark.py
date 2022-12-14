#!/usr/bin/env python3

from tile_map import TILE_MAP1
from tile_map import TILE_MAP2
from graph import buildGraph
from graph import printGraph
from astar import noHeuristic
from astar import manhattan
from astar import euclidian
from astar import Astar
#from h_path_find import hPathFind
from timeit import default_timer as time

def main ():
  print ("%s" % ("-" * 50))
  print ("Benchmarking Hierarchical Path Finding")
  print ("%s" % ("-" * 50))

  graph = buildGraph (TILE_MAP1)

  print ("\nDijkstra")
  # Running A* with no heuristic is equivalent to running Dijkstra
  heuristic = noHeuristic
  start = time ()
  path, search_count = Astar (graph, heuristic, (19,1), (31,23)) 
  duration = time () - start

  printGraph (graph, path)
  print ("# of visited nodes: %d" % search_count)
  print ("Duration: %f ms" % (duration * 1000))

  print ("\nA*")
  #heuristic = euclidian
  heuristic = manhattan
  start = time ()
  path, search_count = Astar (graph, heuristic, (19,1), (31,23)) 
  duration = time () - start

  printGraph (graph, path)
  print ("# of visited nodes: %d" % search_count)
  print ("Duration: %f ms" % (duration * 1000))


#  print ("\nHierarchical Path Finding")
#  graph = buildGraph (TILE_MAP1)
#  lv2_graph = buildGraph (TILE_MAP1)
#
#  #heuristic = euclidian
#  heuristic = manhattan
#  start = time ()
#  found, path, visit_count = hPathFind (lv2_graph, graph, heuristic, lv2_graph[1][11], lv2_graph[21][31], 10) 
#  duration = time () - start
#
#  printGraph (lv2_graph, path)
#  print ("# of visited nodes: %d" % visit_count)
#  print ("Duration: %f ms" % (duration * 1000))


if __name__ == "__main__":
  main ()
