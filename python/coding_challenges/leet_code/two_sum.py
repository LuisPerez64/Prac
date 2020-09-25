"""
Questions: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Implies that every input will have an answer from the wording of the question
    Constraint that the values in the list are unique as only one solution could exist
    the pair needed to make the target must be there only once.

    For this purpose it'd be better to collect the number and the integer that
    would produce the target into a hash table
    """
    compliments = dict()
    for idx, cur_val in enumerate(nums):
        need_val = target - cur_val

        if need_val in compliments:
            return [compliments[need_val], idx]
        compliments[cur_val] = idx
    return []
#         right_idx = len(nums) - 1
#         while left_idx < right_idx:
#             left = nums[left_idx]
#             right = nums[right_idx]
#             if

#         for idx_a in range(len(nums)):
#             for idx_b in range(idx_a+1, len(nums)):
#                 if (nums[idx_a] + nums[idx_b]) == target:
#                     return [idx_a, idx_b]
