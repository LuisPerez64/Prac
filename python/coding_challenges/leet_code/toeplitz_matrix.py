"""
Question: https://leetcode.com/problems/toeplitz-matrix/
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

"""
from collections import defaultdict
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return self.first(matrix)

    def first(self, matrix: List[List[int]]) -> bool:
        """
        Get if the current value is a toeplitz by storing the children values in a set.
        Grabbing the possible firsts from the top row, and first columns.
        """
        # base_dict will hold a field denoting the first element in each possible diagonal.
        # {(0,0): A, (0,1): B, ..., (1,0): Q, (2, 0): P, ...}
        base_dict = defaultdict(int)

        # get the rows.
        for c in range(len(matrix[0])):
            base_dict[(0, c)] = matrix[0][c]

        for r in range(1, len(matrix)):
            base_dict[(r, 0)]= matrix[r][0]

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                # Get the base from the smallest value in the r/c pair subtracted from the current location.
                sub = min(r, c)
                cur = matrix[r][c]
                if cur != base_dict[(r-sub, c-sub)]:
                    return False

        return True