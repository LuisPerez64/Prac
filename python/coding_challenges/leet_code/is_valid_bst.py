"""
REVISIT: Attempt the solution outlined in the first_implementations docstring. It's more complex, but should hold
Question: https://leetcode.com/problems/validate-binary-search-tree/submissions/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
from implementations.data_structures import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.second_implementation(root)

    def first_implementation(self, root: TreeNode) -> bool:
        """
        Can be solved using level order traversal of the tree.
        Then validating the tree in the format of the heap property a[n] > a[n+1] < a[n+2]
            excluding the nodes that are null from the calculation as no_ops.
        """
        pass

    def second_implementation(self, root: TreeNode) -> bool:
        """
        Solve using inorder traversal algo ensuring that at every instance of an insert into the resulting array
        it satisfies the property cur > pre
        Time Complexity: O(n)
        Space Complexity: O(log n)
            At most one full run the height of the tree could be stored in the stack.
        """
        if root is None:
            # Empty tree is a valid BST
            return True

        stack = []
        prev = float('-inf')
        # In order traversal Left, Root, Right
        while True:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if root.val <= prev:
                    # If at any point the condition of the tree being in order is violated break.
                    return False
                prev = root.val
                root = root.right
            if not (stack or root):
                break
        return True