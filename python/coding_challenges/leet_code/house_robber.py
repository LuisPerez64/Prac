"""
Question: https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
 it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    # Set up base case for the dynamic program.
    rob_results = [nums[0], max(nums[0], nums[1])]
    # The first choices possible have been recorded above for the running tally
    for idx in range(2, len(nums)):
        # Get the running total for robbing the current house and the one two houses before.
        # Or foregoing robbing this house and taking from the previous one
        rob_results.append(max(nums[idx] + rob_results[idx - 2], rob_results[idx - 1]))
    return rob_results[-1]