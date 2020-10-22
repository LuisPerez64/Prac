"""
Question: https://leetcode.com/problems/design-hit-counter/
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that
calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing).
You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up:
What if the number of hits per second could be very large? Does your design scale?


"""
from heapq import heappop, heappush


class HitCounter:

    def __init__(self, cycle_time=300):
        """
        Initialize your data structure here.
        Use a dict to get O(1) access to the hits at any point in the
        array. If the time is looped by the current ask then remove it.
        """
        self.hit_count = 0
        self.prev_ts = 0
        self.min_heap = []
        self.cur_tally = 0
        self.cycle_time = cycle_time

    def _register_hit(self, timestamp: int, inc_tally=1):
        """
        If the time_stamp is the same as the prev_timestamp don't insert it just
        increase the cur_tally value.
        The inc_tally is normmaly 1, but if we run the gethit call it will be
        a 0 hit, and additional processing of the logic happens as normal.
        """

        if timestamp == self.prev_ts:
            self.cur_tally += inc_tally
            return

        # a new time is seen, insert it. Ensures that the heap doesn't grow past the cycle time.
        heappush(self.min_heap, (self.prev_ts, self.cur_tally))
        # register the current hit for the next instance.
        self.hit_count += self.cur_tally
        self.cur_tally = inc_tally
        self.prev_ts = timestamp
        return self._clean_heap(timestamp)

    def _clean_heap(self, timestamp: int):
        # print('in', timestamp, self.min_heap, self.min_heap and timestamp - self.min_heap[0][0] >= self.cycle_time)
        while self.min_heap and timestamp - self.min_heap[0][0] >= self.cycle_time:
            self.hit_count -= heappop(self.min_heap)[1]

        return self.hit_count

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._register_hit(timestamp)
        if len(self.min_heap) > self.cycle_time:
            # start some cleanup as the user is only making calls to hit and not getting anything. Relieves the strain
            # later on.
            # Could combine this with the timestamp validation and remove the values once we've looped
            self._clean_heap(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self._register_hit(timestamp, 0)
        return self._clean_heap(timestamp) + self.cur_tally

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
