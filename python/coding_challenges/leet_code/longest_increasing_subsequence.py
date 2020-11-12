"""
REVISIT: All three implementations need a revisit but mainly the last two.
    First implementation is too inefficient and should always try to avoid recursive solutions when possible

Question: https://leetcode.com/problems/longest-increasing-subsequence/submissions/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.third_implementation(nums)
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Brute force recursive solution. Finding the elements based off of either taking the starting point or
        leaving it. Comparing the result of the two operations and grabbing the max length of the list
        Time Complexity: O(2**n)
        Space Complexity: O(2n)
            The recursion call stack houses itself in memory and will need to branch out on every element with
            the taken/not_taken logic
        """
        if len(nums) <= 1:
            return len(nums)
        from functools import lru_cache
        memo = {}

        @lru_cache(maxsize=None)
        def find_max_length(prev, cur_pos):
            if (prev, cur_pos) in memo:
                return memo.get((prev, cur_pos))
            if cur_pos == len(nums):
                return 0
            taken = 0
            if nums[cur_pos] > prev:
                # Ingest the DP list with the assumption that we're taking the current node as a start point
                taken = 1 + find_max_length(nums[cur_pos], cur_pos + 1)
            # Get the length if the value before was used
            not_taken = find_max_length(prev, cur_pos + 1)
            cur_max = max(taken, not_taken)
            memo[(prev, cur_pos)] = cur_max
            return cur_max

        return find_max_length(float('-inf'), 0)

    def second_implementation(self, nums: List[int]) -> int:
        """
        Dynamic programming approach.

        Store the result of the calculations so far into the DP array based off of the index of the starting element.
        Eliminate the need to recalculate the value from the known indices
        Time Complexity: O(n ^ 2)
        Space Complexit: O(n)
            Space for the DP Array
        """
        if len(nums) <= 1:
            return len(nums)

        dp = [0 for _ in range(len(nums))]
        max_len = 1
        dp[0] = 1

        for idx_a in range(1, len(nums)):
            # Calculate the max length of the array possible from start to idx_a sliced
            local_max = 0
            for idx_b in range(0, idx_a):
                # Get all of the values that are smaller than the element at the end of the current slice.
                if nums[idx_a] > nums[idx_b]:
                    # If current element is smaller than the max check to see if the current subsequence is
                    # larger than a subsequence without it included.
                    local_max = max(local_max, dp[idx_b])
            # Increment the local_max by 1 to ingest the end element capturing the longest chain possible until idx_a
            # Updating the max_len variable to not run the max function on the dp array at the end
            dp[idx_a] = local_max + 1
            max_len = max(max_len, dp[idx_a])
        return max_len

    def third_implementation(self, nums: List[int]) -> int:
        """
        Dynamic programming approach with binary search

        Assumption made that the bisect(binary search) operation in python runs in O(log n) time
        Time Complexity: O(n log n)
            Iterates over the list O(n) * binary search operation O(log n)
        Space Complexity: O(n)
            dp array of size n
        """
        from bisect import bisect_left

        dp = [0 for _ in range(len(nums))]
        max_len = 0
        for num in nums:
            # Find the best place to place the current number based on the bisect operation.
            # The max len value dictates the last possible insert location.
            # As the values continue increasing we continue appending them
            # as the location they belong in is the end of the list.
            insert_idx = bisect_left(dp, num, 0, max_len)

            # Insert num into the position it would be occur in the subsequence list
            # As we move through the list of inputs it could overwrite an element,
            # but that elements max subsequence is preserved
            dp[insert_idx] = num
            if insert_idx == max_len:
                max_len += 1
        return max_len


Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
