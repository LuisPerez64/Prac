"""
REVISIT: This is an insanely annoying question that could be used to build up to a set of three problems in
    an interview.
Question: https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i
such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2


Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.first_implementation(arr)

    def first_implementation(self, arr: List[int]) -> int:
        """
        Find the first element where the base condition is met a[i] < a[i+1] then continue climbing
        once we've hit the peak we start the decline. As long as the range is of len >=3 we can return that peak.
        """
        if not arr:
            # Invalid input should raise an error.
            return -1
        base = 0
        possible_peak = -1
        while base < len(arr):
            end = base
            if end + 1 < len(arr) and arr[end] < arr[end + 1]:
                # Climb up and try to find a valid peak
                while end + 1 < len(arr) and arr[end] < arr[end + 1]:
                    end += 1
                possible_peak = end
                if end + 1 < len(arr) and arr[end] > arr[end + 1]:
                    while end + 1 < len(arr) and arr[end] > arr[end + 1]:
                        end += 1
                    if end - base >= 3:
                        return possible_peak
            base = max(end, base + 1)

        return possible_peak
