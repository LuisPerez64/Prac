"""
Question: https://leetcode.com/problems/number-of-islands/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.first_implementation(grid)

    def first_implementation(self, grid: List[List[str]]) -> int:
        """
        Backtracking solution for this.
        Find the first location where the value is 1.
        search all valid adjacent points in the matrix.
        Mark visited cells with -1 to not revisit.
        If at least 1 location is 1 increment count for that instance.
        Backtrack when no possible moves and search for the next [1] grid.
        """

        if not len(grid) or not len(grid[0]):
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        islands = 0
        moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

        def valid_move(row, col):
            return not (row < 0 or row >= num_rows or col < 0 or col >= num_cols \
                        or grid[row][col] != "1")

        def backtrack(row, col):
            if not valid_move(row, col):
                return
            grid[row][col] = "-1"

            for rowOffset, colOffset in moves.values():
                backtrack(row + rowOffset, col + colOffset)

        for c_row in range(num_rows):
            for c_col in range(num_cols):
                if valid_move(c_row, c_col):
                    islands += 1
                    backtrack(c_row, c_col)
        return islands
