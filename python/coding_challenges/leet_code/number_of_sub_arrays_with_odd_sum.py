"""
REVISIT: DP solution with and without the DP array.
Question: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
Given an array of integers arr. Return the number of sub-arrays with odd sum.

As the answer may grow large, the answer must be computed modulo 10^9 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All sub-arrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All sub-arrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
Example 4:

Input: arr = [100,100,99,99]
Output: 4
Example 5:

Input: arr = [7]
Output: 1


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 100
"""
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        return self.second(arr)

    def first(self, arr: List[int]) -> int:
        """
        Anotate this.
        TC: O(n)
        SC: O(n)
        """
        mod = 10 ** 9 + 7

        dp = [[0, 0] for _ in range(len(arr))]

        if arr[-1] % 2 == 1:
            dp[-1] = [0, 1]
        else:
            dp[-1] = [1, 0]
        end_sum = dp[-1][1]

        for idx in range(len(arr) - 2, -1, -1):
            # distinguish if we're adding to the 0's or 1's arr.
            dp_idx = arr[idx] % 2
            # We're updating either the 0's or 1's indices with the added sum of the zero's arrays.
            dp[idx][dp_idx] = (1 + dp[idx + 1][0]) % mod
            # The counter sum is added in for the previous idx at the ones place.
            dp[idx][not dp_idx] = dp[idx + 1][1]

            end_sum += dp[idx][1]

        return end_sum % mod

    def second(self, arr: List[int]) -> int:
        """
        Anotate this.
        TC: O(n)
        SC: O(1)
        """
        mod = 10 ** 9 + 7

        zero = 0
        one = 0

        if arr[-1] % 2 == 1:
            one = 1
        else:
            zero = 1
        end_sum = one

        for idx in range(len(arr) - 2, -1, -1):
            tmp = one
            add_in = (1 + zero) % mod
            # distinguish if incrementing the zeros or ones values.
            if arr[idx] % 2:
                # add in an odd value.
                one = add_in
                zero = tmp
            else:
                zero = add_in
                one = tmp
            end_sum += one

        return end_sum % mod
