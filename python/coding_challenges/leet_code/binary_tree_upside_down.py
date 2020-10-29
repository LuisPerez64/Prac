"""
REVISIT: This question is apparently very common, and the process of rotating a binary tree could definitely come up.
Question: https://leetcode.com/problems/binary-tree-upside-down/

Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

Example 1:
Input: root = [1,2,3,4,5]
Output: [4,5,2,null,null,3,1]
"""

from collections import deque

from implementations.data_structures import TreeNode


class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        return self.pulled_implementation(root)

    def first_implementation(self, root: TreeNode) -> TreeNode:
        """
        Steps:
        1) Find the new root for the tree (left most node). without losing its parent pointer
        2) Perform the rotation operation on each node visited until new root is established
        """
        if root is None:
            return root
        stack = []

        def rotate(node, parent):
            if not parent:
                return
            parent.left = node.left
            right_node = parent.right
            parent.right = node.right
            node.right = parent
            node.left = right_node

        # Find the left_most node in the tree preserving its parents
        while root and root.left:
            stack.append(root.left)
            rotate(root.left, root)
            root = root.left
        root = stack.pop()
        # while stack:
        #     root = stack.pop()
        #     parent = stack and stack.pop() or None
        #     rotate(root, parent)
        #     # stack.append(root)
        return root

    def pulled_implementation(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = deque()
        while root:
            stack.append(root)
            root = root.left

        root = stack[-1]
        left = root.left
        right = root.right
        while len(stack) > 1:
            node = stack.pop()
            # Place the parent as the right hand child of its child node.
            node.right = stack[-1]
            # Place the parents right hand child as the left child of the node
            node.left = stack[-1].right
        # Set the last remaining node in the stack to the children of the original leaf.
        # Though the problem says it will have the constraint of no children placing this here for future implements.
        stack[-1].left = left
        stack[-1].right = right
        return root


tree = TreeNode(val=1)
TreeNode.insert(tree, [2, 3, 4, 5])

Solution().upsideDownBinaryTree(tree)
