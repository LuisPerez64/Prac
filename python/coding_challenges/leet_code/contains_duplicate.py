"""
Question: https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
 and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> bool:
        """
        Sorting Algorithm: Heap Sort
          Time Complexity: O(n * log(n))
          Space Complexity: O(1)

        Time Complexity: O(nlog(n)) + O(n)
        Space Complexity: O(1)
        """

        from heapq import heappop, heapify
        heapify(nums)
        last_num = heappop(nums)
        while len(nums):
            cur_num = heappop(nums)
            if last_num == cur_num:
                return True
            last_num = cur_num
        return False


    def second_implementation(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dup_set = set()
        for x in nums:
            if x in dup_set:
                return True
            dup_set.add(x)
        return False