"""
Question: https://leetcode.com/problems/combination-sum-iii/solution/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice,
and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.

Constraints:

2 <= k <= 9
1 <= n <= 60
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.first_implementation(k, n)

    def first_implementation(self, k: int, n: int) -> List[List[int]]:
        """
        Make combinations through the use of a backtracking function.
        The values need to be unique and of length k for the max combination.
        Once we've reached the max combination then we return
        """
        results = []

        def backtrack(remain: int, cur: list, next_start: int):
            """
            """
            if remain == 0 and len(cur) == k:
                # Valid make a copy of the list else its elements will be affected by next iteration.
                results.append(list(cur))
                return True
            elif remain < 0 or len(cur) == k:
                # We've reached an invalid combination or have gone past the upper bound
                return False

            for cur_num in range(next_start, 9):
                # THe cases where a start value is < the current is handled outside of the scope of cur in the running loop.
                # Add the current number into the current combination
                cur.append(cur_num + 1)
                backtrack(remain - cur_num - 1, cur, cur_num + 1)
                # Backtrack and remove the curent value from the current combination before trying for the next.
                cur.pop()

        backtrack(n, [], 0)
        return results
