"""
REVISIT: Annotate and find the proper pattern from the pulled solution.
Question: https://leetcode.com/problems/count-submatrices-with-all-ones/

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.



Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5


Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""
from typing import List, Any


def print_matrix(inp_matrix: List[List[Any]]):
    print()
    for row in inp_matrix:
        print(row)
    print()

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        return self.pulled_implementation(mat)

    def first_implementation(self, mat: List[List[int]]) -> int:
        """
        Submatrix is defined as any combination that produces a rectangle
        [1], [[1], [1]], [1,1,1], ...
        """
        if not len(mat) or not len(mat[0]):
            return 0
        num_rows = len(mat)
        num_cols = len(mat[0])
        count = 0
        marker = float('-inf')
        if mat[0][0] == 1:
            count += 1

        # print_matrix(mat)
        for row in range(num_rows):
            for col in range(1, num_cols):
                if mat[row][col] >= 1:
                    # Accumulate the columns values
                    mat[row][col] += mat[row][col - 1]
        # print_matrix(mat)
        for col in range(num_cols):
            prev_val = 0
            for row in range(1, num_rows):

                if mat[row][col] >= 1:
                    inc = 0
                    if col >= 1:
                        inc = 1 if mat[row][col-1] else 0
                    # Take into account the values that are 1 before the
                    mat[row][col] += min(mat[row][col] +1 , mat[row-1][col])
        # print_matrix(mat)
        return sum(sum(mat[x]) for x in range(num_rows))

    def pulled_implementation(self, mat: List[List[int]]) -> int:
        if not mat:return 0
        m,n = len(mat),len(mat[0])
        res = 0
        #RLE - Run length encoding
        for i in range(m):
            for j in range(n):
                if  j:
                    if mat[i][j]:
                        mat[i][j] = mat[i][j-1] + 1

        #Now,calculate all the rectangular submatrices from the RLE
        for i in range(m):
            for j in range(n):
                # (i,j) :top right of matrix
                ans = mat[i][j]
                for k in range(i,m):#bottom-right
                    ans = min(ans,mat[k][j])
                    res+= ans

        return res

"""
Test Cases:

[[1,0,1],[1,1,0],[1,1,0]]
[[0,1,1,0],[0,1,1,1],[1,1,1,0]]
[[1,1,1,1,0],[1,0,0,1,0],[0,0,1,0,1],[0,1,0,0,0]]
"""