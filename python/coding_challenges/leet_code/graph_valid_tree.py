"""
REVISIT: Implementation of DFS without recursion, and the Disjoint Set Union usage as well.
Question: https://leetcode.com/problems/graph-valid-tree/
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to
 check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
from typing import List

from implementations.data_structures import DSU


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # return self.second_implementation(n, edges)
        return self.third_implementation(n, edges)

    def first_implementation(self, n: int, edges: List[List[int]]) -> bool:
        """
        Produce an adjaceny dict for the nodes.
        Iterate over the nodes using DFS and if at any point we visit a node
        that's already marked as visited. We've found a cycle.
        """

        connections = defaultdict(set)
        for nde_a, nde_b in edges:
            connections[nde_a].add(nde_b)
            connections[nde_b].add(nde_a)
        print(n, edges, connections)
        seen = set()

        def dfs(cur_node: int, parent=None) -> bool:
            if cur_node in seen:
                return False
            valid = True
            seen.add(cur_node)
            # Safeguarding for nodes that have no children.
            for neighbor in connections.get(cur_node, []):
                if parent is not None and neighbor == parent:
                    # Don't retrace from the node that lead to this one.
                    continue
                valid = valid and dfs(neighbor, cur_node)
                if not valid:
                    break
            return valid

        return dfs(0) and len(seen) == n

    def second_implementation(self, n: int, edges: List[List[int]]) -> bool:
        """
        DFS implemented using a deque
        """
        connections = defaultdict(set)
        for nde_a, nde_b in edges:
            connections[nde_a].add(nde_b)
            connections[nde_b].add(nde_a)

        def dfs():
            dq = deque([0])
            parent = {0: -1}
            while dq:
                nde = dq.pop()
                for neighbor in connections.get(nde, []):
                    if neighbor == parent[nde]:
                        # This child is being iterated through from the parent node.
                        # It's not an invalid connection.
                        continue
                    if neighbor in parent:
                        # This nodes already been visited by some other node.
                        return False
                    dq.append(neighbor)
                    parent[neighbor] = nde
            return len(parent) == n

        return dfs()

    def third_implementation(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return False
        # Ensure that there only exists one root in the graph.
        return len(set([dsu.find(c) for c in range(n)])) == 1
