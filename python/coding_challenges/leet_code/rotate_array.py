"""
REVISIT: Do at least one more implementation
Question: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:
    1 <= nums.length <= 2 * 10^4
    It's guaranteed that nums[i] fits in a 32 bit-signed integer.
    k >= 0
"""
from typing import List


def rotate_array(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Time Complexity: O(k % len(nums)) -> O(n)
    Space Complexity: O(1) size of the input array does not grow/shrink
    """
    # Pop unshift solution. Remove the element at the end, and place it at the start of the array.
    # Remove multiple cycles as 2 % 5 and 7 % 5 yield the same result.
    for idx in range(k % len(nums)):
        last_val = nums.pop()
        nums.insert(0, last_val)
