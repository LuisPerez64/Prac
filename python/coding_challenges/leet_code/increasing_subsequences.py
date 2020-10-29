"""
REVISIT: The set theory and use of tuples to not have to do the copies is an odd trick
Question: https://leetcode.com/problems/increasing-subsequences/
Given an integer array, your task is to find all the different possible increasing subsequences
of the given array, and the length of an increasing subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]


Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also
be considered as a special case of increasing sequence.
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int]) -> List[List[int]]:
        """
        Capture the subsequences in a list. Iterate over that list with all of the
        new sequences. Each time an item is brought in the sequence is inserted
        """

        results = {()}

        for num in nums:
            copy = {(), (num,)}
            for cur in results:
                if cur and cur[-1] <= num:
                    copy |= {cur + (num,)}
            results |= copy

        return [list(x) for x in results if len(x) >= 2]
