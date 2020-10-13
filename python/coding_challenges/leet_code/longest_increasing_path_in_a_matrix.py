"""
Question: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or
move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.first_implementation(matrix)

    def first_implementation(self, matrix: List[List[int]]) -> int:
        """
        DFS approach with memoization.
        The memoization needs to take into account the len of the sequence at the value
        its either storing or retrieving.
        When storing only need the len of the path from the current node in the grid
        so removing the seq_len from previous iterations into the equation.
        When cutting the task down the seq_len gets added so paths adding in the len from the current path
        are not affected.
        Time Complexity: O(mn)
            The memoization ensures that the work from any one node is not repeated.
        Space Complexity: O(2(mn)) => O(mn)
            The max size of the memo dict and possible recursion depth
        """
        num_rows = len(matrix)
        if num_rows == 0 or len(matrix[0]) == 0:
            return 0
        num_cols = len(matrix[0])
        max_len = 0
        moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        memo = {} # Key (row, col), Val: Max path from this value

        def valid(row, col, prev_num):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols \
                   and matrix[row][col] != '#' and matrix[row][col] > prev_num

        def dfs(row, col, prev_num, seq_len):
            nonlocal max_len
            if not valid(row, col, prev_num):
                return 0

            if (row, col) in memo:
                return memo[(row, col)] + seq_len

            cur_val = matrix[row][col]
            matrix[row][col] = '#'
            tmp_len = seq_len

            for rowOffset, colOffset in moves.values():
                tmp_len = max(dfs(row + rowOffset, col+colOffset, cur_val, seq_len + 1), tmp_len)
            matrix[row][col] = cur_val
            if tmp_len > max_len:
                max_len = tmp_len
            # The - seq_len was the missing piece... Need the path produced from just this node not aggregated.
            memo[(row, col)] = tmp_len - seq_len

            return tmp_len

        for row in range(num_rows):
            for col in range(num_cols):
                dfs(row, col, float('-inf'), 1)
        return max_len
