# Hierarchical Path Finding

#### Members: Addie Audette, Bug Lee, Annorah Lewis, Luke Marks
#### Last updated: December 2022

## Introduction
The problem of finding an optimal path arises in many application domains including navigation, robotics, networking, and video games. There are different flavors of algorithms that correctly find the shortest (or near shortest) path between two or more nodes in a graph.

Two algorithms, Dijkstra and A*, are widely known and guarantee to find the shortest path in general cases. When the problem domain is restricted to only containing non-negative edge weights, the Dijkstra can find the shortest path to all vertices that are connected to the graph[4]. On the other hand, the A* algorithm, the successor of Dijkstra, is generally more suitable for application as it demands less computation with the help of an admissible heuristic function.

However, the naive A* algorithm is no longer sufficient for modern real-time applications. Given the sheer number of the nodes for the graph in modern applications, computation demands are too high to run a naive A* algorithm simultaneously for hundreds, if not thousands, of agents [1]. Thus, like many problems in computer science, adding a hierarchy is a solution to reduce the complexity of the problem.

...Continue on the research paper.

## [Our research Paper](research_proj/hierarchical_path_finding.pdf)

## [Beamer Presentation](beamer/beamer_hierarchical_path_finidng.pdf)

## Running experiments
Go to the `research_proj/experiment` directory and then run
```
./benchmark.py
```
Visual results from the benchmark will be located at `research_proj/experiment/visual`.
