"""
Question: https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Given a 01 matrix M, find the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""
from typing import List


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        one_nodes = []
        num_rows = len(M)
        if not num_rows:
            return 0
        num_cols = len(M[0])
        # we're looking for the longest line. Treating each as disjoint sets
        # flatten a 2d array into a 1d array. Note find way to traverse without actual flatten
        # From every node point we determine
        offsets = [(0, 1), (1, 0), (1, 1), (1, -1)]

        def is_valid(row, col):
            return row >= 0 and row < num_rows and col >= 0 and col < num_cols and M[row][col] == 1

        def dfs(row, col, offset, cur_len=0):
            cur_len = 0
            while is_valid(row, col):
                cur_len += 1
                row = row + offset[0]
                col = col + offset[1]
            return cur_len

        #             cur_len += 1

        #             return cur_len + dfs(row + offset[0], col + offset[1], offset)
        max_len = 0
        for row in range(len(M)):
            for col in range(len(M[0])):
                for offset in offsets:
                    max_len = max(dfs(row, col, offset), max_len)
                    if max_len >= max(num_rows, num_cols):
                        return max_len
                        # can't get better than this
        return max_len
