class Heap:
  def __init__(self):
    self.storage = []

  # insert the value into the heap
  def insert(self, value):
    self.storage.append(value)
    # print(f'storage: {self.storage}')
    self._bubble_up(self.get_size() - 1)

  def delete(self):
    if self.get_size():
      # print(f'storage delete: {self.storage}')
      deleted_element = self.storage[0]
      self.storage[0], self.storage[self.get_size() - 1] = self.storage[self.get_size() - 1], self.storage[0]
      # print(f'storage delete: {self.storage}')
      self.storage.pop(self.get_size() - 1)
      # print(f'storage delete: {self.storage}')
      self._sift_down(0)
      return deleted_element


  # get the max element in constant time
  def get_max(self):
    # return whatever is at storage[0]
    # print(f'Max: {self.storage[0]}')
    return self.storage[0]

  def get_size(self):
    # print(f'Get Size: {len(self.storage)}')
    return len(self.storage)

  # called as a helper function in insert
  # "buble up" the newely inserted element to a valid spot in the heap
  def _bubble_up(self, index):
    # print(f'Index: {index}')
    # we'll use the child to parent formula here
    # loop until parent index is a valid heap index (or recurse)
    while (index - 1) // 2 >= 0:
    # child has access to the parent at this point
    # compare the child's value against its parent's value
    # if child's value > parent's value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap these two elements via ther indices
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      # repeat this process until the child no longer needs to be swapped with it's parent
      # update the index to be the parent's index
      index = (index - 1) // 2

  # called as a helper function in delete
  # "sifts down" the element at the top of the heap
  def _sift_down(self, index):
    # assign left, right and largest variables
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    # check if left is < heap size and that left is > than index
    if left < self.get_size() and self.storage[left] > self.storage[largest]:
      # if true eassign left to largest
      largest = left
    else:
      # if false assign index to largest
      largest = index
    # check if right is < heap size and that right is > than index
    if right < self.get_size() and self.storage[right] > self.storage[largest]:
      # if true assign right to largest
      largest = right
    # check if largest != index
    if largest != index:
      # if true swap index and largest and recurse
      self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
      self._sift_down(index)
    # check to see if still a valid max-heap
    for i in range(self.get_size() - 1):
      if self.storage[i + 1] > self.storage[i]:
        self._bubble_up(i + 1)



    # trying with while loop
    # if (2 * index + 2) < self.get_size() - 1:
    #   if self.storage[index] < self.storage[2 * index + 1]:
    #     self.storage[index], self.storage[2 * index + 1] = self.storage[2 * index + 1], self.storage[index]
    # else:
    #   while (2 * index + 2) > self.get_size() + 1:
    #     print(f'Size: {self.get_size()}')
    #     print(f'sift_down index: {index}')
    #     if self.storage[2 * index + 1] >= self.storage[2 * index + 2]:
    #       self.storage[index], self.storage[2 * index + 1] = self.storage[2 * index + 1], self.storage[index]
    #       index = 2 * index + 1
    #     elif self.storage[2 * index + 2] >= self.storage[2 * index + 1]:
    #       self.storage[index], self.storage[2 * index + 2] = self.storage[2 * index + 2], self.storage[index]
    #       index = 2 * index + 2