"""
Question: https://leetcode.com/problems/moving-average-from-data-stream/
Given a stream of integers and a window size, calculate the moving
average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._generator = self._moving_average(size)
        self._generator.send(None)

    def _moving_average(self, size):
        """
        Use a generator function to calculate these fields at run time.
        This may be a bit of overkill but it would be the way to resolve it
        without the needed context of the class.
        """
        cur_sum = 0
        dq = deque(maxlen=size)
        while True:
            val = yield
            if len(dq) >= size:
                cur_sum -= dq.popleft()
            dq.append(val)
            cur_sum += val
            yield cur_sum / len(dq)

    def next(self, val: int) -> float:
        tmp = self._generator.send(val)
        next(self._generator)
        return tmp



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)