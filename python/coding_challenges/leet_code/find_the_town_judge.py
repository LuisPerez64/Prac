"""
REVISIT: First graph problem, and its explanation on relationship between the vertices is simple enough to focus on.

Question: https://leetcode.com/problems/find-the-town-judge/solution/
In a town, there are N people labelled from 1 to N.  There is a rumor that
one of these people is secretly the town judge.

If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the
person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Constraints:

1 <= N <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        return self.second_implementation(N, trust)

    def first_implementation(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        trust_somebody = set()
        trusted = set()
        for trust, trustee in trust:
            trust_somebody.add(trust)
            trusted.add(trustee)

        doesnt_trust = trusted.difference(trust_somebody)
        return doesnt_trust and doesnt_trust.pop() or -1

    def second_implementation(self, N: int, trust: List[List[int]]) -> int:
        """
        Use an array to log the amount of people that trust person X
        and another to grab the list of people that person X trusts
        """
        trust_arr = [0 for _ in range(N + 1)]
        for out_trust, in_trust in trust:
            trust_arr[out_trust] -= 1
            trust_arr[in_trust] += 1

        for person in range(1, N + 1):
            # Using this index as there is no 0th person
            if trust_arr[person] == N - 1:
                return person
        return -1

Solution().findJudge(3, [[1,2],[2,3]])
