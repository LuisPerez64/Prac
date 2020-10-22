"""
REVISIT: Implement this once more, and get the logic working in the first solutions.
Question: https://leetcode.com/problems/shortest-distance-to-target-color/
You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c,
return the shortest distance between the given index i and the target color c.
If there is no solution return -1.



Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation:
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
"""
from bisect import bisect
from typing import List
# class Solution:
#     def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
#         color_map = defaultdict(list)

#         for idx in range(len(colors)):
#             color = colors[idx]
#             color_map[color].append(idx)
#         res = []
#         for idx, color in queries:
#             cur = color_map[color]
#             if not cur:
#                 res.append(-1)
#             else:
#                 # find the location where the idx would appear in the list of indices, that is a sorted list.
#                 in_idx = bisect.bisect(cur, idx)
#                 if in_idx == 0:
#                     res.append(cur[0])
#                 elif in_idx == len(cur):
#                     res.append(cur[-1])
#                 else:
#                     # need to determine if we select the previous or next element from the in_idx
#                     res.append(min(abs(idx - cur[in_idx-1] ), abs(idx - cur[min(in_idx, len(cur) -1)])))

#         return res



class Solution:
    def shortestDistanceColor(self, c: List[int], q: List[List[int]]) -> List[int]:
        C, A = {}, []
        for i,j in enumerate(c):
            if j in C: C[j].append(i)
            else: C[j] = [i]
        for [i,d] in q:
            if d not in C:
                A.append(-1)
                continue
            I = bisect.bisect(C[d],i)
            A.append(min(abs(i-C[d][I-1]),abs(i-C[d][min(I,len(C[d])-1)])))
        return(A)