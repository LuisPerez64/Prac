"""
REVISIT: Same logic employed as daily_temperature_ranges problem. Anotate this
Question: https://leetcode.com/problems/next-greater-element-i/
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Use a minheap to keep track of the elements that have occured so far.
        If at any idx in the array the current value is > the heap at 0
            keep popping off of it until the number at the start of the heap is no longer smaller.
            On every element popped off signal that the next bigger value for it is X in a hashmap.
        """
        from heapq import heappop, heappush
        min_heap = []
        gt_map = {}

        for num in nums2:
            # Nums1 is a subset of nums2
            # Drain the min_heap until a number greater than the one we're at is found.
            while min_heap and num > min_heap[0]:
                gt_map[heappop(min_heap)] = num

            heappush(min_heap, num)

        while min_heap:
            # Empty out the rest of the heap as these values have no next num greater than them.
            gt_map[heappop(min_heap)] = -1
        return [gt_map.get(num) for num in nums1]