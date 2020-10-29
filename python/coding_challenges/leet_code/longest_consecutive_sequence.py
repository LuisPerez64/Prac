"""
Question: https://leetcode.com/problems/longest-consecutive-sequence/submissions/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.first_implementation(nums)

    def first_implementation(self, nums):
        """
        Using the hashset to mark all of the existing elements from the array.
        After the set is constructed it comes down to ensuring that for any element in the array
        there exists an element+1 and so forth.
        Using memoization to not redo the work for known indices.
        Time Complexity: O(n)
            O(n) average case due to the memoization,
            worst case O(n ^ 2) for a reversed list
        Space Complexity: O(2n) => O(n)
            creating the memoization table, and the set operation
        """

        # Create the set, as the order of the array elements won't matter
        exists = set([x for x in nums])
        longest_seq = 0
        memo = {}

        for num in nums:
            cur_long = 1
            cur = num + 1
            while cur in exists:
                if cur in memo:
                    cur_long += memo[cur]
                    break
                cur_long += 1
                cur += 1
            memo[num] = cur_long
            longest_seq = max(longest_seq, cur_long)

        return longest_seq
