"""
REVISIT: Annotate this problem. It's not difficult just easy to trip over in an interview
Question: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same,
or all the values in B are the same.

If it cannot be done, return -1.

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every
value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6

"""
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        Want to reach an array with all of the values on one row being equivalent
        """

        def rotate(base):
            rotations = [0, 0]
            for idx in range(len(A)):
                if A[idx] != base and B[idx] != base:
                    return -1
                if A[idx] != base:
                    rotations[0] += 1
                elif B[idx] != base:
                    rotations[1] += 1
            return min(rotations)

        tmp = rotate(A[0])

        if tmp >= 0 or A[0] == B[0]:
            return tmp
        return rotate(B[0])
