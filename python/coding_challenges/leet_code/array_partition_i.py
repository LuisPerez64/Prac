"""
Question: https://leetcode.com/problems/array-partition-i

Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Sort the input to get the results in a patterned order.
        After sorting the min value in a 2n array would be the first in every pair.
        0, 2,... until the last is met. This is done through some list comprehension
        arr[::2] => from start to end of the array incrementing index by 2
        Time Complexity: O(n log n) + O(n/2) => O(n log n)
        Space Complexity: O(1)
        """
        return sum(sorted(nums)[::2])
