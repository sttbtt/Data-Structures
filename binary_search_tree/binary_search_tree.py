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
    if target < self.value:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif target > self.value:
      if self.right is None:
        return False
      return self.right.contains(target)
    else:
      return True

  def get_max(self):
     # check if the tree is empty
    if not self:
      return None
    # check if self.right doesn't exist
    if not self.right:
      # return value of the current node
      return self.value
    # otherwise, recurse to the right
    return self.right.get_max()


    # if self.value:
    #   return print(self.value)
    # self.right.get_max()


  def print_tree(self):
    if self.right:
      self.right.print_tree()
    print(self.value)
    if self.right:
      self.right.print_tree()

# bst = BinarySearchTree(8)
# bst.insert(3)
# bst.insert(10)
# bst.insert(1)
# bst.insert(6)
# bst.insert(4)
# bst.insert(7)
# bst.insert(14)
# bst.insert(13)

# print(bst.contains(13))
# print(bst.right.right.value)
# print(bst.print_tree())
# print(bst.get_max())
