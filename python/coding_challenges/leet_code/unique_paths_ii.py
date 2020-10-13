"""
Question: https://leetcode.com/problems/unique-paths-ii/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.first_implementation(obstacleGrid)

    def first_implementation(self, obstacleGrid: List[List[int]]) -> int:
        """
        As there are fail cases the quickest resolve would be to expand on the 
        backtracking algo as the straight DP's handling of the obstacles 
        may be a bit out of scope.
        """
        num_rows = len(obstacleGrid)
        if not num_rows or not len(obstacleGrid[0]):
            return 0
        num_cols = len(obstacleGrid[0])
        move_set = [(0, 1), (1, 0)]  # + [(-1, 0), (0, -1)] # Move Down or Right in the grid.
        # Memoization to skip completed paths.
        # If memo[(row, col)] has been visited then we know if they yield a valid result or not.
        memo = {}

        def valid(row, col):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols and obstacleGrid[row][col] != 1

        def backtrack(row, col):
            if not valid(row, col):
                return 0

            if (row, col) in memo:
                tmp = memo[(row, col)]
                return tmp

            if row == num_rows - 1 and col == num_cols - 1:
                memo[(row, col)] = 1
                return 1

            # mark the current location in the grid as invalid to not revisit it, though this is not possible with 
            # only two planes of travel available. If we add the other dimensions it would be useful
            # orig = obstacleGrid[row][col]
            # obstacleGrid[row][col] = 1
            tmp = 0
            for rowOffset, colOffset in move_set:
                tmp += backtrack(row + rowOffset, col + colOffset)
            memo[(row, col)] = tmp
            # obstacleGrid[row][col] = orig
            return tmp

        return backtrack(0, 0)
