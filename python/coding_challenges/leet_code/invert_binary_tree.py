"""
REVISIT: This is another instance of traversal algos
Question:https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
from collections import deque

from implementations.data_structures import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.first_implementation(root)

    def first_implementation(self, root: TreeNode) -> TreeNode:
        """
        Inversion is stated as at each root take its
        left and right child and swap them.
        Algo:
            While can go left keep ingesting left nodes until you've reached the bottom.
            Place them in a stack on each iteration. Bubble up the stack and do the swaps for children of the current node.
            Do the same for the right.
            Pop again and swap.
            Reach bottom left node.

        """
        if not root:
            return root

        def swap_children(parent: TreeNode):
            """
            This will do the swapping based on a given nodes children. Called from the context
            """
            if not parent:
                return
            tmp_node = parent.left
            parent.left = parent.right
            parent.right = tmp_node

        head = root
        queue = deque([root])
        while queue:
            cur_root = queue.pop()
            swap_children(cur_root)
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

        return head
