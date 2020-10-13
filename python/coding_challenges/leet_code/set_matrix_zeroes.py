"""
Question: https://leetcode.com/problems/set-matrix-zeroes/
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
Input: matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
Output: [
    [1,0,1],
    [0,0,0],
    [1,0,1]
]
Example 2:


Input: matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
Output: [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.first_implementation(matrix)

    def first_implementation(self, matrix: List[List[int]]) -> None:
        """
        Find the indices where the grid is 0.
        Mark them initially to not mistakenly overreach.
        Once that's captured iterate over the matrix and if the item at
        that row or column is in the set then mark it.
        Time Complexity: O(2 (m * n)) => O(mn)
            Iterate over the matrix twice.
        Space Complexity: O(m + n)
            The max size of the sets for rows and cols tracking.
        """
        # memo = {
        #     'rows': set(), 'cols': set()
        # }
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        rows = set()
        cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rows or col in cols:
                    matrix[row][col] = 0

    def pulled_implementation(self, matrix: List[List[int]]) -> None:
        """
        Pulled this implementation from leetcode solution.
        https://leetcode.com/problems/set-matrix-zeroes/solution/
        Algorithm 2
        Time Complexity: O(mn)
        Space Complexity: O(1)
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if is_col:
            for i in range(R):
                matrix[i][0] = 0