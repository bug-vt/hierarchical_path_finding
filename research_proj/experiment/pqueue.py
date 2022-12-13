class PriorityQueue:
  def __init__ (self):
    self.queue = []

  def empty (self):
    return len (self.queue) == 0 

  def insert (self, new_node):
    for i in range (len (self.queue)):
      if new_node.cost < self.queue[i].cost:
        self.queue.insert (i, new_node)
        return

    self.queue.append (new_node)

  def extractMin (self):
    return self.queue.pop (0)

  def pop (self, node):
    for i in range (len (self.queue)):
      if node == self.queue[i]:
        return self.queue.pop (i)

  def decreaseKey (self, node):
    self.pop (node)
    self.insert (node)
