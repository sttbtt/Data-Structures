"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        print('insert_after-----------')
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # wrap the input value in a new ListNode
        new_node = ListNode(value=value)
        new_node.next = self.head
        new_node.prev = None
        # check if we have anything in our linked list
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def remove_from_head(self):
        # check to see if we have an empty list by checking head == None
        if not self.head:
            return None
        # what if only one element, check if self.head.next == None
        if self.head.next is None:
            # grab a secon reference to our current head element
            head = self.head
            # set self.head and self.tail to None
            self.head = None
            self.tail = None
            # return value of old head element
            return head.value
        # if we have multiple elements
        else:
            # grab a secon reference to our current head element
            head = self.head
            self.delete(head.value)
            return head.value

    def add_to_tail(self, value):
        self.tail.insert_after(value)
        self.tail = self.tail.next

    def remove_from_tail(self):
        # check to see if we have an empty list by checking tail == None
        if not self.tail:
            return None
        # what if only one element, check if self.head.next == None
        if self.tail.prev is None:
            # grab a secon reference to our current head element
            tail = self.tail
            # set self.head and self.tail to None
            self.tail = None
            self.none = None
            # return value of old tail element
            return tail.value
        # if we have multiple elements
        else:
            # grab a secon reference to our current tail element
            tail = self.tail
            self.delete(tail.value)
            return tail.value 

    def move_to_front(self, node):
        # grab a reference to node
        node_value = node.value
        if node == self.head:
            return
        else:
            # delete node
            node.delete()
            # move node to head
            self.add_to_head(node_value)
          
    def move_to_end(self, node):
        # grab a reference to node
        node_value = node.value
        if node == self.tail:
            return
        else:
            # delete the node
            node.delete()
            print('Delete')
            # move node to tail
            self.add_to_tail(node_value)

    def delete(self, node):
        # check if ouir list is completely empty
        if not self.head and not self.tail:
            return None

        # if oour list has only a single node, then when we delete it
        # both self.head and self.tail should be none
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # check if the given node is the head
        if self.head == node:
            # set the self.head point to the net node
            self.head = node.next
            # delete the node
            node.delete()

        # check if the given node is the tail
        if self.tail == node:
            # set the self.tail pointer to the previous node
            self.tail = node.prev
            # delete the noe
            node.delete()

        # otherwise, the node we're looking to the delete is in the middle of the list
        else:
            # just call node.delete
            node.delete()

        pass

    def get_max(self):
        # check to see if we have an empty list by checking head == None
        if not self.head:
            return None
        # init a `current_node` variable to keep track of where we are in the 
        # linked list as we're iterating
        current_node = self.head
        max_node = self.head
        # check while current_node is a valid (non-None) node
        while current_node:
            # check if current node is > max_node, 
            # if yes assign current_node to max_node
            if current_node.value > max_node.value:
                max_node.value = current_node.value
            current_node = current_node.next
        return max_node.value


