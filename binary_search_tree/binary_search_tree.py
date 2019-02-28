class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value:
      if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)
      elif value >= self.value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
    else:
      self.value = value


  def contains(self, target):
    if self.value == target:
      return True
    if target >= self.value:
      if self.right.value == target:
        return True
      else:
        self.contains(target)
    if target < self.value:
      if self.left.value == target:
        return True
      else:
        self.contains(target)

  def get_max(self):
    pass

