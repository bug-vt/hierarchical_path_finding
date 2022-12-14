from PIL import Image
from graph import WALL

def color10x10 (pix, x, y, color):
  for i in range (x*10, x*10 + 10):
    for j in range (y*10, y*10 + 10):
      if i == x*10 or i == x*10 + 9 or j == y*10 or j == y*10 + 9:
        pix[i, j] = (200, 200, 200, 255) 
      else:
        pix[i, j] = color


def saveGraph2Img (graph, file_name, path=[]):
  img = Image.new (mode="RGBA", size=(len (graph)*10, len (graph[0])*10))
  pix = img.load ()

  for y in range (len (graph)):
    for x in range (len (graph[y])):
      if graph[y][x] == WALL:
        color10x10 (pix, x, y, (0,0,0,255))
        continue
      
      in_route = False
      for node in path:
        if x == node.x and y == node.y:
          if node == path[0]:
            color10x10 (pix, x, y, (255,0,0,255))
          elif node == path[len (path) - 1]:
            color10x10 (pix, x, y, (0,0,255,255))
          else:
            color10x10 (pix, x, y, (0,255,0,255))
          in_route = True
          break

      if not in_route: 
        color10x10 (pix, x, y, (255,255,255,255))

   
  img.save (file_name)
