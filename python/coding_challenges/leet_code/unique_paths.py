"""
REVISIT: Base DP problem
Question: https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?



Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6


Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.first_implementation(m, n)
        # return self.second_implementation(m,n)

    def first_implementation(self, height: int, width: int) -> int:
        """
        The possible moves for the robot to make at any grid point is to either move right or down.
        At each grid they initially have one possible choice to make. Taking into account all of the choices taken
        to get to the current gridpoint based on whether they came in from a tile higher or a tile to the left.
        We add both of those possibilities to denote how they could have gotten where they currently are.
        """
        # Initialize the DP array
        dp = [[1 for _ in range(width)] for _ in range(height)]
        # At each col * row calculation is adding the steps taking from the previous two choices
        # and stating them as the amount of choices possible to get to the current spot in the grid.
        for col in range(1, height):
            for row in range(1, width):
                dp[col][row] = dp[col - 1][row] + dp[col][row - 1]
        # The final grid point where the start is located is the culmination of all of the possible moves.
        return dp[height - 1][width - 1]

    def second_implementation(self, height: int, width: int) -> int:
        """
        Same as the first implementation but using a dict instead of a 2d array
        """
        dp = {}
        for x in range(height):
            for y in range(width):
                dp[(x, y)] = 1
        for col in range(1, height):
            for row in range(1, width):
                dp[(col, row)] = dp[(col - 1, row)] + dp[(col, row - 1)]
        return dp[(height-1, width-1)]

