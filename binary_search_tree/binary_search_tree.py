import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into tree
    def insert(self, value):
        if value < self.value:  # Check if the new nodes value is less than the current value
            if self.left is None:  # go left
                self.left = BinarySearchTree(value)  # repeat search
            else:
                self.left.insert(value)  # insert the value
        else:
            if self.right is None:  # go right
                self.right = BinarySearchTree(value)  # repeat search
            else:
                self.right.insert(value)  # insert the value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        elif self.right and self.value < target:
            return self.right.contains(target)

        elif self.left and self.value > target:
            return self.left.contains(target)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)  # pass cb

        if self.left:  # same for left
            self.left.for_each(cb)

    # DAY 2 Project -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:  # If a node is passed in recursively, run code block, otherwise end
            self.in_order_print(node.left)  # pass in left
            print(node.value)  # print current value
            self.in_order_print(node.right)  # pass in right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()  # instantiate Queue Class
        storage.enqueue(node)  # add root to queue

        while storage.len() > 0:  # While there is something in queue
            current_node = storage.dequeue()  # dequeue current node
            print(current_node.value)

            if current_node.left:  # check if left child exists
                storage.enqueue(current_node.left)  # enqueue left child

            if current_node.right:  # check if a right child exists
                storage.enqueue(current_node.right)  # enqueue right child

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()  # instantiate Stack Class
        storage.push(self)  # add root to stack
        while storage.len() > 0:  # While there is something in stack
            current_node = storage.pop()  # Grab (top) node from stack
            print(current_node.value)

            if current_node.left:  # If left
                storage.push(current_node.left)  # Add left to stack

            if current_node.right:  # If right
                storage.push(current_node.right)  # Add right to stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
