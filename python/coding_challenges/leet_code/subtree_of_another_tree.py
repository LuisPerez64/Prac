"""
Question: https://leetcode.com/problems/subtree-of-another-tree/
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values
 with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
 The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
from collections import deque

from implementations.data_structures import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.first_implementation(s, t)

    def first_implementation(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Broken down into subproblems. First one find the common root node.
        Any of the traversals would work for this
        """

        def find_common_root(root, sub_root):
            """
            """
            stack = []
            possible_roots = []
            while True:
                while root:
                    stack.append(root)
                    root = root.left

                if stack:
                    root = stack.pop()
                    if root.val == sub_root.val:
                        possible_roots.append(root)
                    root = root.right

                if not root and not stack:
                    break
            return possible_roots

        def same_tree(p: TreeNode, q: TreeNode):
            queue = deque([p, q])

            while queue:
                p_node = queue.popleft()
                q_node = queue.popleft()
                if p_node and q_node:
                    if p_node.val != q_node.val:
                        return False
                    queue.append(p_node.left)
                    queue.append(q_node.left)
                    queue.append(p_node.right)
                    queue.append(q_node.right)
                elif p_node or q_node:
                    # One of them is pointing to a NULL node
                    return False
            return True

        possible_roots = find_common_root(s, t)
        if not possible_roots:
            return False
        for root in possible_roots:
            if same_tree(root, t):
                return True
        return False
