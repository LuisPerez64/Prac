"""
Question: https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.first_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Hold three counters.
        Min value, Max Value, Result.
        The min is held because negative * negative could yield a high
        max is the running max.
        result is the global max.
        Initialize the three candidates at the same val. nums[0]
        iterate over the array from index 1+
        establishing the min/max based on  these combinations (max_val * cur_num, min_va * cur_num, cur_num)
        pulling the min/max from calling the appropriate functions
        The result is then the global maximum calculated by comparing current max and recorded max
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0

        # initialize the candidates to all have the same shot.
        max_val = nums[0]
        min_val = nums[0]
        result = nums[0]
        for num in nums[1:]:
            # Calculate both max,min within the context of their previous value, else a temp max value would need to be logged.
            max_val, min_val = max(max_val * num, num, min_val * num), min(max_val * num, num, min_val * num)
            # Get the global maximum.
            result = max(max_val, result)
        return result

    def second_implementation(self, nums: List[int]) -> int:
        """
        Naive solution:
        Time Complexity: O(n ^ 2)
        """
        pass
