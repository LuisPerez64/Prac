"""
Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they
 add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target,
 where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]

Constraints:

2 <= nums.length <= 3 * 104
-1000 <= nums[i] <= 1000
nums is sorted in increasing order.
-1000 <= target <= 1000
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.first_implementation(numbers, target)

    def first_implementation(self, numbers: List[int], target: int) -> List[int]:
        """
        Input is sorted, so finding the two values that add up to the wanted number
        is a simple sliding window problem.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                # right hand too big so search for a smaller
                right -= 1
            else:
                # left too small search a bigger one
                left += 1

    def second_implementation(self, numbers: List[int], target: int) -> List[int]:
        """
        Iterate over the list trying to find the compliment that fits the wanted value.
        Since the input is sorted at some point we'll find a complimentary value
        to a previous that gives the needed answer in the dict.
        Time Complexity: O(n)
        Space Complexity: O(n)
            For the compliments dict
        """
        compliments = {}
        for idx, val in enumerate(numbers):
            comp = target - val
            if val in compliments:
                return [compliments[val], idx + 1]
            else:
                compliments[comp] = idx + 1
