"""
REVISIT: All of the tree traversal iterative algos need to be reviewed

Question: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List

from implementations.data_structures import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return self.first_implementation(root)

    def first_implementation(self, root: TreeNode) -> List[List[int]]:
        """
        Iterative solution building on the level_order_traversal algo.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return []
        levels = []
        level = 0
        queue = [root]
        while queue:
            levels.append([])

            level_length = len(queue)

            for idx in range(level_length):
                cur_node = queue.pop(0)
                levels[level].append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            level += 1

        return levels
