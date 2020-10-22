"""
Question: https://leetcode.com/problems/max-consecutive-ones/

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0
        for elt in nums:
            if not elt:
                max_counter = max(counter, max_counter)
                counter = 0
            else:
                counter += 1
        return max(max_counter, counter)

    def second_implementation(self, nums: List[int]) -> int:
        """
        use an accumulator to grab the values as we move forward.
        If the value is a 0 reset the count.

        Iterate over the array a second time and grab the max value from the fields.
        """
        count = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                count = 0
            else:
                count += 1
                nums[idx] = count
        return max(nums)