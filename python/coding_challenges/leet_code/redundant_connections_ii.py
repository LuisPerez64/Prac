"""
REVISIT: This is a hellish question. Finding the edge equation to ensure that we return the first 
    instance if there exist multiple candidates needs a deep look in.
NOTE: I got close to the answer, and the in degrees portion, but couldn't figure out the exact link 
    to get it to reflect properly. Review this as the added piece is just an extension from the first.

Question: https://leetcode.com/problems/redundant-connection-ii/
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root)
for which all other nodes are descendants of this node, plus every node has exactly one parent, 
except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes 
(with distinct values 1, 2, ..., N), with one additional directed edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] 
that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3
Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
from typing import List

from implementations.data_structures import DSU


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        return self.first_implementation(edges)

    def first_implementation(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()

        # find the root node, which is the node with the no parents 
        # if no such node exists, then elect the node with the least parents
        degrees = [0] * (len(edges) + 1)
        ans1 = None
        ans2 = None
        # Get the in degrees for the nodes in the graph.
        # If at any point we find multiple in degrees then we log this as an occurence of a 
        # failure. Because of the constraints of the problem one node has to win out.
        # A graph like this [[1,2],[1,3],[2,3], [3,1], [1,4], [4, 2]] is invalid due to multiple double parent nodes.

        for src, dst in edges:
            if degrees[dst] > 0:
                # We've found an instance of multiple out in nodes getting referenced.
                # update the instance of the last seen cycle.
                # The answer would be either the cycle that get's created from the previous node
                # or the current edge itself. REVIWE THIS CONCEPT!!!
                ans1 = [degrees[dst], dst]
                ans2 = [src, dst]
            degrees[dst] = src
            # print(degrees, src, dst, ans1, ans2)

        for edge in edges:
            if edge == ans2:
                # no need to check the edge that was denoted as a failure point.
                continue
            if not dsu.union(*edge):
                # We've found a cycle. 
                # Instead of returning the current edge if we found one from the degrees return it.
                return edge if not ans1 else ans1
        return ans2


"""
Example Input:

[[1,2],[1,3],[2,3], [3,1], [1,4]]
[[1,2], [1,3], [2,3]]
"""
