
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # the max number of nodes it can hold
        # the current number of nodes (start the count at 0 and increment in functions)
        self.size = 0
        # a doubly linked list to store the key:value pairs in order
        self.order = DoublyLinkedList()
        self.storage = {}  # empty dictionary to hold the key:value pairs

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:  # if the key is in the storage
            node = self.storage[key]  # get the key
            # then move the key value pair to the end
            self.order.move_to_end(node)
            return node.value[1]  # return the value
        else:
            return None  # return none if the key is not in the cache

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # cache size, remove from least (rightest most), add to the front
        # duplicates, if there is a duplicate, override value, move it to front
        # check duplicate first, then cache size

        # Additionally, in the case that the key already exists in the cache, we simply
        # want to overwrite the old value associated with the key with'
        # the newly-specified value.
        if key in self.storage:
            node = self.storage[key]  # sets existing value to new value
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        # If the cache is already at max capacity
        # before this entry is added, then the oldest entry in the
        # cache needs to be removed to make room.
        if self.size == self.limit:
            del self.storage[self.order.remove_from_head()[0]]
            self.order.remove_from_head()
            self.size -= 1

        # Adds the given key-value pair to the cache.
        self.order.add_to_tail((key, value))
        # Add to dictionary
        self.storage[key] = self.order.tail
        self.size += 1
