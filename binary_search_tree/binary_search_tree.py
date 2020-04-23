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
        # if value is less than self.value
        if value < self.value:
            # if left is none
            if self.left is None:
                # set left to be node
                self.left = BinarySearchTree(value)
                # if not set left node this value
            else:
                self.left.insert(value)

        else:
          # do same for right side
            if value >= self.value:

                if self.right is None:

                    self.right = BinarySearchTree(value)
        # if it has a node, call self.right.insert with this value
            else:
                self.right.insert(value)

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
        if self.right is None:
            pass
        else:
            self.right.for_each(cb)  # pass cb

        if self.left is None:
            pass
        else:  # same for left
            self.left.for_each(cb)
        cb(self.value)

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
        queue = Queue()  # instantiate Queue Class
        queue.enqueue(self)  # add root to (end of) queue
        while queue.size() > 0:  # While there is something in queue
            current_node = queue.dequeue()  # grab node from front of queue
            print(current_node.value)

            if current_node.left:  # If left
                queue.enqueue(current_node.left)  # Add left to end of queue

            if current_node.right:  # If right
                queue.enqueue(current_node.right)  # Add right to end of queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()  # instantiate Stack Class
        stack.push(self)  # add root to stack
        while stack.size() > 0:  # While there is something in stack
            current_node = stack.pop()  # Grab (top) node from stack
            # Print current_node value
            print(current_node.value)
            if current_node.left:  # If left
                stack.push(current_node.left)  # Add left to stack
            if current_node.right:  # If right
                stack.push(current_node.right)  # Add right to stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
