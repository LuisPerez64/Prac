"""

"""
from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.second_implementation(matrix, target)

    def first_implementation(self, matrix, target):
        """
        The matrix is sorted at each row, and along each column
        Checking to see if an element is within the bounds of either edge at each step
        if indices are [0][0] check if any elements on the edges encompass this number.
        If neither satisfy the condition that the number is within the start/end bound increment both indices
        else increment the index that does not contain the value.
        """
        if not matrix or not matrix[0]:
            return False
        idx_a = idx_b = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        while idx_a < num_rows or idx_b < num_cols:
            # check if the element exists within the current row.

            if matrix[idx_a][idx_b] >= target:
                # its within the starting bound at the current segment of the matrix
                # Check if the row contains it
                if matrix[idx_a][-1] > target and idx_a < num_rows:
                    # its outside this rows bound
                    idx_a += 1
                if matrix[-1][idx_b] > target and idx_b < num_cols:
                    idx_b += 1
                if matrix[idx_a][idx_b] == target:
                    return True
            elif idx_a < num_rows and idx_b < num_cols:
                idx_a += 1
                idx_b += 1
        return False

    def second_implementation(self, matrix: List[List[int]], target: int) -> bool:
        """
        In all this is a Binary search applicable problem.
        Pattern:
            From a given point check if the last idx element for the row and column are in the bound.
            Increasing the row/col if the value is above the two bounds.
        """
        num_rows = len(matrix)
        if not num_rows or not len(matrix[0]):
            return False
        num_cols = len(matrix[0])
        # Handle the base case that the index is past the largest or less than the smallest element.
        if target > matrix[num_rows - 1][num_cols - 1] or target < matrix[0][0]:
            return False

        def is_valid(row, col):
            # Keep from going out of bounds.
            return row >= 0 and col >= 0 and row < num_rows and col < num_cols

        def find_next_index(row, col):
            if not is_valid(row, col):
                return False
            # Cases
            cur_val = matrix[row][col]
            # Found the target. Return true
            if cur_val == target:
                return True

            # At end of the matrix and target > than it. Return false
            if row == num_rows - 1 and col == num_cols - 1:
                return False

            # The Target is larger than the two current bounds.
            if target > matrix[row][num_cols - 1] and target > matrix[num_rows - 1][col]:
                # Check if the next segment has it.
                return find_next_index(row + 1, col + 1)
            elif target <= matrix[row][num_cols - 1]:
                # Value in this row
                return find_next_index(row, col + 1)
            elif target <= matrix[num_rows - 1][col]:
                # Value not in this column
                return find_next_index(row + 1, col )
            else:
                return False

        return find_next_index(0, 0)

# Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
# Solution().searchMatrix([[1,3]], 3)