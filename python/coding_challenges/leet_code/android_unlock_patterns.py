"""
REVISIT: Need to do this problem, and annotate it as well
Question: https://leetcode.com/problems/android-unlock-patterns/
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9,
count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.



Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys,
the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.





Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.



Example:

Input: m = 1, n = 1
Output: 9
"""


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = {}

        skip[(1, 7)] = 4
        skip[(1, 3)] = 2
        skip[(1, 9)] = 5
        skip[(2, 8)] = 5
        skip[(3, 7)] = 5
        skip[(3, 9)] = 6
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        res = 0

        def bfs(used, last):
            nonlocal res
            if len(used) >= m:
                res += 1
            if len(used) == n:
                return
            for j in range(1, 10):
                if j not in used:  # if j is not used
                    # Sort the vertices of the edge to search in skip
                    edge = (min(last, j), max(last, j))
                    if edge not in skip or skip[edge] in used:
                        bfs(used + [j], j)

        for i in range(1, 10):
            bfs([i], i)
        return res
