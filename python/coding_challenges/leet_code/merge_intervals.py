"""
REVISIT: Base graph theory and the problem is a good one to build upon

Question: https://leetcode.com/problems/merge-intervals/submissions/
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Constraints:

intervals[i][0] <= intervals[i][1]
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.first_implementation(intervals)

    def first_implementation(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort the list of intervals based on their start point.
        If the end interval of n[m] is within the start of n[m+1] then they can be merged.
        Else the element at m will not be able to be merged and should be taken as is.
        Time Complexity: O(n log n) + O(n)
            O(n log n) Using pythons standard sorting lib which uses TimSort
            O(n): Iterating over the sorted array
        Space Complexity: O(1)
            O(1) the sort is done in place, though it uses N auxilary space
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            prev_upper_bound = merged_intervals[-1][1]
            # Check if the current element can be merged with the previous element in the merged_intervals list
            if prev_upper_bound >= interval[0]:
                # [[1,5], [3, 6]] 3 is within the bound check so it fits in the interval.
                # If appending this element would actually increase the previous interval overwrite it
                merged_intervals[-1][1] = max(prev_upper_bound, interval[1])
            else:
                # The current interval is outside of the scope of the previous.
                merged_intervals.append(interval)
        return merged_intervals
