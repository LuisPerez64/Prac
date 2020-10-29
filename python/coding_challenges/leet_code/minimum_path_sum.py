"""
REVISIT: DP Problem, and the solution is a bit different from the others in that the original input is initialized.
Question: https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.first_implementation(grid)

    def first_implementation(self, grid: List[List[int]]) -> int:
        """
        Possible moves at each node right or down.
        The choice is based on which of the two origins would give the least costly path
        From the starting point [0,0] there is no previous history or choice.
        For every grid point where theres on origin i.e. topmost column then could only have come from the left.
            We just add that in.
        For points where we could have come from the left or above then register the least expensive option as origin.
        Iterate through the matrix and at the end relay the sum at the lower right gridpoint.
        Time complexity: O(m * n)
        Space Complexity: O(n)
            Could have been O(1) if the initial grid were used instead of the DP array, but overwriting input would
            require some input from the interviewer.
        """

        dp = [[grid[x][y] for y in range(len(grid))] for x in range(len(grid[0]))]
        col = row = 0
        for col in range(len(grid)):
            for row in range(len(grid[0])):
                if col > 0 and row > 0:
                    # Origin was from above or to the left so choose the path that was least costly.
                    dp[col][row] = dp[col][row] + min(dp[col - 1][row], dp[col][row - 1])
                elif col > 0:
                    # Must have come from above as the row is 0
                    dp[col][row] += dp[col - 1][row]
                elif row > 0:
                    # Could only come from the left so add that in.
                    dp[col][row] += dp[col][row - 1]
        return dp[col][row]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
