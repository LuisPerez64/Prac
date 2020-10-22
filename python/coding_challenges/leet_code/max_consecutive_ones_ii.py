"""
Question: https://leetcode.com/problems/max-consecutive-ones-ii/
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream?
    In other words, you can't store all numbers coming from the stream as it's too large to hold in memory.
    Could you solve it efficiently?
"""
from collections import defaultdict
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int], max_swap: int = 1) -> int:
        """
        Allow for this to be extensible and use the frequency calculation, with a max swap of 1
        values.

        """
        frequency = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            frequency[nums[right]] += 1
            window = right - left + 1

            # calculate the amount of 0's in the window and if possible to supplant them with a 1 do so.
            if window - frequency[1] <= max_swap:
                # we can swap within this threshold.
                max_len = max(max_len, window)
            else:
                # slide the whole window over and decrease the frequency of the leftmost element.
                frequency[nums[left]] -= 1
                left += 1

        return max_len
