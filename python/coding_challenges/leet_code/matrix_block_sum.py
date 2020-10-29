"""
Question: https://leetcode.com/problems/matrix-block-sum/
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j]
is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K,
and (r, c) is a valid position in the matrix.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        return self.second(mat, K)

    def first(self, mat, K):
        answer = [[0] * len(mat[0]) for _ in range(len(mat))]

        def is_valid(i, j, r, c, K):
            return i - K <= r <= i + K and j - K <= c <= j + K

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for r in range(len(mat)):
                    for c in range(len(mat[0])):
                        if not is_valid(i, j, r, c, K):
                            continue
                        answer[i][j] += mat[r][c]
        return answer

    def second(self, mat, K):
        """
        Annotate this. It's an odd enough concept but with visual aids its straight forward.
        Credits to: Leet Code Solution http://tiny.cc/rtv0tz

        """
        answer = [[0] * len(mat[0]) for _ in range(len(mat))]
        prefix = [[0] * len(mat[0]) for _ in range(len(mat))]

        # make a prefix matrix for the rows and the columns independent of any other row.
        for r in range(len(mat)):
            # pre populate the values in the 0th index for the prefix matrix.
            prefix[r][0] = mat[r][0]
            for c in range(1, len(mat[0])):
                # Just sum up all of the elements in each row.
                prefix[r][c] = prefix[r][c - 1] + mat[r][c]

        # do the same for the columns
        for r in range(1, len(mat)):
            for c in range(len(mat[0])):
                prefix[r][c] = prefix[r - 1][c] + prefix[r][c]

        for r in range(len(mat)):
            ru = max(r - K, 0)
            rd = min(r + K, len(mat) - 1)

            for c in range(len(mat[0])):
                cl = max(0, c - K)
                cr = min(len(mat[0]) - 1, c + K)

                value = prefix[rd][cr]

                if ru - 1 >= 0:
                    value -= prefix[ru - 1][cr]
                if cl - 1 >= 0:
                    value -= prefix[rd][cl - 1]
                if ru - 1 >= 0 and cl - 1 >= 0:
                    value += prefix[ru - 1][cl - 1]
                answer[r][c] = value
        return answer
