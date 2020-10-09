"""
Question: https://leetcode.com/problems/largest-number-at-least-twice-of-others/
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Can be calculated easily by sorting the array,  and finding the largest value in it
        then comparing that value against every other element in the original array.
        but the sort would increase the time complexity to O(n log n) at best.
        Iterating over the array with two pointers and at each instance checking if the current value is bigger than
        these two pointers.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0

        idx_a = 0
        idx_b = 1
        num_a = nums[0]
        num_b = nums[1]

        for idx, val in enumerate(nums[2:], 2):
            if val > num_a or val > num_b:
                if num_a > num_b:
                    # replace num_b
                    num_b = val
                    idx_b = idx
                else:
                    num_a = val
                    idx_a = idx

        if num_a > num_b and num_a >= 2 * num_b:
            return idx_a
        if num_b > num_a and num_b >= 2 * num_a:
            return idx_b
        return -1

    def second_implementation(self, nums: List[int]) -> int:
        """
        Array sort and eliminate the need to do the max calculation if invalid.
        Time Complexity: O(n log n) + O(n) => O(n log n)
            Sorting algo: O(n log n)
            Iterate algo: O(n) -- done only if array is valid.
        Space Complexity: O(n)
            Need to create a copy for the sorted array
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        sorted_nums = sorted(nums)
        max_val = sorted_nums[-1]
        next_largest = sorted_nums[-2]
        if max_val < 2 * next_largest:
            return -1

        # Using built in index function which is O(n) same as enumerate iteration.
        return nums.index(max_val)
        # # else iterate over the array and find the index of the max_val
        # for idx, val in enumerate(nums):
        #     if val == max_val:
        #         return idx

Solution().dominantIndex([0, 0, 0, 1])
