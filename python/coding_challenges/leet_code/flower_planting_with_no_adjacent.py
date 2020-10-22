"""
Question: https://leetcode.com/problems/flower-planting-with-no-adjacent/
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi]
describes the existence of a bidirectional path from garden xi to garden yi.
In each garden, you want to plant one of 4 types of flowers.

There is no garden that has more than three paths coming into or leaving it.

Your task is to choose a flower type for each garden such that,
for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden.
The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.



Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

"""
# class DSU(object):
#     def __init__(self):
#         self.forest = {}

#     def make_set(self, node):
#         if node not in self.forest:
#             self.forest[node] = {'parent': node, 'rank': 0}
#         return node

#     def find(self, node):
#         root = self.make_set(node)
#         while self.forest[root]['parent'] != root:
#             root = self.forest[root]['parent']

#         while self.forest[node]['parent'] != root:
#             parent = self.forest[node]['parent']
#             self.forest[node]['parent'] = root
#             node = parent

#         return root

#     def union(self, x, y):
#         xr = self.find(x)
#         yr = self.find(y)

#         if xr == yr:
#             return False

#         if self.forest[xr]['rank'] < self.forest[yr]['rank']:
#             # swap the two nodes to simplify parent selection
#             xr, yr = yr, xr

#         self.forest[yr]['parent'] = xr
#         self.forest[xr]['rank'] += 1
#     def get_parents(self):
#         # Get the parents present in the forest
#         roots = set()
#         for rel in self.forest.values():
#             roots.add(rel.get('parent'))

#         return roots

# class Solution:
#     def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
#         """
#         Do a Union Find to find all of the discrete root nodes.
#         Once they've been found iterate over the nodes and assign the flower garden
#         to each child from round robin selection.
#         """
#         dsu = DSU()
#         adjacency_list = defaultdict(set)

#         for edge in paths:
#             dsu.union(*edge)
#             adjacency_list[edge[0]].add(edge[1])
#             adjacency_list[edge[1]].add(edge[0])
#         # for each of the roots initialize the flower they will give the child.
#         flower = defaultdict(int)
#         result = [0] * n
#         for node in dsu.get_parents():
#             result[node -1] = 1
#             flower[node] = 2
#         for node in range(1, n+1):
#             if result[node -1] != 0:
#                 # parent nodes get first pick.
#                 continue
#             parent = dsu.find(node)
#             cur_flower = flower[parent]
#             for adj in adjacency_list[node]:
#                 if result[adj -1] == cur_flower:
#                     cur_flower = (cur_flower) % 4 + 1

#             result[node -1] = cur_flower
#             flower[parent] = (cur_flower )% 4 +1

#         return [x if x else 1 for x in result]
from collections import defaultdict


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        g = defaultdict(list)
        for x, y in paths:
            g[x].append(y)
            g[y].append(x)
        plantdict = {i: 0 for i in range(1, N + 1)}
        for garden in g:
            pick = set(range(1, 5))
            for each in g[garden]:
                if plantdict[each] != 0 and plantdict[each] in pick:
                    pick.remove(plantdict[each])
            plantdict[garden] = pick.pop()
        return [plantdict[x] if plantdict[x] != 0 else 1 for x in range(1, N + 1)]
