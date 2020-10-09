"""
Question: https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.first_implementation(matrix)

    def first_implementation(self, matrix: List[List[int]]) -> List[int]:
        """
        The spiral algo for the matrix is going to run through the patterns
            1) Move right until a bound is met
            2) Move down until a bound is met
            3) Mover right until a bound is met
            4) Move up until a bound is met
            5) repeat.
        the bound is defined as either the next index that will yield an out of bounds error
        or the next cell has been visited already.
        Maintaining the current location that the cell is at at the end of the traversal and using that as the
        basis for the next segments start point.
        The "fix" increment is in place to correct the bounds and move the next operation into the proper start point.
        i.e. if at the lower right of the matrix ([m][n]) that operation has been registered already so next is
        m-1, n-1 and we then keep moving right along the current row.
        """

        if len(matrix) == 0:
            return []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        cur_row = 0
        cur_col = 0
        spiral_order = []

        def valid_move(next_row, next_col):
            if next_col < num_cols and next_col >= 0 and next_row < num_rows and next_row >= 0 and type(
                    matrix[next_row][next_col]) is int:
                return True
            return False

        def traverse(start_row, start_col, increment, fix_idx, op):
            # print(start_row, start_col, increment, fix_idx, op)
            cur_trip = []
            while valid_move(start_row, start_col):
                cur_val = matrix[start_row][start_col]
                cur_trip.append(cur_val)
                matrix[start_row][start_col] = str(cur_val)
                start_row += increment[0]
                start_col += increment[1]
            spiral_order.extend(cur_trip)
            return start_row + fix_idx[0], start_col + fix_idx[1]

        # Tme increments and fixes needed at each stage of the spiralling.
        increments = [
            ((0, 1), (1, -1), 'right'),
            ((1, 0), (-1, -1), 'down'),
            ((0, -1), (-1, 1), 'left'),
            ((-1, 0), (1, 1), 'up')
        ]
        while len(spiral_order) < num_rows * num_cols:
            for shift, fix, direction in increments:
                cur_row, cur_col = traverse(cur_row, cur_col, increment=shift, fix_idx=fix, op=direction)
        return spiral_order

    def second_implementation(self, matrix: List[List[int]]) -> List[int]:
        """
        Non working solution to this problem that i'd worked on before.
        """
        if len(matrix) <= 1:
            return matrix[0]
        fin_x_index = len(matrix[0])
        fin_y_index = len(matrix)
        ini_x_index = 0
        ini_y_index = 0
        total_items = fin_x_index * fin_y_index
        ret_list = []

        def iter_x_helper(start, end, ini_y, step):
            t_list = []
            for idx in range(start, end, step):
                t_list.append(matrix[ini_y][idx])
            return t_list

        def iter_y_helper(start, end, ini_x, step):
            t_list = []
            for idx in range(start, end, step):
                t_list.append(matrix[idx][ini_x])
            return t_list

            # Cond L->R Y stays the same X increases until it reaches Fin X
            # Cond R->L Y Stays Same X Decreases until it reaches Init X
            # Cond T->B X Stays The Same Y Increases until it reaches Fin Y
            # Cond B->T X Stays The Same Y Decreases until it reaches Ini Y

        while ini_y_index * ini_x_index < total_items:
            ret_list.extend(iter_x_helper(ini_x_index, fin_x_index, ini_y_index, 1))
            ret_list.extend(iter_y_helper(ini_y_index + 1, fin_y_index, fin_x_index - 1, 1))
            ret_list.extend(iter_x_helper(fin_x_index - 1, ini_x_index, fin_y_index - 1, -1))
            ret_list.extend(iter_y_helper(fin_y_index - 1, ini_y_index + 1, ini_x_index, -1))
            ini_x_index += 1
            ini_y_index += 1
            fin_x_index -= 1
            fin_y_index -= 1

        return ret_list


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
