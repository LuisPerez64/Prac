"""
Question: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.first_implementation(nums, target)

    def first_implementation(self, nums: List[int], target: int) -> int:
        """
        The array would basically become two sorted arrays and the first step in finding the element
        would be finding section at which the array has an element less than the first element in it.
        Using Binary search to find the first instance where element at n+1 < n
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # Find the first index satisfying the pivot condition arr[n+1] < arr[n].
        def find_pivot(left, right):
            # Check to see if the array is sorted on init
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid_point = (left + right) // 2
                if nums[mid_point] == target:
                    return mid_point
                # Find the index where the array is first seen to be out of order.
                if nums[mid_point] > nums[mid_point + 1]:
                    return mid_point + 1
                else:
                    # Find the new indices for the operation with binary slicing
                    if nums[mid_point] < nums[left]:
                        right = mid_point - 1
                    else:
                        left = mid_point + 1

        def search(left, right):
            while left <= right:
                mid_point = (left + right) // 2
                if nums[mid_point] == target:
                    return mid_point
                elif nums[mid_point] < target:
                    left = mid_point + 1
                else:
                    right = mid_point - 1
            return -1

        pivot = find_pivot(0, len(nums) - 1)
        if nums[pivot] == target:
            return pivot

        if pivot == 0:
            # [1,2,3,4,5] Array is in sorted order so the whole array should be searched
            return search(0, len(nums) - 1)
        elif target >= nums[0]:
            # [3,4,5,0,1,2] pivot = 3 target = 4 target > nums[0] search [0:pivot]
            # Search in the elements from 0 to the pivot point
            return search(0, pivot)
        else:
            # [3,4,5,0,1,2] pivot = 3 target = 2 target < nums[0] search [pivot:len(nums)-1]
            return search(pivot, len(nums) - 1)
