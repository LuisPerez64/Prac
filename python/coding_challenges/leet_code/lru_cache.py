"""
Question: https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise,
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.
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

# #First implementation. Redoing using the ordered dict structure.
# Time Complexity for get/put were governed by the rank function.
# If that and the eviction could be streamlined then this solution is comparable.
# class LRUCache:

#     def __init__(self, capacity: int):
#         print("New Cache")
#         self.cache = {}
#         self.max_capacity = capacity
#         self.max_rank = 0
#         # self.ranking = deque()

#     @property
#     def size(self):
#         return len(self.cache)

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # increment the rank of the element
#         self._rank(key)
#         return self.cache.get(key).get('val')


#     def put(self, key: int, value: int) -> None:
#         # Check if the key is in the cache already
#         if key not in self.cache:
#             # key did not exist. Check if it will fit.
#             if self.size >= self.max_capacity:
#                 # need to evict the last used key from the cache.
#                 self._evict()
#             self.cache[key] = {'val': value, 'rank': 0}
#         else:
#             self.cache[key]['val'] = value
#         # The ranking algo could change at any point so establishin the rank from there.
#         self._rank(key, is_insert=True)

#     def _evict(self):
#         """
#         Evict a key based on the last used criteria.
#         This moves the complexity away from O(1) if we use the base rank
#         """
#         tmp = float('inf')
#         key = None
#         for k, v in self.cache.items():
#             if v.get('rank') < tmp:
#                 tmp = v.get('rank')
#                 key = k
#         if key is not None:
#             # Just in case the capacity is at 0
#             del self.cache[key]

#     def _rank(self, key: int, is_insert = False):
#         # if is_insert:
#             # If inserting a new key need to ensure that it's got a rank higher than the rest.
#         tmp = self.max_rank
#         self.max_rank += 1

#         if key in self.cache:
#             self.cache.get(key)['rank'] = tmp
#             self.max_rank = max(self.cache.get(key).get('rank'), self.max_rank)
#         # print(key, is_insert, self.max_rank, self.cache.items())


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
