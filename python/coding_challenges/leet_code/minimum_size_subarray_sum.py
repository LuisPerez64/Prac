"""
REVISIT: Do a few live examples to get through the logic relayed here regarding the running sum.
Question: https://leetcode.com/problems/minimum-size-subarray-sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # return self.second_implementation(s, nums)
        return self.first_implementation(s, nums)

    def first_implementation(self, s: int, nums: List[int]) -> int:
        """
        Simple two loop implementation.
        Time Complexity: O(n**2)
        """
        inf = float('inf')
        min_sub_len = inf

        for left in range(len(nums)):
            cur_sum = 0
            for right in range(left, len(nums)):
                cur_sum += nums[right]
                if cur_sum >= s:
                    min_sub_len = min(min_sub_len, right - left + 1)
                    break
                if right - left + 1 > min_sub_len:
                    # won't do better than the current best. break out.
                    break

        return 0 if min_sub_len == inf else min_sub_len

    def second_implementation(self, s: int, nums: List[int]) -> int:
        """
        Pulled Algo:
        Initialize left pointer to 0 and sum to 0
        Iterate over the \text{nums}nums:
        Add nums[i] to sum
        While sum is greater than or equal to s:
        Update ans=min(ans,i+1−left), where i+1−left is the size of current subarray
        It means that the first index can safely be incremented, since,
         the minimum subarray starting with this index with sum ≥ s has been achieved
        Subtract nums[left] from  sum and increment left
        Time Complexity: O(2n)
            Iteration over the full array and the secondary counter with the left pointer.
        """
        left = 0
        tally = 0
        min_sub = float('inf')
        for idx in range(len(nums)):
            # Add to the running sum from this index >
            tally += nums[idx]
            # When we get to an index that produces a sum >= the value we're seeking we backtrack to find the point
            # where this condition could have been met. removing values from the left of the array until the sum is
            # no longer past the max val given.
            while tally >= s:
                min_sub = min(min_sub, idx + 1 - left)
                # Decrement the current tally to be able to break out of this loop.
                tally -= nums[left]
                left += 1
        return min_sub if min_sub != float('inf') else 0

# every value
# print(Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]))
# print(Solution().minSubArrayLen(s=15, nums=[1, 2, 3, 4, 5]))
