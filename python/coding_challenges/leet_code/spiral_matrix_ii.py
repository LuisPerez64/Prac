"""
Question: https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return self.first_implementation(n)

    def first_implementation(self, n: int) -> List[List[int]]:
        """
        Problems are creating the matrix and iterating over it in the format that the spiral matrix algo does.
        Maintaining a counter and placing that value into the matrix at [row][col]
        """
        matrix = [[-1] * n for _ in range(n)]
        num_rows = num_cols = n
        cur_row = cur_col = 0
        # pattern is move right, down, left, up
        increments = [
            ((0, 1), (1, -1)),
            ((1, 0), (-1, -1)),
            ((0, -1), (-1, 1)),
            ((-1, 0), (1, 1))]

        def is_valid(c_row, c_col):
            return c_row >= 0 and c_row < num_rows and c_col >= 0 and c_col < num_cols and matrix[c_row][c_col] == -1

        def traverse(c_row, c_col, increment, fix, start_val):
            while is_valid(c_row, c_col):
                matrix[c_row][c_col] = start_val
                start_val += 1
                c_row += increment[0]
                c_col += increment[1]
            return c_row + fix[0], c_col + fix[1], start_val

        val = 1
        while val <= n * n:
            for shift, fix in increments:
                cur_row, cur_col, val = traverse(cur_row, cur_col, increment=shift, fix=fix, start_val=val)
        return matrix
