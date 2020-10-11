"""
REVISIT: The context of the prefix sum and its application to problems like this is massive.
Question: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        return self.second_implementation(nums, k)

    def first_implementation(self, nums: List[int], k: int) -> int:
        """
        Brute force it to at least get the problem resolved.
        Time complexity: O(n**2)
        """
        max_len = 0
        for idx_a in range(len(nums)):
            cur_sum = 0
            cur_len = 0
            for idx_b in range(idx_a, len(nums)):
                cur_sum += nums[idx_b]
                if cur_sum == k:
                    cur_len = idx_b - idx_a
            max_len = max(cur_len + 1, max_len)

        return max_len

    def second_implementation(self, nums: List[int], k: int) -> int:
        """
        Prefix sum method. Read up on it more, the idea came but couldn't implement in full.
        Find the running sum of the nums list, and at every instance its either 0
        In base []
        or the target mark it. Place them into a hashmap for easy retrieval.
            Key: Index
            Val: Sum at index

        We hold a "ghost" 0 index in the compliments to denote that if the value is ever 0
        we can assume that the maximum length should take the start of the whole array into account.
        since from idx "0" to 2 (in a non zero indexed format) the total sum of all the elements before is 0.

        Example: input: [1,-1,5,-2,3], prefix_sum: [1,0,5,3,6], compliments: {0: 0, 1: 0, 5: 2, -2: 3, 3:4 }
        # -1 is already captured as its looped back to 0.

        """
        prefix_sum = [0]
        compliments = {0: 0}
        cur_sum = 0
        max_len = 0

        for num in nums:
            # populate the prefix sum array
            cur_sum += num
            prefix_sum.append(cur_sum)

        # skip the 0th index from the prefix sums padding.
        for idx in range(1, len(nums) + 1):
            # get the value that would be needed from the current index in the prefix_sum to get
            # to value K
            comp = prefix_sum[idx] - k
            if comp in compliments:
                # Get the first location of that compliment and the current location in the nums array
                # Example run will be added to the docstring
                max_len = max(max_len, idx - compliments[comp])

            if prefix_sum[idx] not in compliments:
                # Add the current prefix sum into the compliments for future passthroughts
                # This ensures that we don't overwrite the first instance of a value appearing
                #
                compliments[prefix_sum[idx]] = idx

        return max_len
