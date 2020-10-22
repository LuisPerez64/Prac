"""
REVISIT: This is a good concept to keep in mind as it is simple, and efficient.
Question: https://leetcode.com/problems/daily-temperatures/
Given a list of daily temperatures T, return a list such that, for each day in the input,
 tells you how many days you would have to wait until a warmer temperature.
  If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
 Each temperature will be an integer in the range [30, 100].
"""
from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        return self.first_implementation(T)

    def first_implementation(self, T: List[int]) -> List[int]:
        """
        Iterate over the array in reverse.
        Get the max val and as long as there's a value less than it decrement the counter for days til
        """
        high_dq = deque()
        result = [0] * len(T)
        high_dq.append((len(T) - 1, T[-1]))
        for idx in range(len(T) - 2, -1, -1):
            temp = T[idx]
            while high_dq and temp >= high_dq[0][1]:
                high_dq.popleft()
            if high_dq and temp < high_dq[0][1]:
                result[idx] = high_dq[0][0] - idx
            else:
                result[idx] = 0
            high_dq.appendleft((idx, temp))
        return result

    def second_implementation(self, T: List[int]) -> List[int]:
        """
        Same as first implementation but with a minheap
        """
        high_dq = []
        result = [0] * len(T)
        heappush(high_dq, (T[-1], len(T) - 1))
        for idx in range(len(T) - 2, -1, -1):
            temp = T[idx]
            while high_dq and temp >= high_dq[0][0]:
                heappop(high_dq)
            if high_dq and temp < high_dq[0][0]:
                result[idx] = high_dq[0][1] - idx
            else:
                result[idx] = 0
            heappush(high_dq, (temp, idx))
        return result
