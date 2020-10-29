"""
Question: https://leetcode.com/problems/jump-game/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
 which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

from typing import Union, List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.second_implementation(nums)

    def first_implementation(self, nums: List[int]) -> bool:
        """
        Validate that it's possible to get to the last index from the first index.
        Steps:
            1) create valid_jumps function from any given index except the last we can jum at most arr[idx] times
                i.e. if it's 2 then the choices are jumping choices[1,2] to the right.
            2) store the value of seen jump locations as long as they provide a path forward.
                The program only cares about whether we can make it not the combinations of making it so as soon
                as one is met then return
            3) start from the end and iterate to the left until the start of the array is found.
        Time Complexity: O(n) * O(max(m))
            O(n): Iteration through the nums array
            O(max(m)): Largest choice point in the array.
        Space Complexity: O(n)
            For the memoization arr.
        """
        # create memo array.
        # values are either we can get to the right most from that step or not.
        memo: List[Union[None, bool]] = [None for _ in range(len(nums))]
        bound = len(nums)
        memo[-1] = True

        def valid_jump(idx):
            cur_jumps = nums[idx]
            # Check to see if one leap could be done from the current index to the end bound
            if cur_jumps + idx >= bound:
                memo[idx] = True

            else:
                # Check if from here we can get to at least one other valid location.
                for jump in range(cur_jumps + 1):
                    if memo[idx + jump] == True:
                        memo[idx] = True
                        break

        for cur in range(len(nums) - 2, -1, -1):
            # iterate through the array in reverse until the 0th index.
            valid_jump(cur)

        return memo[0]

    def second_implementation(self, nums: List[int]) -> bool:
        """
        Start from the left jumping as far as can be done.
        View the max jump that can be done that would extend the current bound and log it.
        We then jump from there instead so the max jump is nums[idx] + the maximum index that can
        be reached if we try from some intermediary path.
        i.e. [3,5,2,1,7,2,1,2,1,2,1]
        3 => [5,2,1] => to get to 5 its -1 so max(2,5) => 5 max jump and continue on this path
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(nums) == 1:
            # Base case start at end.
            return True
        cur_jump = nums[0]
        idx = 1
        can_reach = False
        # Keep trying as long as you can still move forward.
        while idx < len(nums) and cur_jump > 0 and not can_reach:
            can_reach = cur_jump + idx >= len(nums)
            # check if stopping at this node and jumping from here on would be beneficial.
            cur_jump = max(cur_jump - 1, nums[idx])
            idx += 1
        return can_reach

# print(Solution().canJump([3, 5, 2, 1, 7, 2, 1, 2, 1, 2, 1]))
