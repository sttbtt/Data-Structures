class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.size += 1
    self.storage.insert(0, item)
  
  def dequeue(self):
    if self.len() == 0:
      return None
    else:
      self.size -= 1
      return self.storage.pop()

  def len(self):
    return self.size
