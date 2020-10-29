"""
Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non decreasing array.
-10^9 <= target <= 10^9
"""
import unittest
from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    # O(logn) implementation for searching through a sorted list with binarySearch
    # Two conditions come into play. If first time seeing the value,
    # it may not be the first time it appears in the array
    # Same is said for the time its found the second time around
    indices = [-1, -1]  # If never found then the default return value is given
    # Two problems to resolve Finding the number and then its absolute first/last indices

    start_idx = 0
    end_idx = len(nums)

    # Divide and Conquer Programming approach
    def get_first_index(arr_slice):
        # All values in the arr_slice must be <= to the target value if the input is sorted
        # Keep decreasing the end value until a point is met thats lower than it
        local_start = 0
        local_end = len(arr_slice)
        while local_start < local_end:
            local_mid = (local_start + local_end) // 2
            if arr_slice[local_mid] < target:
                # Keep checking to the left for a value that's < the target
                local_start = local_mid + 1
            else:
                # Check from the start to see if the
                local_end = local_mid
        return local_end

    def get_last_index(arr_slice):
        """
        Get the index of the last time the value was seen in this sub_array.
        """
        local_start = 0
        local_end = len(arr_slice)
        while local_start < local_end:
            local_mid = (local_start + local_end) // 2
            if arr_slice[local_mid] > target:
                # Keep checking to the left for a value that's < the target
                local_end = local_mid
            else:
                # Check from the start to see if the
                local_start = local_mid + 1
        return local_start

    while start_idx < end_idx:
        mid_point = (start_idx + end_idx) // 2
        if nums[mid_point] == target:
            # Found the value that we're looking for at which point the problem is broken down
            # Split the work out to independent workers for the start/end indices
            # If start_idx == mid_point then the first seen idx of the number is mid_point else
            indices[0] = start_idx + get_first_index(arr_slice=nums[start_idx:mid_point])
            indices[1] = mid_point + get_last_index(arr_slice=nums[mid_point + 1:end_idx])
            break
        elif nums[mid_point] > target:
            end_idx = mid_point
        else:
            start_idx = mid_point + 1
    return indices


class Test(unittest.TestCase):

    def test_array_with_valid_target(self):
        actual = tuple(search_range([1, 2, 3, 3, 3, 3, 4, 5, 9], 3))
        expected = (2, 5)
        self.assertEqual(actual, expected)

    def test_array_with_invalid_target(self):
        actual = tuple(search_range([1, 2, 3, 3, 3, 3, 4, 5, 9], 6))
        expected = (-1, -1)
        self.assertEqual(actual, expected)

    def test_array_with_target_repeated_twice(self):
        actual = tuple(search_range([2, 2], 2))
        expected = (0, 1)
        self.assertEqual(actual, expected)

    def test_array_with_target_repeating_odd_number_of_times(self):
        actual = tuple(search_range([2 for _ in range(11)], 2))
        expected = (0, 10)
        self.assertEqual(actual, expected)

    def test_array_with_one_element_thats_target(self):
        actual = tuple(search_range([1], 1))
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_array_with_target_at_last_idx(self):
        actual = tuple(search_range([1, 2, 3], 3))
        expected = (2, 2)
        self.assertEqual(actual, expected)

    def test_array_with_target_at_first_idx(self):
        actual = tuple(search_range([1, 2, 3], 1))
        expected = (0, 0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=3)
