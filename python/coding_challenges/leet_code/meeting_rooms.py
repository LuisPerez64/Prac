"""
Question: https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        return self.first_implementation(intervals)

    def first_implementation(self, intervals: List[List[int]]) -> bool:
        """
        Check the intervals and if none overlap then all meetings could be attended.
        Need to sort the input first driving the solution to O(n log n) time complexity.
        """
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda k: (k[0], k[1]))

        can_go = intervals.pop(0)
        for interval in intervals:
            if can_go[1] <= interval[0]:
                can_go[1] = max(can_go[1], interval[1])
            else:
                return False
        return True
