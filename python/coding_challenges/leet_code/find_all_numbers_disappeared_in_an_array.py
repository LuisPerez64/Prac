"""
Question: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            offset = abs(nums[x]) - 1
            if nums[offset] > 0:
                nums[offset] *= -1
        res = []
        for idx in range(len(nums)):
            if nums[idx] > 0:
                res.append(idx + 1)

        return res
