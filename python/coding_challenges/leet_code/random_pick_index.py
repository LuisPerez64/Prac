"""
REVISIT: Reservoir sampling makes sense, but need to be able to explain it if need be.
    https://en.wikipedia.org/wiki/Reservoir_sampling
Question: https://leetcode.com/problems/random-pick-index/
Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int], reservoir_size=1):
        self.nums = nums
        self.reservoir_size = reservoir_size

    def pick(self, target: int) -> int or list:
        """
        Using reservoir sampling to grab the value when/if it comes in.
        Iterate over the array. Select the first element that fits the criteria for selection.
        Continue iterating over the array, comparing if the value attained randomly should be used to
        replace the element. Implementing this with the full reservoir sample criteria.

        Since we're only picking one element at any point no need to clear out the
        reservoir.
        """
        reservoir = []
        sample = 0
        for idx, num in enumerate(self.nums):
            if num == target:
                if len(reservoir) < self.reservoir_size:
                    # keep appending until we've hit the initial limit.
                    reservoir.append(idx)
                else:
                    # generate a random number in the range of the current idx in the array.
                    res = random.randint(0, sample)
                    # If the random index can fit in the array then we replace the value that exists at that index.
                    # ensuring that the end value is a random list without scrambling the whole array.
                    if res < self.reservoir_size:
                        reservoir[res] = idx
                # Increase the sample range to allow a wider spread in the choices getting made from here on.
                sample += 1

        if self.reservoir_size == 1:
            return reservoir[0]
        else:
            return reservoir
