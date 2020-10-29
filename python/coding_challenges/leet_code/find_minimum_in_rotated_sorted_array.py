"""
Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        """
        Initial approach iterate over the array, and at the point where arr[n-1] > arr[n] you've found the min
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Handle base cases.
        if not nums:
            raise Exception("No base case for empty array.")
        if len(nums) == 1:
            return nums[0]
        if nums[-1] >= nums[0]:
            # Array is fully sorted.
            return nums[0]

        # initialize the max val and result as 0th element.
        # for the case where nums is fully sorted the value will keep increasing. and result will not change.
        max_val = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num >= max_val:
                max_val = num
            else:
                result = num
                break
        return result

    def second_implementation(self, nums: List[int]) -> int:
        """
        Finding the pivot index through binary search.
        In full we've got two sorted arrays in the worst case and one sorted array in the best case.
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Handle base cases.
        if not nums:
            raise Exception("No base case for empty array.")
        if len(nums) == 1:
            return nums[0]
        if nums[-1] >= nums[0]:
            # Array is fully sorted.
            return nums[0]

        def find_pivot():
            """
            Find the location at which nums[n-1] > nums[n]
            This is doable through a modified binary search operation.
            """
            start_idx = 0
            end_idx = len(nums) - 1
            target = nums[0]
            while start_idx <= end_idx:
                mid_point = (start_idx + end_idx) // 2
                # Find the location at which nums[idx-1] > target and nums[idx-1] > nums[idx]
                if nums[mid_point - 1] >= target and nums[mid_point - 1] > nums[mid_point]:
                    return nums[mid_point]
                elif nums[mid_point] >= target:
                    # Still increasing so start from here next round
                    start_idx = mid_point + 1
                else:
                    # Went too far forward.
                    end_idx = mid_point
            return nums[0]

        # The array is pivoted. Find the first instance satisfying nums[idx-1] > nums[idx]
        return find_pivot()

# print(Solution().second_implementation([10,1,10,10,10]))
