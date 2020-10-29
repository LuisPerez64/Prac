"""
Question: https://leetcode.com/problems/add-to-array-form-of-integer/
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        """

        """
        if len(A) == 0 or K == 0:
            return A
        # Remove iterations over K from the list.
        neg_idx = -1
        while K:
            K, n = divmod(K, 10)
            if len(A) < abs(neg_idx):
                A.insert(0, 0)
            A[neg_idx] += n
            neg_idx -= 1

        carry = 0
        for idx in range(len(A) - 1, -1, -1):
            if carry:
                A[idx] += carry
                carry = 0
            if A[idx] >= 10:
                carry, A[idx] = divmod(A[idx], 10)
        if carry:
            A.insert(0, carry)
        return A
