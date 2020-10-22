"""
Question: https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

from implementations.data_structures import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []

        # only need to count the nodes at the left to get the height.
        # Then the nodes on the right keep going right until you can't
        # any more then try going left. Simple traversal is easiest.
        count = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not root and stack:
                root = stack.pop()
                count += 1
                root = root.right

            if not stack and not root:
                break
        return count
