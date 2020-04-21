import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# NOTE: Think of queue like music queue or store line or grabbing milk...first in last out
# NOTE: Think of stack like a stack of plates, last one on stack first one off stack


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # If you didn't have a .prev on your tail node, you would have to start
        # at the beginning of the list so O(n) to find the tail versus being able to traverse
        # backwards and have complexity of O(1). If you did not have to queue with enque and deque
        # then you could use LL

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add item to the list (First in last out)
        # function add_to_tail from DoublyLinkedList class does this
        # list size is important, remember to update list size with each function
        # enqueue adds one to the list so size will increase by 1
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        # remove item from the list
        # function remove_from_head from DoublyLinkedList class does this
        # list size is important, remember to update list size
        # dequeue removes a value from the list so size decreases by 1
        if self.size == 0:  # could also say if < 1
            return None
        else:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
