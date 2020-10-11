"""
Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes node_p and node_q as the
 lowest node in T that has both node_p and node_q as descendants (where we allow a node to be a descendant of itself).”

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], node_p = 5, node_q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], node_p = 5, node_q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], node_p = 1, node_q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
node_p != node_q
node_p and node_q will exist in the tree.
"""
from implementations.data_structures import TreeNode
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.first_implementation(root, p, q)

    def first_implementation(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Start from the root node and traverse the tree.
        Until we find node_p and node_q both, keep storing the parent pointers in a dictionary.
        Once we have found both node_p and node_q, we get all the ancestors for node_p using the parent dictionary and
        add to a set called ancestors.
        Similarly, we traverse through ancestors for node node_q.
        If the ancestor is present in the ancestors set for node_p, this means this is the first ancestor
        common between node_p and node_q (while traversing upwards) and hence this is the LCA node.
        """

        stack = deque([root])
        parents = {root: None}

        while p not in parents or q not in parents:
            # Keep searching until both are in the dict.
            # Doing a level order traversal until both sides are exhausted.
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)

        # Create an ancestors set to grab all of the ancestors for the individual nodes.
        ancestors = set()

        # Grab all of the parents that lead up to P
        while p:
            ancestors.add(p)
            # Find the current ancestors parent until we get all the way to the root node.
            p = parents[p]

        while q not in ancestors:
            # Keep going up the to the parent node for node_q as long as its not in Ps ancestors list.
            # We'll either get to a common node or reach the point where node_q == root.
            q = parents[q]

        return q
