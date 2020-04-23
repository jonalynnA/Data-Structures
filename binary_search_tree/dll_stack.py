import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # using a double linked list allows for a time complexity of O(1)
        # the action of push or pop can only be done at 1 position the front aka the top aka the head
        # no matter the length of the list you perform a push or pop in 1 step
        self.storage = DoublyLinkedList()

    def push(self, value):
        # push happens when you need to add something to the front of the list (the head)
        # like when you're washing dishes and you stack the clean plates in the cabinet
        # the top dish is continuously being added to by placing another plate on top (on the head)
        # as your list grows, you push the head further down in the stack

        # no need to check for an empty list since e are insering or adding to the stack here

        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        # pop is when you remove an item
        # in the case of stack you are removing an item from the head (the top)
        # using the example above, once you have a stack of nice clean dishes whenever you
        # go to grab a dish you grab the one on top
        # you remove a dish from the stack by taking the top dish

        # you cannot remove something that doesn't exist, so check for empty list first

        if self.size < 1:
            return None
        else:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size
