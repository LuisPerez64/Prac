"""
Question: https://leetcode.com/problems/median-of-two-sorted-arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.first_implementation(nums1, nums2)

    def first_implementation(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge the two arrays, and place their merged values into the "merged" array.
        Stop iteration once the midpoint is met which is calculated through size_merged // 2
        Notes:
            size_merged = size(arr1) + size(arr2)
            mid_point = size_merged // 2
            If size_merged % 2 == 0 then need to add two values so dual midpoints are used
                mid_point_a = mid_point
                mid_point_b = mid_point_a - (1 if size_merged %2 == 0 else 0)

        Time Complexity: O(log (m+n))
            At most m+n/2 loops could occur as the loop short circuits when both midpoints are
            ingested.
        Space Complexity: O(log (m+n))
            The size of the merged array would not exceed the number of loop iterations.
        """
        size_a = len(nums1)
        size_b = len(nums2)
        size_merged = size_a + size_b

        if size_merged == 0:
            raise Exception("No fail value given. Handle this outside this scope.")

        # If the midpoint then stop processing once size of the merged array is above it.
        # added not if the size_merged is even then need to add two values mid_point and mid_point-1
        # The iteration over the two arrays is over once we're past the size of the max mid point
        mid_point_a = size_merged // 2
        mid_point_b = mid_point_a - (1 if size_merged % 2 == 0 else 0)

        merged = []
        idx_a = 0
        idx_b = 0
        while idx_a + idx_b <= max(mid_point_a, mid_point_b):
            if idx_a < size_a and idx_b < size_b:
                # Both are still in bounds so check both for insertion.
                num_a = nums1[idx_a]
                num_b = nums2[idx_b]
                if nums1[idx_a] <= nums2[idx_b]:
                    cur_num = nums1[idx_a]
                    idx_a += 1
                else:
                    cur_num = nums2[idx_b]
                    idx_b += 1
            elif idx_a < size_a:
                cur_num = nums1[idx_a]
                idx_a += 1
            else:
                cur_num = nums2[idx_b]
                idx_b += 1
            merged.append(cur_num)
        return (merged[mid_point_a] + merged[mid_point_b]) / 2

    def second_implementation(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merge the two arrays, and increment the needed counters to get the current value.
        Stop iteration once the midpoint is met which is calculated through size_merged // 2
        Notes:
            size_merged = size(arr1) + size(arr2)
            mid_point = size_merged // 2
            If size_merged % 2 == 0 then need to add two values so dual midpoints are used
                mid_point_a = mid_point
                mid_point_b = mid_point_a - (1 if size_merged %2 == 0 else 0)
        Time Complexity: O(log (m+n))
            At most m+n/2 loops could occur as the loop short circuits when both midpoints are
            ingested.
        Space Complexity: O(1)
            The size of the merged array would not exceed the number of loop iterations.
        """
        size_a = len(nums1)
        size_b = len(nums2)
        size_merged = size_a + size_b

        if size_merged == 0:
            raise Exception("No fail value given. Handle this outside this scope.")

        # If the midpoint then stop processing once the number of iterations have reached it.
        # There are two possible midpoints
        # if the size of the merged output % 2 is 0 then
        #   size_output // 2 and size_output // 2 -1
        # else the size_output // 2 is duplicated as the midpoint since n * 2 /2 => n
        mid_point_a = size_merged // 2
        mid_point_b = mid_point_a - (1 if size_merged % 2 == 0 else 0)
        mid_a = 0
        mid_b = 0
        idx_a = 0
        idx_b = 0
        cur_num = 0

        while idx_a + idx_b <= max(mid_point_a, mid_point_b):
            if idx_a < size_a and idx_b < size_b:
                # Both are still in bounds so check both for insertion.
                num_a = nums1[idx_a]
                num_b = nums2[idx_b]
                if nums1[idx_a] <= nums2[idx_b]:
                    cur_num = nums1[idx_a]
                    idx_a += 1
                else:
                    cur_num = nums2[idx_b]
                    idx_b += 1
            elif idx_a < size_a:
                cur_num = nums1[idx_a]
                idx_a += 1
            else:
                cur_num = nums2[idx_b]
                idx_b += 1
            cur_idx = idx_a + idx_b
            if cur_idx == mid_point_a + 1:
                mid_a = cur_num
            if cur_idx == mid_point_b + 1:
                mid_b = cur_num
        return (mid_a + mid_b) / 2
