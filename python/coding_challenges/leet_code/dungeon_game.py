"""

Question: https://leetcode.com/problems/dungeon-game/solution/
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid.
Our valiant knight (K) was initially positioned in the top-left room and must fight his way
through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0
or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms;
other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward
or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
 path RIGHT-> RIGHT -> DOWN -> DOWN.
[
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]

Note:
The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        return self.first_implementation(dungeon)

    def first_implementation(self, dungeon: List[List[int]]) -> int:
        """
        Movements either right or downward.
        Amount of health needed to survive is 1
        Possible conditions at each cell visited.
            Dmg: (-hp) health decreases by the value.
            Pot: (+hp) health increases by this value reduces the amount of health needed at point X
            Nul: (0)   health not affected
        Problems:
            Determine the amount of health that will need to be added to survive each cell.
            Determine which path was taken if a choice of origin is available (a cell exists to the left or above)

        NOTES: Starting this process from the end, and backtracking through to get the best choice
            Need to review other DP solutions and attempt them in the same manner to encourage bottom-up design.
        """
        rows = len(dungeon)
        cols = len(dungeon[0])
        def health_needed_to_survive(cur_cell):
            return 1 if cur_cell > 0 else cur_cell * -1 + 1

        # Fill the matrix up to not overwrite the initial data else could just use dungeon instead of dp
        dp = [[0] * cols for _ in range(rows)]

        # Initialize the dungeons last grid with the health needed
        dp[-1][-1] = health_needed_to_survive(dp[-1][-1]) or 1

        for row in range(rows - 1, 0, -1):
            dp[-1][row-1] = health_needed_to_survive(dp[-1][row] - dungeon[-1][row-1])

        for col in range(cols-1, 0, -1):
            dp[col-1][-1] = health_needed_to_survive(dp[col][-1] - dungeon[col-1][-1])

        for row in range(rows - 2, -1, -1):
            for col in range(cols - 2, -1, -1):
                dp[row][col] = min(1, health_needed_to_survive(dp[row+1][col] - dungeon[row][col]),
                                   health_needed_to_survive(dp[row][col+1] - dungeon[row][col]))

        return dp[0][0]

    #    def first_implementation(self, dungeon: List[List[int]]) -> int:
    #     """
    #     Movements either right or downward.
    #     Amount of health needed to survive is 1
    #     Possible conditions at each cell visited.
    #         Dmg: (-hp) health decreases by the value.
    #         Pot: (+hp) health increases by this value reduces the amount of health needed at point X
    #         Nul: (0)   health not affected
    #     Problems:
    #         Determine the amount of health that will need to be added to survive each cell.
    #         Determine which path was taken if a choice of origin is available (a cell exists to the left or above)
    #     """
    #
    #     dp = [[dungeon[x][y] for y in range(len(dungeon[0]))] for x in range(len(dungeon))]
    #     row = col = 0
    #     for col in range(len(dungeon[0])):
    #         for row in range(len(dungeon)):
    #             # At the current position in the dungeon if its a damaging grid you'd need dmg * -1 + 1 to survive.
    #             added_health_to_survive = 0 if dungeon[row][col] > 0 else dungeon[row][col] * -1 + 1
    #             # The current health is independent
    #             if row > 0 and col > 0:
    #                 # Can choose the previous location based on benefits
    #                 dp[row][col] = added_health_to_survive + min(dp[row - 1][col], dp[row][col - 1])
    #             elif row > 0:
    #                 # Can only have come from the right.
    #                 dp[row][col] = dp[row - 1][col] + added_health_to_survive
    #             elif col > 0:
    #                 # Can only have come from above.
    #                 dp[row][col] = added_health_to_survive - dungeon[row][col - 1]
    #             else:
    #                 dp[row][col] = added_health_to_survive
    #     res = dp[row][col]
    #     return res * -1 if res < 0 else res


print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
# Solution().calculateMinimumHP([[-2, -3, 3]])
