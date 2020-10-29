"""
REVISIT: Matrix manipulation as a whole is a topic that needs more time invested into it.
Question: https://leetcode.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order
as shown in the below image.
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.first_implementation(matrix)

    def first_implementation(self, matrix: List[List[int]]) -> List[int]:
        """
        Iterate over the edges of the matrix gathering the diagonal positions from the instances where the row is 0
        or the col is the last column available.
        Using a single function to get the diagonal from any given start point and reversing the list it produces if
        the current start index is odd (pattern is diag up, diag down, on repeat)
        Time Complexity: O(m*n) all of the cells are visited once.
        Space Complexity: O(min(m,n)) + O(1)
            There's a temporary array used to house the temporary diagonal array and it will not be longer than the
            shortest side of the input matrix.
            O(1) for space needed to house the output which is not counted else O(m*n)
        """
        if not matrix or not matrix[0]:
            return []

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        order_diag = [matrix[0][0]]

        def get_diagonal(start_row, start_col):
            """
            Diagonal is defined as matrix[m][n] -> matrix[m+1][n-1] until either m == num_rows -1 or n == 1
            from any start point in the matrix.
            """
            cur_diag = []
            while start_row < num_rows and start_col >= 0:
                cur_diag.append(matrix[start_row][start_col])
                start_row += 1
                start_col -= 1
            return cur_diag

        # At every boundary capture the diagonal possible from that start point. We're doing the same operation in
        # but in reverse when getting the diagonal up so use the same function and reverse its value based on
        # the pattern. Diag up if % 2 == 0 else reverse the output list.
        for cur_col in range(1, num_cols):
            diag = get_diagonal(0, cur_col)
            if cur_col % 2 == 0:
                # handle case for diagonal down (odd numbered start)
                diag = diag[::-1]
            order_diag.extend(diag)

        for cur_row in range(1, num_rows):
            # Exhausting the possible diagonals from the last col of the matrix
            diag = get_diagonal(cur_row, num_cols - 1)
            # Depending on the dimensions of the array the inversion along the cols is reversed.
            if cur_row % 2 != 0 + num_cols % 2:
                diag = diag[::-1]
            order_diag.extend(diag)

        return order_diag

    def second_implementation(self, matrix: List[List[int]]) -> List[int]:
        """
        DOES NOT WORK.
        Iteration over the elements in the matrix to generate a diagonal order
        Steps:
        while cur_row < max_rows or cur_col < max_cols
            Get element at matrix[row][col]
            Decrease row by 1 incremenet col by 1
                At the first index this will be skipped as its out of bounds.
            Increment the column index by 1
            Increment the row index by 1
            increment the row index by 1
            increment the origins x,y indices by 1
        repeat until exhausted.
        Pattern does not work for non mxm matrices...
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        # Do all of these from the cleared state of the cur_cell value.
        # start point is (0,0)
        if num_cols == num_rows:
            # increments for an mxm matrix
            increments = [(-1, 1), (0, 1), (1, 0), (2, 0)]
        elif num_rows > num_cols:
            # increments for lopsided matrices.
            increments = [(-1, 1), (0, 1), (1, 0), (2, 0)]
            pass
        else:
            pass
        diag_order = []

        def get_element(cur_cell: tuple, next_cell: tuple):
            next_index = (cur_cell[0] + next_cell[0], cur_cell[1] + next_cell[1])
            if next_index[0] >= num_rows or next_index[0] < 0 or next_index[1] >= num_cols or next_index[1] < 0:
                return
            diag_order.append(matrix[next_index[0]][next_index[1]])
            return next_index

        cur_cell = (0, 0)
        while cur_cell[0] < num_rows or cur_cell[1] < num_cols:
            if cur_cell[0] < num_rows and cur_cell[1] < num_cols:
                # base case the current index is within range of the matrix
                diag_order.append(matrix[cur_cell[0]][cur_cell[1]])
            elif cur_cell[0] < num_rows:
                # m x n array with more rows than columns. i.e. [[0],[1],[2],[3]]
                diag_order.append(matrix[cur_cell[0]][cur_cell[1] - 1])
            elif cur_cell[1] < num_cols:
                # mxn array with more columns than rows i.e. [[0,1,2,3,4,5]]
                diag_order.append(matrix[cur_cell[0] - 1][cur_cell[1]])
            for inc in increments:
                get_element(cur_cell, inc)
            cur_cell = (min(num_rows, cur_cell[0] + 1), min(num_cols, cur_cell[1] + 1))

        return diag_order


print(Solution().findDiagonalOrder(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
print(Solution().findDiagonalOrder(
    [[1, 2],
     [3, 4],
     [5, 6]]
))
print(Solution().findDiagonalOrder(
    [[2, 5], [8, 4], [0, 1], [7, 9]]
))
