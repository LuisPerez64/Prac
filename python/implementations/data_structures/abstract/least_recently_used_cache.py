"""
Least Recently Used Cache implementation
"""
from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int):
        """
        Get the item at the key iff it exists.
        Mark that an operation took place on the key by moving it to the
        Last index in the order.
        """
        if key not in self:
            return -1
        # Update that it's been used and place it at the end of the dict
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value):
        """
        OrderedDict allows for insertion and remembers the order in which the insertions occured.
        Basically mixing a Dict and a PriorityQueue into one struct.
        """
        if key not in self:
            if len(self) + 1 > self.capacity:
                self.popitem(last=False)
            self[key] = value
        else:
            self[key] = value
            self.move_to_end(key)
