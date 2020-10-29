"""
REVISIT: The relayed total is actually not tied to the number of nodes but the number of unions
    needed at each instance.
Question: https://leetcode.com/problems/number-of-islands-ii
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""
from collections import defaultdict
from typing import List

from implementations.data_structures import DSU


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        """
        Use a DSU structure to mark the connections between the nodes in the matrix.
        For every node, grab its adjacent pairs from the current "grid", and see if there
        are any connections to it based on their existence in the grid.
        For each new island being added, that's not in the adjacency dict increment the total.
        For each island that's already connected to the same root, based on the DSU.Union op,
            decrease the total count of islands at that stage.

        """
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid = defaultdict(set)
        result = []
        dsu = DSU()

        total = 0
        # O(k)
        for position in positions:
            position = tuple(position)
            total += 1 if position not in grid else 0

            row = position[0]
            col = position[1]
            # TC: O(4)
            for rowOff, colOff in offsets:
                r = row + rowOff
                c = col + colOff
                if r >= 0 and r < m and c >= 0 and c < n and (r, c) in grid:
                    grid[position].add(tuple([r, c]))
            # TC: O(k * m alpha(n)) -- The inverse Ackerman function
            for adj in grid[position]:
                # If there was no union operation then don't change the total
                # Only need to decrease it if we have joined two previously disjoint islands.
                total += -1 if dsu.union(position, adj) else 0

            result.append(total)
        return result

# from collections import defaultdict

# NEIGHBOURS = [[-1, 0], [1, 0], [0,-1], [0, 1]]

# class Solution:
#     def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
#         grid = []
#         for i in range(m):
#             grid.append([0] * n)

#         result = []
#         grid_map = defaultdict(int)
#         grid_height = defaultdict(int)
#         island_num = 1
#         total = 0

#         for r, c in positions:
#             if grid[r][c] == 0:
#                 parent = None
#                 for i, j in NEIGHBOURS:
#                     x, y = r + i, c + j
#                     if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
#                         if parent is None:
#                             parent = grid[x][y]
#                             grid[r][c] = parent
#                         else:
#                             total += self.merge(grid_map, grid_height, grid[x][y], parent)
#                 if parent is None:
#                     grid[r][c] = island_num
#                     grid_map[island_num] = island_num
#                     grid_height[island_num] = 0
#                     island_num += 1
#                     total += 1
#             result.append(total)

#         return result

#     def merge(self, grid_map, grid_height, node1, node2):
#         p1 = self.get_parent(grid_map, node1)
#         p2 = self.get_parent(grid_map, node2)

#         if p1 == p2:
#             return 0

#         if grid_height[p1] > grid_height[p2]:
#             grid_map[p2] = p1
#         else:
#             grid_map[p1] = p2
#             grid_height[p2] = max(grid_height[p2], grid_height[p1] + 1)

#         return -1

#     def get_parent(self, grid_map, key):
#         while key != grid_map[key]:
#             key = grid_map[key]
#         return key
