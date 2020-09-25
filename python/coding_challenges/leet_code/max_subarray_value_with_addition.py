"""
Question: https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
 more subtle.
"""


def max_subarray_with_addition(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    cur_tally = nums[0]
    cur_highest = nums[0]
    for num in nums[1:]:
        # prev_highest = cur_tally
        cur_tally = num + cur_tally
        cur_highest = max(cur_tally, cur_highest, num)
        if num > cur_tally:
            # Throw away the previous tally as a new peak has been found
            cur_tally = num

    return cur_highest


if __name__ == '__main__':
    max_subarray_with_addition([-2, 1, -3, 4, -1, 2, 1, -5, 4])
