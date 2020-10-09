"""
REVISIT: The overlapping logic makes sense but may need some visuals to go along with it.
Question: https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        return self.first_implementation(intervals)

    def first_implementation(self, intervals: List[List[int]]) -> int:
        """
        Inverting the interval range logic.
        Since the intervals are not sorted first step is to sort them based on their starting positions
        In the case of an overlap between intervals at n and n-1 we select the element
        with the shortest interval based on the intervals end value.

        i.e. [1,2], [3,20],[4,8],[5,7]
        It would make sense to remove 3->20 interval as the most [4 ->8] could interfere with are 3 others vs 17.
        Even without looking ahead.
        """
        if not intervals:
            return 0
        # Sort the intervals to make the search for overlaps linear
        intervals.sort(key=lambda k: k[0])
        non_overlapping = [intervals[0]]
        for interval in intervals[1:]:
            # check if the current interval overlaps with the previous.
            if non_overlapping[-1][1] > interval[0]:
                # Theres an overlap now selecting which one should be tossed based on the end interval of the two.
                # The start interval of the current has to be >= to the start of the previous
                # It comes down to the width of intervals they're likely to cover.
                #
                if non_overlapping[-1][1] >= interval[1]:
                    non_overlapping[-1] = interval
            else:
                non_overlapping.append(interval)
        return len(intervals) - len(non_overlapping)
