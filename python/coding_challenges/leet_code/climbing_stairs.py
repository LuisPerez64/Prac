"""
Question: https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    memo = [0, 1, 2]
    # Calculate the possible branch based off of the steps
    for idx in range(3, n + 1):
        memo.append(memo[idx - 1] + memo[idx - 2])
    return memo[n]


# First attempt at the problem which did not yield a valid solution.
#     def climbStairs(self, n: int) -> int:
#         # Branching tree approach for this so every "node" has the spawn of its possible decisions.
#         if n <= 2:
#             return n
#         possible_steps_at_stair = {n: {1: 0, 2: 0}}
#         # Start walking backwards as the possible number of steps you can take at any
#         # n would be the possible steps taking at n+1 + possible steps taken at n
#         # Populating the n-1 value as theres only one choice there and complicating the logic for it is unneeded
#         for step in range(n - 1, 0, -1):
#             # At this step get the sum total of possible steps if 2 and 1 step were taken
#             possible_steps_at_stair \
#                 .setdefault(step,
#                             {2: possible_steps_at_stair[step + 1][2] + 1 if step + 2 <= n else 0,
#                              1: possible_steps_at_stair[step + 1][1] + 1})
#         first_step = possible_steps_at_stair[1]
#         return first_step[1] + first_step[2]


print(climb_stairs(5))
