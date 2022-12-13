#!/usr/bin/env python3

from tile_map import TILE_MAP1
from tile_map import TILE_MAP2
from graph import buildGraph
from graph import printGraph
from graph import shortestPath 
from graph import visitedNodesCount
from dijkstra import dijkstra


def main ():

  graph = buildGraph (TILE_MAP1)
  printGraph (graph)
  dijkstra (graph, graph[1][1]) 
  path = shortestPath (graph, 30, 11)
  printGraph (graph, path)
  print (visitedNodesCount (graph))

if __name__ == "__main__":
  main ()
