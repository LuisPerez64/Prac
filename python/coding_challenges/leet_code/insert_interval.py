"""
Question: https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # return self.first_implementation(intervals, newInterval)
        return self.second_implementation(intervals, newInterval)

    def first_implementation(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Go over the intervals array and since its sorted based on start on the interval we can skip that step.
        Try to find the place where the newInterval belongs based on the constraint that the order of the intervals
        needs to be sorted based on the start point.
        base cases:
            new_interval.end < intervals[0].start: prepend new_interval to intervals and return intervals as theres no intersection
                `return [new_interval] + intervals`
            new_interval.start > intervals[-1].end: append new_interval to intervals and return intervals as it's not intersection
                return intervals + [new_interval]
        edge cases:
            intervals is empty: return the list with just the new_interval.
            intervals size is 1: insert new_interval into the intervals list based on its start to preserve order.
                new_interval becomes None
        new_interval insertion cases: After any case is met new_interval becomes None and the merging proceeds as normal
            new_interval.start <= merged_intervals[-1].end: extend the previously merged_intervals range
            new_interval.start < cur_interval.start: Add new_interval to the merged_intervals before cur_interval
            new_interval.start <= cur_interval.end: extend the range of the current interval to hold the full range
                cur_interval = [min(new_interval.start, interval.start), max(new_interval.end, interval.end)]


        Create the merged_intervals list with the first element from intervals inserted
        At each interval check to see if its start point is within the range of the previous interval
            if merged_intervals[-1].end >= cur_interval.start:
                then extend the range of the previous merged_interval
                merged_intervals[-1].end = max(merged_intervals[-1].end, cur_interval.end)
        If its not then just append that interval to the merged_intervals and continue until all intervals is consumed.
        If the new_interval still exists at the end of this operation then it did not intersect and should be appended
            to the end of the merged_intervals list.
        Return the merged_intervals list.

        Time Complexity: O(n)
            Iterating over the list of intervals.
        Space Complexity: O(1)
            O(n) if taking into account the output
        """
        if not intervals:
            # Edge Case 1:  empty intervals list no merging will be doable.
            return [new_interval]
        if new_interval[1] < intervals[0][0]:
            # Base Case 1: newIntervals end implies that it should be inserted at the start and no overlap occurs.
            return [new_interval] + intervals
        if new_interval[0] > intervals[-1][1]:
            # Base Case 2: newIntervals start is > than the last elements in intervals end so append it
            return intervals + [new_interval]

        if len(intervals) == 1:
            """
            Edge Case 2:
            # To not overwrite the logic for cases where theres only one interval
            # check to see where newInterval could fit. Don't return from here just in case merging needs to occur. 
            """
            if intervals[0][0] < new_interval[0]:
                intervals.append(new_interval)
            else:
                intervals = [new_interval] + intervals
            new_interval = None
        # eliminate the need to verify that merged_intervals[-1] exists.
        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if new_interval:
                # The interval still hasn't found its place.
                if new_interval[0] <= merged_intervals[-1][1]:
                    # extend the previously merged intervals range.
                    merged_intervals[-1] = [min(new_interval[0], merged_intervals[-1][0]),
                                            max(new_interval[1], merged_intervals[-1][1])]
                    new_interval = None
                elif new_interval[0] < interval[0]:
                    # case where the new_interval just needs to be inserted in the intervals list
                    # the rest of the merging will proceed as normal.
                    merged_intervals.append(new_interval)
                    new_interval = None
                elif new_interval[0] <= interval[1]:
                    # case where the end of the current interval would be within the bounds of the new_interval
                    # extend the range of the interval in full.
                    interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]
                    new_interval = None

            # The merging of the intervals can resume as normal.
            prev_upper = merged_intervals[-1]
            if prev_upper[1] >= interval[0]:
                # merge the two intervals as the start of the current is less than the end of the previous.
                merged_intervals[-1][1] = max(prev_upper[1], interval[1])
            else:
                merged_intervals.append(interval)
        # this is handled by base case 1
        # if new_interval:
        #     # the new_interval did not get inserted anywhere as its start bound was higher than the known intervals.
        #     merged_intervals.append(new_interval)
        return merged_intervals
