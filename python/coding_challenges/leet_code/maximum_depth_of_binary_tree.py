"""
Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from implementations.data_structures import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.first_implementation(root)

    def first_implementation(self, root: TreeNode) -> int:
        """
        Use a stack to log the depth from the current node down to its children.
        Implementing the preorder traversal with an added index.
        Time Complexity: O(n) as all nodes are visited.
        Space Complexity: O(n)
        """
        if not root:
            return 0
        stack = [(1, root)]
        depth = 0

        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth
